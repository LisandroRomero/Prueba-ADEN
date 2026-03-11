from odoo import models, fields

class StudyPlan(models.Model):
    _name = "university.study_plan"
    _description = "Study Plan"
    name = fields.Char(string="Name")

    career_id = fields.Many2one("university.career", string="Career")

    subject_ids = fields.One2many("university.subject", "study_plan_id", string="Subjects")