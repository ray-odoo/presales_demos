# Copyright 2024 Moduon Team S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    project_id = fields.Many2one("project.project", string="Project")


    def action_create_project_wizard(self):
        self.ensure_one()
        
        view = self.env.ref('sale_project.sale_project_view_form_simplified_template', raise_if_not_found=False)
        if not view:
            return False
        return {
            'name': 'Create a Project from Template',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'project.template.create.wizard',  
            'views': [(view.id, 'form')],
            'target': 'new',
            'context': dict(self.env.context),
        }
