from django.http import JsonResponse
from .models import Transacao

def listar_transacoes(request):
    transacoes = Transacao.objects.all().values(
        'id', 
        'descricao', 
        'valor', 
        'data', 
        'categoria__nome',  # Traz o nome da categoria, não apenas o ID
        'categoria__tipo',  # Traz se é receita ou despesa
        'usuario__nome'     # Traz o nome do usuário
    )
    
    return JsonResponse(list(transacoes), safe=False)
