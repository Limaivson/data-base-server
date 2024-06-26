from .data_base_sales_control.data_base.consultas import Consultas
from django.http import JsonResponse

consultas = Consultas()


def inserir_funcionario(request):
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    response = consultas.inserir_funcionario(nome, cargo)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def listar_funcionarios(request):
    response = consultas.listar_funcionarios()
    if response:
        return JsonResponse({'status': 'success', 'funcionarios': response})
    else:
        return JsonResponse({'status': 'error'})


def deletar_funcionario(request):
    id_funcionario = request.POST.get('id_funcionario')
    response = consultas.deletar_funcionario(id_funcionario)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def atualizar_funcionario(request):
    id_funcionario = request.POST.get('id_funcionario')
    nome = request.POST.get('nome')
    cargo = request.POST.get('cargo')
    response = consultas.atualizar_funcionario(id_funcionario, nome, cargo)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def buscar_funcionario(request):
    id_funcionario = request.POST.get('id_funcionario')
    response = consultas.buscar_funcionario(id_funcionario)
    if response:
        return JsonResponse({'status': 'success', 'funcionario': response})
    else:
        return JsonResponse({'status': 'error'})


def buscar_funcionario_por_nome(request):
    nome = request.POST.get('nome')
    response = consultas.buscar_funcionario_por_nome(nome)
    if response:
        return JsonResponse({'status': 'success', 'funcionario': response})
    else:
        return JsonResponse({'status': 'error'})


def listar_clientes(request):
    response = consultas.listar_clientes()
    if response:
        return JsonResponse({'status': 'success', 'clientes': response})
    else:
        return JsonResponse({'status': 'error'})


def inserir_cliente(request):
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    endereco = request.POST.get('endereco')
    response = consultas.inserir_cliente(nome, telefone, endereco)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def deletar_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    response = consultas.deletar_cliente(id_cliente)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def atualizar_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    nome = request.POST.get('nome')
    telefone = request.POST.get('telefone')
    endereco = request.POST.get('endereco')
    response = consultas.atualizar_cliente(id_cliente, nome, telefone, endereco)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def buscar_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    response = consultas.buscar_cliente(id_cliente)
    if response:
        return JsonResponse({'status': 'success', 'cliente': response})
    else:
        return JsonResponse({'status': 'error'})


def buscar_cliente_por_nome(request):
    nome = request.POST.get('nome')
    response = consultas.buscar_cliente_por_nome(nome)
    if response:
        return JsonResponse({'status': 'success', 'cliente': response})
    else:
        return JsonResponse({'status': 'error'})


def buscar_cliente_por_endereco(request):
    endereco = request.POST.get('endereco')
    response = consultas.buscar_cliente_por_endereco(endereco)
    if response:
        return JsonResponse({'status': 'success', 'cliente': response})
    else:
        return JsonResponse({'status': 'error'})


def listar_pagamentos(request):
    response = consultas.listar_pagamentos()
    if response:
        return JsonResponse({'status': 'success', 'pagamentos': response})
    else:
        return JsonResponse({'status': 'error'})


def inserir_pagamento(request):
    id_cliente = request.POST.get('id_cliente')
    id_funcionario = request.POST.get('id_funcionario')
    tipo_pagamento = request.POST.get('tipo_pagamento')
    valor = request.POST.get('valor')
    data = request.POST.get('data')
    response = consultas.inserir_pagamento(id_cliente, id_funcionario, tipo_pagamento, valor, data)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def deletar_pagamento(request):
    id_pagamento = request.POST.get('id_pagamento')
    response = consultas.deletar_pagamento(id_pagamento)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def atualizar_pagamento(request):
    id_pagamento = request.POST.get('id_pagamento')
    id_cliente = request.POST.get('id_cliente')
    id_funcionario = request.POST.get('id_funcionario')
    tipo_pagamento = request.POST.get('tipo_pagamento')
    valor = request.POST.get('valor')
    data = request.POST.get('data')
    response = consultas.atualizar_pagamento(id_pagamento, id_cliente, id_funcionario, tipo_pagamento, valor, data)
    if response:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


def buscar_pagamento(request):
    id_pagamento = request.POST.get('id_pagamento')
    response = consultas.buscar_pagamento(id_pagamento)
    if response:
        return JsonResponse({'status': 'success', 'pagamento': response})
    else:
        return JsonResponse({'status': 'error'})
