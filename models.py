from odoo import api, models, fields
from datetime import date, datetime

class cerveza (models.Model):
    _name='cerveza.cerveza'
    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    alcohol_rate = fields.Float(string='Contenido de alcohol %')
    precio_unidad = fields.Float(string="Precio por unidad")
    volume_per_unite = fields.Float(string='Volumen alcohol (ml)')
    available = fields.Boolean(string='Disponible')
    productionPack = fields.One2many(comodel_name='cerveza.lote', inverse_name='cerveza_id')
    distributor_id = fields.Many2one(comodel_name='cerveza.distribuidor', string = 'distributor_id')
    
    
class loteProduccion(models.Model):
    _name='cerveza.lote'
    cerveza_id =fields.Many2one(comodel_name='cerveza.cerveza', string='cerveza_id')
    date_start = fields.Date(string='Fecha Inicio')
    date_end = fields.Date(string='Fecha Final')
    quantity = fields.Integer(string='Cantidad')
    state = fields.Selection([ ('proceso', 'En Proceso'), ('completo', 'Completado'), ('espera' , 'En espera de empaquetado')], string = 'Estado')
    pack_id = fields.Many2one(comodel_name='cerveza.empaquetado', string='pack_id')
    
class ingrediente(models.Model):
    _name='cerveza.ingrediente'
    name=fields.Char(string='Ingrediente')
    tipe = fields.Selection([ ('malta', 'Malta'), ('lupulo', 'Lúpulo'), ('levadura' , 'Levadura'), ('agua' , 'agua'), ('otro' , 'otro')], string = 'Tipo')
    available_quantity = fields.Float(string='Cantidad Disponible')
    cerveza_id = fields.Many2many(comodel_name='cerveza.cerveza', string='cerveza_id')

class empaquetado(models.Model):
    _name='cerveza.empaquetado'
    productionPack_id = fields.One2many(comodel_name='cerveza.lote', inverse_name='pack_id')
    packing_date = fields.Date(string='Fecha de Empaquetado')
    quantity = fields.Integer(string='Cantidad')

class distribuidor(models.Model):
    _name='cerveza.distribuidor'
    name=fields.Char(string='Nombre')
    phone=fields.Char(string='Teléfono')
    beers_supplied=fields.One2many(comodel_name='cerveza.cerveza', inverse_name='distributor_id')