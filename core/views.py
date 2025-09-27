from django.contrib import messages
from django.shortcuts import render

from .forms import ContatoForm


def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            # pegando os dados com cleaned_data
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'{nome}')
            print(f'{email}')
            print(f'{assunto}')
            print(f'{mensagem}')
            
            messages.success(request, 'Email enviado com sucesso!') 
            form = ContatoForm()
        else :
            messages.error(request, 'Erro ao enviar o Email')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')