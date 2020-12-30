from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 
estados =(
    ('MG','Minas Gerais'),
    ('SP','São Paulo'),
)
# Create your models here.
class OsCabecalho(models.Model):
    servico = models.CharField(max_length=20,verbose_name = 'Serviço')
    referencia = models.CharField(max_length=20,verbose_name = 'Referência')
    
    cep = models.CharField(max_length=15)
    logradouro = models.CharField(max_length=70)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=70)
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2,choices = estados) #usar choices
    
    dtpedido = models.DateTimeField(default=datetime.now, blank=True,verbose_name = 'Data do Pedido')
    
    #codservicos
 #   
   # termino
  #  
 #   codservico
#    servqtd

   # resp
  #  matricula
 #   nome
#    tempodeslocamento
    #tempoexecucao
   # tempoatendimento
   # tiposerv
    user = models.ForeignKey(User,on_delete = models.PROTECT)
    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
    def __str__(self):
        return self.servico 
#-----------------------
    @property
    def normalizandoCampos(self):
        return '' if self.cidade is None else self.cidade
# isso é para tratar os dados entrgues nesse caso o nome da propriedade
# deverar ser usado no template
