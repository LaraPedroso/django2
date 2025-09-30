from django import forms
from django.core.mail import EmailMessage

from .models import Produto

# formulario comum, não ligado a nenhum modelo do bando de dados.
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        # pegando os dados com cleaned_data
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        email_message = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body=conteudo,
            from_email='no-reply@seudominio.com.br',
            to=['no-reply@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        email_message.send()


# formulario que se baseia em um modelo do django - classe models.Model
class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
