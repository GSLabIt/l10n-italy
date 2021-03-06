from odoo import models


class Invoice(models.Model):
    _inherit = "account.invoice"

    def generate_self_invoice(self):
        res = super(Invoice, self).generate_self_invoice()
        rc_type = self.fiscal_position_id.rc_type_id
        if rc_type.fiscal_document_type_id:
            self.rc_self_invoice_id.fiscal_document_type_id =\
                rc_type.fiscal_document_type_id.id
        if self.fatturapa_attachment_in_id:
            doc_id = self.fatturapa_attachment_in_id.name
        else:
            doc_id = self.reference if self.reference else self.number
        self.rc_self_invoice_id.related_documents = [
            (0, 0, {
                "type": "invoice",
                "name": doc_id,
                "date": self.date_invoice,
            })
        ]
        return res
