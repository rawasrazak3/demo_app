// Copyright (c) 2022, ME and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client Side Scripting', {
	refresh: function(frm) {
	frappe.msgprint("Helloooooo")
	// frappe.throw("errorrrr")
	}



	// onload: function(frm) {
	// 	frappe.msgprint("Hellooo fro onload")
	// }
	
	// validate: function(frm) {
	// 	frappe.throw("Helloooo from throw")
	// }

	// before_save: function(frm) {
	// 	frappe.throw("Hellooo from Before Save")
	// }

	// after_save: function(frm) {
	// 	frappe.throw("Helloo from after save")
	// }

	// enable: function(frm)  {
	// 	frappe.msgprint("Heelloo from Enable function")
	// }

	// age: function(frm) {
	// 	frappe.msgprint("Helloo from age")
	// }

	// family_members_on_form_rendered: function(frm) {
	// 	frappe.msgprint("Hellooo from Family Member")
	// }


	// before_submit: function(frm) {
	// 	frappe.throw("Helloo from before save")
	// }

	// on_submit: function(frm) {
	// 	frappe.msgprint("helloo from on submit")
	// }

	// before_cancel: function(frm) {
	// 	frappe.throw("hellooo from befor cancel")
	// }

	// after_cancel: function(frm) {
	// 	frappe.msgprint("hellooo from afterr cancel")
	// }


//////////////////////////  SETTING INTRO OR THE CONTANT OF THE PAGE ///////////////////////


	// refresh:function(frm){

	// 	// frm.set_intro('Now you can create a new client scriping doctype')

	// 	if(frm.is_new()){
	// 		frm.set_intro('Now you create a new client scriping doctype')
	// 	}

	// }




///////////////////////////   SET VALUES ///////////////////////////////

	// validate:function(frm){


	// 	frm.set_value('full_name',frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name)
	// }

	// 	let row=frm.add_child('family_members',{
	// 		name1:'John',
	// 		relation: 'Father',
	// 		age:60,
	// 	})
	// }



//////////////// Value Fetching ///////////////////////////////

	//frm.doc.first_name

	// after_save:function(frm) {
	// 	frappe.msgprint(__("The full name is '{0}'",
	// 			[frm.doc.first_name + " "+ frm.doc.middle_name + " "+ frm.doc.last_name]))
	

	// 	for (let row of frm.doc.family_members) {
	// 		frappe.msgprint(__("{0}. The family member name is '{1}' and the relation is '{2}'",
	// 				[row.idx,row.name1,row.relation]))
	// 	}
	// }






/////////////////////////           BUTTONS         ////////////////////////

	// refresh:function(frm) {
		
		
		// frm.add_custom_button('Click me',() => {
		// 	frappe.msgprint(__('You clicked me!!!!'));

		// })


	// 	frm.add_custom_button('Click me1',() =>{
	// 		frappe.msgprint(__('You Clicked 1!!!!!!'));
	// 	},'Click me')

	// 	frm.add_custom_button('Click me2',() =>{
	// 		frappe.msgprint(__('You Clicked 2!!!!!!'));
	// 	},'Click me')
	
	
	// }






});
//////////////////////   CHILD TABLE SCRIPTS  ///////////////////

frappe.ui.form.on('Family Member', {
		//cdt is child doctype name ie family members
		//cdn is the row name

	// name1: function(frm) {
	// 	frappe.msgprint("Helloo from name1 ")
	// }

	// age(frm,cdt,cdn) {
	// 	frappe.msgprint("Helloo from age")
	// }

	
})





