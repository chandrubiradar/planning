# Copyright (c) 2022, Seyfert and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
from frappe import _
import frappe

"""def execute(filters=None):
	columns, data = [], []
	return columns, data"""


def execute(filters = None):
    return get_columns(), get_data(filters)

def get_data(filters):
    conditions = "1"
    print(conditions)
    #if(filters.get('campaign')):conditions += f" AND c.campaign ='{filters.get('campaign')}'"
    if(filters.get('department1')):conditions += f" AND c.department1 ='{filters.get('department1')}'"
    if(filters.get('supervisor')):conditions += f" AND c.supervisor ='{filters.get('supervisor')}'"
    #if(filters.get('subject')):conditions += f" AND c.subject ='{filters.get('subject')}'"
    
    data = frappe.db.sql(f"SELECT c.department1, c.exp_start_date, c.exp_end_date, c.won_, sum(c.crew_count),count(c.supervisor),c.subject  FROM `tabTask` as c WHERE  {conditions} GROUP BY department1,exp_start_date,exp_end_date ")
    return data


def get_columns():
    return [
            {
            "fieldname": "department1",
            "label": _("Department"),
            "fieldtype": "Data",
            "width": 300,
            },
            {
            "fieldname": "start_date",
            "label": _("Start Date"),
            "fieldtype": "Date",
            "width": 300,
            },
            {
            "fieldname": "end_date",
            "label": _("End Date"),
            "fieldtype": "Date",
            "width": 300,
            },
            {
            "fieldname": "won_",
            "label": _("WON"),
            "fieldtype": "Data",
            "width": 100,
           },
           {
            "fieldname": "crew_count",
            "label": _("Crew Count"),
            "fieldtype": "Data",
            "width": 100,
           },
           {
            "fieldname": "supervisor",
            "label": _("Supervisor"),
            "fieldtype": "Data",
            "width": 100,
           },
           {
            "fieldname": "subject",
            "label": _("Crew Name"),
            "fieldtype": "Data",
            "width": 100,
          },
          
        ]
