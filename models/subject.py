from odoo import models, fields, api

class Subject(models.Model):
    _name = "university.subject"
    _description = "Subject"

    name = fields.Char(string="Name", required=True)
    max_capacity = fields.Integer(string="Max Capacity", default=30)
    professor_id = fields.Many2one("university.professor", string="Professor")
    
    study_plan_id = fields.Many2one("university.study_plan", string="Study Plan")
    enrollment_ids = fields.One2many(
        "university.enrollment", 
        "subject_id", 
        string="Enrollments"
    )

    student_count = fields.Integer(
        string="Enrolled Students",
        compute="_compute_student_count",
        store=True  # store=True permite buscar y ordenar por este campo
    )

    @api.depends("enrollment_ids")
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.enrollment_ids)