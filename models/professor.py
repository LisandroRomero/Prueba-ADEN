from odoo import models, fields,api

class Professor(models.Model):
    _name = "university.professor"
    _description = "Professor"
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    
    # salary = fields.Float(string="Salary")

    subject_ids = fields.One2many("university.subject", "professor_id", string="Subjects")

    subjects_names = fields.Char(
        string="Subjects",
        compute="_compute_subject_names"
    )

    
    def _compute_subject_names(self):
        for record in self:
            record.subjects_names = ", ".join(
                record.subject_ids.mapped("name")
            )