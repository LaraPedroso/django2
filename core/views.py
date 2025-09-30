from django.contrib import messages
from django.shortcuts import render

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    # pode ser post(quando envia) ou pode ser None(quando carrega a pagina)/haver contato ou não
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Email enviado com sucesso!') 
            form = ContatoForm()
        else :
            messages.error(request, 'Erro ao enviar o Email')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        # envia os dados que o usuario preencheu no formulario
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            # commit= cria o objeto mas não salva no banco ainda
            prod = form.save()

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else : 
            messages.error(request, 'Erro ao salvar o produto')
    else:
        #get - formulario vazio
        form = ProdutoModelForm()

    context = {
        'form': form
    }
    return render(request, 'produto.html', context)