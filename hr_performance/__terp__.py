{
    "name": "Performance Review",
    "version": "1.0",
    "author": "Tiny",
    "category" : "Generic Modules",
    "depends" : ["base","hr"],
    "website": "http://www.openerp.com",
    "category": "Generic Modules",
    "description": "A module that Check Performance For the Company Employees.",
    "init_xml": ["hr_performance_view.xml"],
    "demo_xml" : [],
    "update_xml": ["security/ir.model.access.csv","hr_performance_view.xml","hr_performance_report.xml"],
    "active": False,
    "installable": True,
}