// Copyright (c) 2022, Seyfert and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Resource Planning"] = {
	"filters": [
		/*{
			"filedname":"campaign",
			"label":__("Campaign ID"),
			"fieldtype":"Data",
			"width":100,
			"reqd":0
		},*/
		{
			"fieldname":"department1",
			"label":__("Department"),
			"fieldtype":"Link",
			"options":"Department",
			"width":100,
			"reqd":0
		},
		{
			"fieldname":"supervisor",
			"label":__("Supervisor"),
			"fieldtype":"Link",
			"options":"Employee",
			"width":50,
			"reqd":0
		}/*
		{
			"fiedlname":"subject",
			"label":__("Crew Name"),
			"fieldtype":"Data",
			"width":100,
			"reqd":0
		},*/
	]
};


// Copyright (c) 2022, Raj Tailor and contributors
// For license information, please see license.txt
/* eslint-disable */

/* frappe.query_reports["Item Tracker"] = {
	"filters":[
		{
		  "fieldname":"campaign_id",
		  "label":__("Camapaign"),
		  "fieldtype":"Data",
		  "width":100,
		  "reqd":0
		},
		{
		 "fieldname":"project",
		 "label":__("Mashhor Work Order"),
		 "fieldtype":"Link",
		 "options":'Project',
		 "width":100,
		 "reqd":0
	   },
	  {
		 "fieldname":"sap_no",
		 "label":__("SAP NO"),
		 "fieldtype":"Data",
		 "width":100,
		 "reqd":0
	   },
	   {
		 "fieldname":"customer",
		 "label":__("Customer"),
		 "fieldtype":"Link",
		 "options":'Customer',
		 "width":100,
		 "reqd":0
	   },
		]
}; */
