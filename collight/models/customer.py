from django.db import models

married = 'casado(a)'
single = 'solteiro(a)'
MARITAL_CHOICES = [
    (married,'casado(a)'),
    (single, 'solteiro(a)'),
]

male = 'Homem'
female = 'Mulher'
others = 'Outros'
not_informed = 'Prefiro não informar'
GENDER_CHOICES = [
    (male, 'Homem'),
    (female, 'Mulher'),
    (others, 'Outros'),
    (not_informed, 'Prefiro não informar')
]

class Customer(models.Model):
    
    '''
    Classe Customer registra consumidores
    
    Atributos
        doc_type indica o tipo consumidor (pessoa física ou jurídica).
        document indica o nº de registro (CPF ou CNPJ).
        gender indica o gênero da pessoa física ou valor nulo.
        address é um objeto que registra informações de endereço do cliente.
        plot indica o endereço e numeração da residência.
        phone indica o telefone.
        name indica o nome.
        email inidica o email.
        birthdate inidica a data de nascimento.

    
    '''
    
    #doc_type = models.CharField(max_length=2, choices=CUSTOMER_CHOICES, default=individual)
    #document = models.CharField(max_length=14, null=True, unique=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    district = models.CharField(max_length=2)
    #address = models.ForeignKey(
    #        Address, max_length=70, null=True, on_delete=models.SET_NULL, db_column="address")
    #plot = models.CharField(
    #            blank=False, null=False, max_length=35)
    #phone = models.CharField(max_length=11)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, primary_key=True)
    age = models.CharField(max_length=3)
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    profile = models.CharField(max_length=10, default=None)
    def __str__(self) -> str:
        return self.name
