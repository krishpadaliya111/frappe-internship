# Copyright (c) 2026, Krish and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        frappe.msgprint("validate() fired")

    def before_save(self):
        frappe.msgprint("before_save() fired")

    def after_insert(self):
        frappe.msgprint("after_insert() fired")

    def on_update(self):
        frappe.msgprint("on_update() fired")

    def before_submit(self):
        frappe.msgprint("before_submit() fired")

    def on_submit(self):
        frappe.msgprint("on_submit() fired")

    def before_cancel(self):
        frappe.msgprint("before_cancel() fired")

    def on_cancel(self):
        frappe.msgprint("on_cancel() fired")
