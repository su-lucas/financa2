from django.http import JsonResponse
from .models import Categoria

def listar_categorias(request):
    if request.method == 'GET':
        # 1. Pega todas as categorias no banco de dados
        categorias = Categoria.objects.all()
        
        # 2. Transforma cada objeto em um dicionário (O trabalho que o serializer faria)
        dados = []
        for categoria in categorias:
            dados.append({
                'id': categoria.id,
                'nome': categoria.nome,
                'tipo': categoria.tipo
            })
            
        # 3. Devolve a resposta em formato JSON
        # O safe=False é necessário porque estamos enviando uma Lista (dados = []) e não um Dicionário único
        return JsonResponse(dados, safe=False)