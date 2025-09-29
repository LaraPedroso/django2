from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# model é uma class Python que representa uma tabela no banco de dados.
# ao rodar makemigrations e migrate, django cria essa tabela no bd

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.DateField('Ativo?', default=True)

# abstract = True: significa que essa tabela não será criada no banco.
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.CharField('Preço', max_length=100)
    estoque = models.CharField('Estoque', max_length=100)
    imagem = StdImageField('Image', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
    


# signals = 'quer que eu faça alguma coisa antes/depois de salvar esse produto?'

# pre_save → antes de salvar no banco
# post_save → depois de salvar.
# pre_delete → antes de deletar.
# post_delete → depois de deletar.


def produto_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.nome)

# quando Produto for salvo, vai executar o metodo produto_pre_save
signals.pre_save.connect(produto_pre_save, sender=Produto)