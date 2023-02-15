import frappe
from frappe.model.document import Document


class User(Document):
    pass


@frappe.whitelist(allow_guest=True, xss_safe=False, methods=["GET"])
def get_users_list():
    print "Your logic!"


@frappe.whitelist(allow_guest=True, xss_safe=False, methods=["POST"])
def update_user_name(email, first_name, last_name):
    print "Your logic!"
