from rest_framework import serializers
from teste_tecnico.backend.models import DatabaseTeste


class DatabaseTesteSerializer(serializers.ModelSerializer):

    total_vendas = serializers.IntegerField()
    contagem_clientes_mes = serializers.IntegerField()

    class Meta:
        model = DatabaseTeste
        fields = [
            'mes_referencia',
            'total_vendas',
            'tipo_compra',
            'contagem_clientes_mes',
            'ticket_medio_cliente',
        ]
