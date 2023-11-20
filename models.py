from odoo import api, models, fields
from datetime import date, datetime

class cerveza (models.Model):
    _name='cerveza.cerveza'
    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    alcohol_rate = fields.Float(string='Contenido de alcohol %')
    precio_unidad = fields.Float(string="Precio por unidad")
    volume_per_unite = fields.Float(string='Volumen alcohol (ml)')
    available = fields.Boolean(string='Disponible', compute='_compute_disponible')
    productionPack = fields.One2many(comodel_name='cerveza.lote', inverse_name='cerveza_id')
    distributor_id = fields.Many2one(comodel_name='cerveza.distribuidor', string = 'distributor_id')
    
    #@api.depends('inventario')
    #def _compute_disponible(self):
        #for record in self:
            #record.available = True if record.inventario > 0 else False
    
     # Filtros de búsqueda personalizados
    #@api.model
    #def _search_cervezas_agotadas(self):
        #return [('disponible', '=', False)]

    #@api.model
    #def _search_cervezas_disponibles(self):
        #return [('disponible', '=', True)]
    
    
class loteProduccion(models.Model):
    _name='cerveza.lote'
    cerveza_id =fields.Many2one(comodel_name='cerveza.cerveza', string='cerveza_id')
    date_end = fields.Date()
    quantity = fields.Integer()
    state = fields.Selection([ ('proceso', 'En Proceso'), ('completo', 'Completado'), ('espera' , 'En espera de empaquetado')], string = 'Estado')
    pack_id = fields.Many2one(comodel_name='cerveza.empaquetado', string='pack_id')
    
class ingrediente(models.Model):
    _name='cerveza.ingrediente'
    tipe = fields.Selection([ ('malta', 'Malta'), ('lupulo', 'Lúpulo'), ('levadura' , 'Levadura'), ('agua' , 'agua'), ('otro' , 'otro')], string = 'Tipo')
    available_quantity = fields.Float()
    cerveza_id = fields.Many2many(comodel_name='cerveza.cerveza', string='cerveza_id')

class empaquetado(models.Model):
    _name='cerveza.empaquetado'
    productionPack_id = fields.One2many(comodel_name='cerveza.lote', inverse_name='pack_id')
    packing_date = fields.Date()
    quantity = fields.Integer()

class distribuidor(models.Model):
    _name='cerveza.distribuidor'
    name=fields.Char()
    phone=fields.Char()
    beers_supplied=fields.One2many(comodel_name='cerveza.cerveza', inverse_name='distributor_id')