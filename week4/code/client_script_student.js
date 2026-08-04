frappe.ui.form.on("Student", {

    // Runs every time the form is opened or refreshed
    refresh(frm) {
        frappe.show_alert({
            message: "Student Form Loaded Successfully",
            indicator: "green"
        });
    },

    // Runs before saving
    validate(frm) {

        // Student Name validation
        if (!frm.doc.student_name) {
            frappe.throw("Student Name is required.");
        }

        // Date of Birth validation
        if (frm.doc.date_of_birth) {
            let today = frappe.datetime.get_today();

            if (frm.doc.date_of_birth > today) {
                frappe.throw("Date of Birth cannot be in the future.");
            }
        
        }
    },

    // Runs when Gender changes
    gender(frm) {

        if (frm.doc.gender) {
            frappe.msgprint("Gender changed to: " + frm.doc.gender);
        }

    },

    // Runs when Department changes
    department(frm) {

        if (frm.doc.department) {
            frappe.show_alert("Department Selected: " + frm.doc.department);
        }

    },
    total_marks(frm) {
    if (frm.doc.total_marks < 0) {
        frappe.msgprint("Marks cannot be negative");
        frm.set_value("total_marks", 0);
    }
    },

    // Runs when Status changes
    status(frm) {

        if (frm.doc.status == "Inactive") {

            frm.toggle_display("notes", false);

        } else {

            frm.toggle_display("notes", true);

        }

    }

});
 frappe.ui.form.on("Student Subject", {
    marks: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.marks < 0) {
            frappe.msgprint("Marks cannot be negative");
            frappe.model.set_value(cdt, cdn, "marks", 0);
        }
    }
   });
