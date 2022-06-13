from rest_framework.decorators import api_view
from rest_framework.response import Response
from teste_tecnico.backend.models import DatabaseTeste
from teste_tecnico.backend.serializers import DatabaseTesteSerializer


@api_view()
def store_list(request):
    q = DatabaseTeste.objects.all()
    serializer = DatabaseTesteSerializer(q, many=True)
    return Response(serializer.data)
