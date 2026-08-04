total = 0
for row in doc.subjects:
    if row.marks is None:
        row.marks = 0
    if row.marks < 0:
        frappe.throw(f"Marks for {row.subject_name} cannot be negative.")
    if row.marks > 100:
        frappe.throw(f"Marks for {row.subject_name} cannot exceed 100.")
    total += row.marks
doc.total_marks = total
doc.maximum_marks = len(doc.subjects) * 100
if doc.maximum_marks > 0:
    doc.percentage = (doc.total_marks / doc.maximum_marks) * 100
else:
    doc.percentage = 0
