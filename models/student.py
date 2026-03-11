from odoo import models, fields ,api

class Student(models.Model):
    _name = "university.student"
    _description = "Student"
    
    name = fields.Char(string="Name" ,required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")

    enrollment_ids = fields.One2many("university.enrollment", "student_id", string="Enrollments")

    # Cambiamos el nombre para que tenga sentido lógico
    enrollment_count = fields.Integer(
        compute="_compute_enrollment_count",
        string="Total Subjects"
    )

    @api.depends("enrollment_ids")
    def _compute_enrollment_count(self):
        for rec in self: # Usamos 'rec' para no confundir
            rec.enrollment_count = len(rec.enrollment_ids)