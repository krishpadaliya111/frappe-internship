# Week 5 — Controllers, Hooks, Scheduler & the ORM
---

## Day 1 — Controllers & the Document API
**Goal:** Work with documents in Python.
Practised `frappe.get_doc`, `.insert()`, `.save()`, `.submit()`, and `doc.get()/doc.set()`.
Added a computed value inside a controller method and called it from a script,
to understand how Python-side document logic runs on the server.

## Day 2 — Hooks intro: doc_events
**Goal:** Connect logic app-wide, not per-DocType.
Learned that `doc_events` in `hooks.py` lets a single function attach to
`validate`, `on_submit`, etc. across any DocType, instead of writing that logic
inside each DocType's own controller file. This is the same mechanism used
later for the Customer Group Count feature (Day 6).

## Day 3 — Scheduler & background jobs
**Goal:** Timed and async work.
Covered `scheduler_events` (hourly/daily/weekly/cron) and `frappe.enqueue()`.
Wrote and confirmed jobs via bench logs — this groundwork was reused on Day 6
for the overdue-loans job.

## Day 4 — The ORM & Query Builder
**Goal:** `frappe.get_doc` / `get_all` / `qb`.
- `frappe.get_all()` vs `frappe.get_list()` — `get_all()` bypasses user permissions
  (safe for internal/admin scripts); `get_list()` respects the logged-in user's
  permissions (safe for user-facing code).
- `frappe.db.set_value()` — fast direct field update, skips `validate()` and hooks.
  Used for bulk/performance-safe updates where business rules don't need re-checking.
- `frappe.qb` (Query Builder) — used for JOINs and aggregates that `get_all()`
  filters can't express (e.g. joining Student with Student Subject).
- `frappe.db.sql()` — raw SQL, last resort only, no automatic permission checks.

## Day 5 — Custom Fields & Fixtures
**Goal:** Ship customisations cleanly.

Added a Custom Field on the **Student** DocType:
- Label: `Result Remark`
- Fieldname: `custom_result_remark`
- Type: Select
- Options: `Excellent`, `Pass`, `Fail`
- Inserted After: `Student Location`

Configured `fixtures` in `hooks.py` to export this Custom Field, ran
`bench export-fixtures`, then proved portability by creating a brand-new
site (`testsite.local`), installing the `student_management` app fresh on it,
and confirming the field appeared automatically via:
```python
frappe.get_meta("Student").get_field("custom_result_remark")
```
This confirmed the customisation is fully version-controlled and does not
depend on manual UI setup on every new site.

## Day 6 — Practical: Student status + Customer count + Library seed
**Goal:** Apply controllers, validation & counting.

### 1. Student — Percentage + Status
- `percentage` — existing field from Week 4 (server-side computed on save).
- Added Custom Field `Status` (Select: `Failed`, `Pass`, `Excellent`).
- Extended the existing validate Server Script to also set Status based on
  percentage:
  - `< 33` → Failed
  - `33–50` → Pass
  - `> 50` → Excellent

### 2. Customer — Customer Group Count
- Added Custom Field `Customer Group Count` (Int, Read Only) on ERPNext's
  built-in **Customer** DocType.
- Logic lives in `student_management/api.py`, wired via `doc_events` in
  `hooks.py` on Customer's `validate` event:
```python
  def set_customer_group_count(doc, method):
      if doc.customer_group:
          count = frappe.db.count("Customer", {"customer_group": doc.customer_group})
          doc.custom_customer_group_count = count + 1
```
  The `+ 1` accounts for the record currently being saved, since it isn't in
  the database yet at `validate` time.
- Tested by creating two Customers in the same Customer Group and confirming
  the count incremented correctly (0 → 1 → 2).

### 3. Library module seed (Book, Member, Book Loan)
- **Book** — reused the existing Book DocType (already built in earlier weeks);
  added 4 sample records.
- **Member** — built as a brand-new DocType (Module: Student Management), since
  no exact "Member" DocType existed yet (only the unrelated "Library Membership",
  which had no real fields defined). Fields:
  - `member_name` (Data, mandatory)
  - `email` (Data)
  - `phone` (Data)
  - `membership_date` (Date)
  - Naming series: `MEM-.YYYY.-.#####`
  - Added 4 sample records.
- **Book Loan** — existing DocType had no real fields (only the auto-added
  "Amended From" field), so fields were added:
  - `book` (Link → Book, mandatory)
  - `member` (Link → Member, mandatory)
  - `loan_date` (Date, mandatory)
  - `return_date` (Date)
  - `status` (Select: `Issued`, `Returned`, `Overdue`)
  - Book Loan is a submittable DocType — records are Saved then Submitted.
  - Added 3–4 sample loan records linking seeded Books and Members.

### 4. Scheduler job — overdue loans
Added a daily scheduled job in `student_management/api.py`:
```python
def mark_overdue_loans():
    cutoff = add_days(nowdate(), -14)
    loans = frappe.get_all(
        "Book Loan",
        filters={"status": "Issued", "loan_date": ["<", cutoff]},
        pluck="name"
    )
    for loan_name in loans:
        frappe.db.set_value("Book Loan", loan_name, "status", "Overdue")
    if loans:
        frappe.db.commit()
```
Registered under `scheduler_events["daily"]` in `hooks.py`.
Tested manually (without waiting for the real daily trigger) with:
```bash
bench --site site1.local execute student_management.api.mark_overdue_loans
```

---

## Files in this folder
- `hooks.py` — doc_events (Customer group count) + scheduler_events (overdue loans) + fixtures config
- `api.py` — `set_customer_group_count()` and `mark_overdue_loans()` functions
- `fixtures/custom_field.json` — exported Custom Fields (Student: Result Remark, Status; Customer: Customer Group Count)
