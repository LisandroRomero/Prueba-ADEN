from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Enrollment(models.Model):
    _name = "university.enrollment"
    _description = "Enrollment"

    student_id = fields.Many2one(string="Student", comodel_name="university.student")
    subject_id = fields.Many2one(string="Subject", comodel_name="university.subject")
    date = fields.Date(string="Date", default=fields.Date.today())

    # Restricción SQL para evitar duplicados (¡Muy bien hecho!)
    _sql_constraints = [
        (
            'unique_student_subject',
            'unique(student_id, subject_id)',
            'This student is already enrolled in this subject.'
        )
    ]

    # Validación de cupo en el método create (más robusto)
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Verificamos si viene subject_id en los valores
            if vals.get('subject_id'):
                subject = self.env["university.subject"].browse(vals["subject_id"])
                
                # Contamos inscripciones actuales
                enrollment_count = self.search_count([("subject_id", "=", subject.id)])
                
                # Lógica de negocio: Si el cupo está lleno
                if subject.max_capacity > 0 and enrollment_count >= subject.max_capacity:
                    raise ValidationError(f"The subject '{subject.name}' is full.")
                    
        return super(Enrollment, self).create(vals_list)