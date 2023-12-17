from django.db import models

#MODELO (TABELA) DA SESSÃO ORÇAMENTO DA PÁGINA INICIAL (index.html) 
class orcamento(models.Model):
  nome = models.CharField(max_length = 255)
  email = models.CharField(max_length = 255)
  telefone = models.CharField(max_length = 255)
  cep = models.CharField(max_length = 25)
  mensagem = models.TextField(max_length = 3000)

#TABELA DOS USUÁRIOS QUE CRIAM O CADASTRO

class Usuario(models.Model):
  cpf = models.CharField(primary_key = True, max_length = 14) 
  nome_completo = models.CharField(max_length = 255)
  email = models.EmailField()
  bairro = models.CharField(max_length = 150)
  estado = models.CharField(max_length=50)
  telefone = models.CharField(max_length=20)
  cidade = models.CharField(max_length=100)
  numero_casa = models.CharField(max_length=10)
  senha_cadastro = models.CharField(max_length=100) 

  def __str__(self):
    return self.nome_completo #função __str__ é usada para fornecer uma representação legível em texto de uma instância de modelo. No caso desse modelo de Django, a função __str__ está definida para retornar o valor do atributo nome_completo, o que significa que quando você chamar str(objeto_usuario) 


#TABELA DO "FEEDBACK E SUJESTÕES DE MELHORIAS NOS NOSSOS SERVIÇOS E SITE" DA PÁGINA PRINCIPAL  (index.html)

class Comentarios(models.Model):
  nome = models.CharField(max_length = 255)
  email = models.CharField(max_length = 100)
  comentario = models.CharField(max_length = 255)
  

#MODELO PlanoPainel RESPONSÁVEL POR EXIBIR OS REGISTROS, CADASTRADOS NELE, NA PÁGINA PRINCIPAL (index.html)
class PlanoPainel(models.Model):
    nome = models.CharField(max_length=100)
    caracteristica = models.TextField()
    preco = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

#TABELA DO CADASTRO DOS DESENVOLVEDORES E TRABALHADORES DA ECMRKNet, PARA QUE SEJA POSSÍVEL LOGAR NO SISTEMA DE DESENVOLVIMENTO

class Servidor(models.Model):
  cpf = models.CharField(primary_key = True, max_length = 14 )
  nome = models.CharField(max_length = 255)
  senha = models.CharField(max_length = 255)

#TABELA IMAGENS DOS EQUIPAMENTOS DE REDE QUE APARECEREM NA PÁGINA INICIAL (index.html) [ NÃO FUNCIONA 

class Equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    imagem = models.ImageField(upload_to='equipamentos/')
    caracteristica = models.CharField(max_length=200)

    def __str__(self):
        return self.caracteristica


#MODELO DA PÁGINA PLANOS ONDE O USUÁRIO IRÁ SOLICITAR A INSTALAÇÃO DE INTERNET NA SUA PROPRIEDADE

class Instalacao(models.Model):
  nome = models.CharField(max_length = 255)
  email = models.EmailField()
  celular1 = models.CharField(max_length = 15)
  celular2 = models.CharField(max_length = 15)
  telefone = models.CharField(max_length = 15)
  cidade = models.CharField(max_length = 255)
  estado = models.CharField(max_length = 50)
  cep = models.CharField(max_length = 10)
  bairro = models.CharField(max_length = 255)
  endereco = models.CharField(max_length = 255)
  numero = models.CharField(max_length = 5)
  complemento = models.CharField(max_length = 255)
  observacao = models.CharField(max_length = 255)
  cupom = models.CharField(max_length = 100)
  cpf = models.CharField(max_length = 14)

  escolha_plano = [
      ('essencial', 'Plano Essencial'),
      ('basico', 'Plano Básico'),
      ('simples', 'Plano Simples'),
      ('intermediario', 'Plano Intermediário'),
      ('avancado', 'Plano Avançado'),
      ('premium', 'Plano Premium'),
      ('bronze', 'Plano Comercial Bronze'),
      ('prata', 'Plano Comercial Prata'),
      ('ouro', 'Plano Comercial Ouro'),
      ('orcamento', 'Solicitou um Orcamento'),
  ]
  plano = models.CharField(max_length = 255, choices = escolha_plano)

  escolha_roteador = [
      ('tp-lk-c6', 'Roteador TP-LINK C60'),
      ('tp-lk-c5','Roteador TP-LINK C50' ),
      ('tp-lk-c8', 'Roteador TP-LINK C80'),
      ('tp-lk-ac1200','Roteador TP-LINK AC1200'),
      ('tp-lk-ec220','Roteador TP-LINK EC220'),
      ('tp-lk-wr841','Roteador TP-LINK WR841'),
      ('tp-lk-n', 'Roteador TP-LINK N'),
      ('tp-lk-ac12','Roteador TP-LINK AC12'),
      ('tp-lk-we829n','Roteador TP-LINK WE829N'),
      ('tp-lk-we840n','Roteador TP-LINK WE840N-W'),
      ('tp-lk-ax73','Roteador TP-LINK ARCHE AX73'),
      ('mlt-n300','Roteador MULTILASER N300'),
      ('mlt-re163v','Roteador MULTILASER RE163V'),
      ('mlt-re160','Roteador MULTILASER RE160'),
      ('mlt-re172','Roteador MULTILASER RE172'),
      ('mlt-re015','Roteador MULTILASER RE015'),
      ('mlt-re184','Roteador MULTILASER RE184'),
      ('mlt-re185','Roteador MULTILASER RE185'),
      ('mlt-re017','Roteador MULTILASER RE017'),
      ('mlt-re063','Roteador MULTILASER RE063'),
      ('mlt-re011','Roteador MULTILASER RE011'),
      ('intbrs-2100g','Roteador INTELBRAS W5-2100G'),
      ('intbrs-rf-1200','Roteador INTELBRAS RF-1200'),
      ('intbrs-rg-1200','Roteador INTELBRAS RG-1200'),
      ('intbrs-rf-301k','Roteador INTELBRAS RF-301K'),
      ('intbrs-rf-1200f','Roteador INTELBRAS RF-1200F'),
      ('intbrs-gf-1200','Roteador INTELBRAS GF-1200'),
      ('intbrs-rx-1500','Roteador INTELBRAS RX-1500'),
      ('intbrs-w4-300f','Roteador INTELBRAS W4-300F'),
      ('intbrs-iwr-3000n','Roteador INTELBRAS IWR-3000N'),
      ('intbrs-w6-1500','Roteador INTELBRAS W6-1500'),
      ('intbrs-wrn300','Roteador INTELBRAS WRN300'),
      ('intbrs-121ac','Roteador INTELBRAS 121AC'),
      ('intbrs-win240','Roteador INTELBRAS WIN240'),
      ('hwei-ax2s','Roteador HUAWEI AX2S'),
      ('hwei-ws7000','Roteador HUAWEI WS7000'),
      ('hwei-ws7001','Roteador HUAWEI WS7001'),
      ('hwei-ws3y18n','Roteador HUAWEI WS318N'),
      ('hwei-ac1300','Roteador HUAWEI AC1300'),
      ('hwei-ws7000','Roteador HUAWEI WS7000'),
      ('hwei-ws5200','Roteador HUAWEI WS5200'),
      ('hwei-ws7206','Roteador HUAWEI WS7206'),
      ('hwei-ws7100','Roteador HUAWEI WS7100'),
      ('dlnk-d846','Roteador D-LINK DIR-846'),
      ('dlnk-d615','Roteador D-LINK DIR-615'),
      ('dlnk-d610','Roteador D-LINK DIR-610'),
      ('dlnk-d842','Roteador D-LINK DIR-842'),
      ('dlnk-d853','Roteador D-LINK DIR-853'),
      ('dlnk-610n','Roteador D-LINK DIR-610N'),
      ('dlnk-n300','Roteador D-LINK DIR615 N300'),
      ('dlnk-2730e','Roteador D-LINK DSR-2730E'),
      ('dlnk-1360','Roteador D-LINK DIR-1360'),
      ('orcamento','Solicitou por Orçamento'),
  ]

  roteador = models.CharField(max_length = 255, choices = escolha_roteador)


  #MODELO DO EQUIPAMENTO PRINCIPAL, O roteador:
  class equipamento_rede(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 25),
    nome = models.CharField(max_length = 255),
    caracteristica = models.CharField(max_length = 255),
    quantidade = models.CharField(max_length = 10),
    preco = models.CharField(max_length = 10),
    unidades_vendidas = models.CharField(max_length = 10),

  #MODELO DAS MENSAGENS QUE O USUÁRIO ENVIA NA PÁGINA (area_cliente.html)
  class mensagens_area_cliente(models.Model):
    mensagem = models.CharField(max_length = 255)
    