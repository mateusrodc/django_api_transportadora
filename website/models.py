from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=255,null=False,blank=False)
    sobrenome = models.CharField(max_length=255,null=False,blank=False)
    cpf = models.CharField(max_length=14,null=False,blank=False)
    tempo_de_servico = models.IntegerField(default=0,null=False,blank=False)
    remuneracao = models.DecimalField(max_digits=8,decimal_places=2,null=False,blank=False)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Funcionário'

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    combustivel = models.CharField(max_length=200, verbose_name='combustível')
    placa = models.CharField(max_length=7, unique=True)
    chassi = models.CharField(max_length=17, unique=True)
    ano = models.IntegerField()
    capacidade = models.IntegerField()

    class Meta:
        ordering = ['marca', 'modelo']
        verbose_name = 'veículo'


    def __str__(self):
        return '{} {} {}'.format(self.placa, self.marca, self.modelo)

class Atendimento(models.Model):
    motorista = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    data_atendimento = models.DateTimeField(auto_now_add=True)
    destino = models.CharField(max_length=255,null=False,blank=False)
    observacao = models.CharField(max_length=255,null=True,blank=True, verbose_name='observação')

    def __str__(self):
        return '{}: {}'.format(self.motorista, self.destino)

class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14,null=False,blank=False)
    rg = models.CharField(max_length=14,null=False,blank=False)
    curso = models.CharField(max_length=255,null=False,blank=False)
    faculdade = models.CharField(max_length=255,null=False,blank=False)

    class Meta:
        ordering = ['nome','faculdade']
        verbose_name = 'estudante'

    def __str__(self):
        return '{}: {}'.format(self.nome,self.faculdade)



