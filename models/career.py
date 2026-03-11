from odoo import models, fields

class Career(models.Model):
    _name = "university.career"
    _description = "Career"

    name = fields.Char(string="Name")

    study_plan_ids = fields.One2many("university.study_plan", "career_id", string="Study Plans")