from odoo import Command, api, fields, models


class ProjectTemplateCreateWizard(models.TransientModel):
    _inherit = 'project.template.create.wizard'

    lead_id = fields.Many2one('crm.lead', string="Linked Lead")

    def _create_project_from_template(self):
        """
        Override the internal method that creates the project record.
        This method returns the new Project Record (project.project),
        which makes it the perfect place to apply our links.
        """
        new_project = super()._create_project_from_template()

        if self.lead_id:
            new_project.lead_id = self.lead_id.id
            self.lead_id.project_id = new_project.id
        return new_project
