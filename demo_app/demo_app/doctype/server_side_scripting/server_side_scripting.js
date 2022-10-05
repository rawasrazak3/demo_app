// Copyright (c) 2022, ME and contributors
// For license information, please see license.txt

frappe.ui.form.on('Server Side Scripting', {

/////////////////////SERVER SIDE CALL  frm.call()  //////////////    
    // enable: function(frm) {
    //     frm.call({
    //         doc: frm.doc,
    //         method: 'frm_call',
    //         args: {
    //             msg: "Helloo"
    //         },
    //         freeze: true,
    //         freeze_message: __('Calling frm_call Method'),
    //         callback: function(r) {
    //             // frappe.msgprint(r.message)

    //             //frappe.msgprint("SErver side calling Compleated")

    //             //frm.refresh_field('medication_orders');

    //         }
    //     });
    // }


////////////////// Server Side Calls || frappe.call()  //////////
    enable: function(frm) {
        frappe.call({
            method: "demo_app.demo_app.doctype.client_side_scripting.client_side_scripting.frappe_call",
            args:{
                msg: "Helloo"
            },
            freeze: true,
            freeze_message: __('Calling frappe_call Method'),
            callback: function(r) {
                frappe.msgprint(r.message)
            }
        });
    }
});
