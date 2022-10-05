# Copyright (c) 2022, ME and contributors
# For license information, please see license.txt

from email import message
from unicodedata import name
# from xml.etree.ElementPath import _Callback
import frappe
from frappe import _, msgprint
from frappe.model.document import Document
from frappe.query_builder.utils import DocType
from frappe.utils import data

class ServerSideScripting(Document):



#/////////////////     GET DOC     //////////////
        

    # def validate(self):
    #         self.get_document()

    # def get_document(self):
    #         doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
    #         frappe.msgprint(("The first name is {0} and age is {1} ").format
    #         (doc.first_name,doc.age))

    #         for row in doc.get("family_members"):
    #             frappe.msgprint((
    #                     "{0}. TH efamily member name is '{1}' and relation is  '{2}'").format
    #                     (row.idx, row.name1, row.relation)
    #             )

#//////////////// NEW DOC AND DELETE DOC /////////////////

### frappe.new_doc(doctype)

#     def validate(self):
#         self.new_document()

#     def new_document(self):
#         doc = frappe.new_doc('Client Side Scripting')
#         doc.first_name= 'jake'
#         doc.last_name= 'jay'
#         doc.age=25
#         doc.append("family_members",{
#                 "name1":"Jonathan",
#                 "relation":"Sister",
#                 "age":16
#         })

        

#         doc.insert()


#///////////////////   DELETING A DOC ////////////

### frappe.delete_doc(doctype, name)

#     def validate(self):
#         frappe.delete_doc('Client Side Scripting','PR0021')



#/////////////////   Document Methods  //////////////////

#     def validate(self):
#             self.new_document()

#     def new_document(self):
#         doc = frappe.new_doc('Client Side Scripting')
#         doc.first_name= 'HUEW'
#         doc.last_name= 'HANK'
#         doc.age=28
#         doc.insert()

#####some escape hatches that can be used to skip certain checks
#     doc.insert(
#         ignore_permissions=True, #ignore wrote permissions during insert
#         ignore_links=True,  #ignore link validation in the document
#         ignore_duplicate=True  #dont insert if dupliaction entry error thrown
#         ignore_mandatory=True   #insert even idf mandatory fiels are not se
#     )



#///////////////// Data base API  GET_LIST  //////////

### frappe.db.get_list(doctype, or_filters, fields, order_by, group_by, start,page_length)
   
    # def validate(self):
    #     self.get_list()
        
    # def get_list(self):
    #     doc = frappe.db.get_list('Client Side Scripting',
    #             filters={
    #                 'enable': 1
    #             },
    #             fields=['first_name','age']
    #             )

    #     for d in doc:
    #             frappe.msgprint(("The parent name is {0} and age is {1} ").format
    #             (d.first_name, d.age))


#///////////////////   get_value() and set_value()  //////////////
### frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filers, fieldname)
    
    # def validate(self):
    #     self.get_value()

    # def get_value(self):
    #     first_name, age = frappe.db.get_value('Client Side Scripting', 'PR0015', ['first_name', 'age'])
    #     frappe.msgprint(("The parent name is {0} and age is {1} ").format(first_name,age))

##set_value()
##frappe.db.set_value(doctype, name, fieldname, value)(

    # def validate(self):
    #     self.set_value()

    # def set_value(self):
    #     frappe.db.set_value('Client Side Scripting', 'PR0015','age',25)

    #     first_name, age = frappe.db.get_value('Client Side Scripting', 'PR0015', ['first_name','age'])
    #     frappe.msgprint(("The parent name is {0}  and new age is {1} ").format(first_name,age))



##///////////////// SQL QUERY sql() //////////////////////

###frappe.db.sql(query,as_dict)

    # def validate(self):
    #     self.sql()

    # def sql(self):

    #     data = frappe.db.sql("""
    #                             SELECT
    #                                 first_name,
    #                                 age
    #                             FROM
    #                                  `tabClient Side Scripting`
    #                             WHERE
    #                                 enable = 1
    #                              """, as_dict = 1)
        
    #     for d in data:
    #         frappe.msgprint(("The pernt first name is  {0} and age is {1} ").format(d.first_name,d.age))

        
#/////////////////////SERVER SIDE CALL  frm.call()  //////////////
#/////JS CODE ////////{
# frappe.ui.form.on('Server Side Scripting',{
#     enable: function(frm) {
#         frm.call({
#             doc: frm.call,
#             method: 'frm_call',
#             args: {
#                 msg: "Helloo"
#             },
#             freeze: true,
#             freeze_message:__('calling frm_call Method'),
#             callback: function(r) {
#                 frappe.msgprint(r.message)

#                 //frappe.msgprint("SErver side calling Compleated")

#                 //frm.refresh_field('medication_orders');

#             }
#         });
#     }
# });
#////////JS CODE /////// }


    # @frappe.whitelist()
    # def frm_call(self,msg):
    #     import time
    #     time.sleep(5)
    #     frappe.msgprint(msg)

    #     self.mobile_number= 9633774545

        # return "Hi this message is from frm_call"
        

#////////////////// Server Side Calls || frappe.call()  //////////
#//JS /// {
    # enable: function(frm) {
    #     frappe.call({
    #         method: "demo_app.doctype.client_side_scripting.client_side_scripting.frappe call",
    #         args:{
    #             msg: "Helloo"
    #         },
    #         freeze: true,
    #         freeze_message: __('Calling frappe_call Method'),
    #         callback: function(r) {
    #             frappe.msgprint(r.message)
    #         }
    #     });
    # }
#/////JS /// }


    pass
@frappe.whitelist()
def frappe_call(msg):
    # import time
    # time.sleep(5)
    # frappe.msgprint(msg)

    return "Hi this message from frappe_call"
    


#////////////////  exists() or not ////////////////


    # def validate(self):
    #     if frappe.db.exists('Client Side Scripting', 'PR0014'):  ##TRUE
    #         frappe.msgprint(("The document is exists in database"))

    #     else:
    #         frappe.msgprint(("The document is no exist"))

#///////////////////  count()  ////////////////////////////
###frappe.db.count(doctype, filters)

    # def validate(self):
    #     doc_count = frappe.db.count('Client Side Scripting', {'enable': 1}) ##true
    #     frappe.msgprint(("The enable document count is {0}").format(doc_count))

# ////////////////////  SERVER SIDE EVENTS ///////////////////

	# def validate(self):
    # 		frappe.msgprint("hellooo")


	# def before_save(self):
    # 		frappe.throw("Hellooo from before save")


	# def before_insert(self):
    # 		frappe.throw("helloo from before_insert")


	
# def after_insert(args):
#     		frappe.throw("helloo from after insert")

	# def on_update(args):
    # 		frappe.msgprint("hellooo from on upadte")



	# def before_submit(self):
    # 		frappe.msgprint("helloo from before submit")


	# def on_submit(self):
    # 		frappe.msgprint("hellooo from on submit")


	# def on_cancel(self):
    # 		frappe.msgprint("helloo from on cancel")


	# def on_cancel(self):
    # 		frappe.msgprint("helloo from on cancel")


	# def after_delete(self):
	# 	frappe.msgprint("helloo from after delete")    		
    		
    		
    		
# ///////////// VALUE FETCHING //////////////////

	# def validate(self):
	# 	frappe.msgprint(("helloo My full name is '{0}' ").format(
	# 		self.first_name + " " + self.middle_name + " " + self.last_name
	# 	))





	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(("{0}. The family member name is '{1}' and the relation is '{2}'").format(
	# 			row.idx,row.name1,row.relation
	# 		))

