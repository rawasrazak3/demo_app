# Copyright (c) 2022, ME and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ClientSideScripting(Document):
	pass

@frappe.whitelist()
def frappe_call(msg):
    import time
    time.sleep(5)
    frappe.msgprint(msg)

    # return "Hi this message from frappe_call"