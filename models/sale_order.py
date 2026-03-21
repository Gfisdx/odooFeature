import random
import string
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    responsible_employee_id = fields.Many2one(
        'hr.employee',
        string='Ответственный за выдачу товара',
        required=True
    )
    

    new_field = fields.Char(
        string='New Field',
        default=lambda self: ''.join(random.choices(string.ascii_letters, k=10))
    )

    @api.onchange('order_line', 'date_order')
    def _onchange_update_new_field(self):
        for record in self:
            if not record.order_line:  # если строк нет
                record.new_field = ''.join(random.choices(string.ascii_letters, k=10))
            else:
                date_str = record.date_order.strftime('%d/%m/%Y %H:%M:%S') if record.date_order else ''
                total = record.amount_total or 0.0
                record.new_field = f"{date_str} + {total}"
                
    
    @api.constrains('new_field')
    def _check_new_field_length(self):
        for record in self:
            if record.new_field and len(record.new_field) > 30:
                raise ValidationError(
                    "Длина текста должна быть меньше 30 символов!"
                )
