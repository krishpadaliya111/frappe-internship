frappe.ui.form.on("Student Subject", {
    marks: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.marks < 0) {
            frappe.msgprint("Marks cannot be negative");
            frappe.model.set_value(cdt, cdn, "marks", 0);
        }
    }
});
