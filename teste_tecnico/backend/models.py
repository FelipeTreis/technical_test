import decimal
from django.db import models


class DatabaseTeste(models.Model):
    id_loja = models.TextField(primary_key=True)
    id_area = models.TextField(blank=True, null=True)
    tipo_compra = models.TextField(blank=True, null=True)
    contagem_clientes_mes = models.TextField(blank=True, null=True)
    total_vendas = models.TextField(blank=True, null=True)
    mes_referencia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'database_teste'

    @property
    def ticket_medio_cliente(self):
        return round(decimal.Decimal(self.total_vendas) / decimal.Decimal(self.contagem_clientes_mes), 2)
