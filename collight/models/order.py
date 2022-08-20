from collight.models.customer import Customer
from django.db import models


class Order(models.Model):
    
    '''
    Classe Order registra dados gerados pela registro de um pedido,
    a partir da aprovação do pagamento.
    
    Atributos
        status é o status do pedido.
        customer é um objeto que carrega informações do cliente.
        items são os itens (produtos) do pedido.
        closed indica se o pedido foi fechado.
        created_at indica a data de criação do pedido.
    '''
       
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    items = models.CharField(max_length=30, null=False)
    created_at = models.DateField(auto_now=True)
    amount = models.IntegerField()
