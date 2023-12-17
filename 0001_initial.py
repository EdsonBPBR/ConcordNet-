# Generated by Django 3.2.13 on 2023-08-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagem', models.ImageField(upload_to='equipamentos/')),
                ('caracteristica', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='equipamento_rede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instalacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('celular1', models.CharField(max_length=15)),
                ('celular2', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=15)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=255)),
                ('observacao', models.CharField(max_length=255)),
                ('cupom', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('plano', models.CharField(choices=[('essencial', 'Plano Essencial'), ('basico', 'Plano Básico'), ('simples', 'Plano Simples'), ('intermediario', 'Plano Intermediário'), ('avancado', 'Plano Avançado'), ('premium', 'Plano Premium'), ('bronze', 'Plano Comercial Bronze'), ('prata', 'Plano Comercial Prata'), ('ouro', 'Plano Comercial Ouro'), ('orcamento', 'Solicitou um Orcamento')], max_length=255)),
                ('roteador', models.CharField(choices=[('tp-lk-c6', 'Roteador TP-LINK C60'), ('tp-lk-c5', 'Roteador TP-LINK C50'), ('tp-lk-c8', 'Roteador TP-LINK C80'), ('tp-lk-ac1200', 'Roteador TP-LINK AC1200'), ('tp-lk-ec220', 'Roteador TP-LINK EC220'), ('tp-lk-wr841', 'Roteador TP-LINK WR841'), ('tp-lk-n', 'Roteador TP-LINK N'), ('tp-lk-ac12', 'Roteador TP-LINK AC12'), ('tp-lk-we829n', 'Roteador TP-LINK WE829N'), ('tp-lk-we840n', 'Roteador TP-LINK WE840N-W'), ('tp-lk-ax73', 'Roteador TP-LINK ARCHE AX73'), ('mlt-n300', 'Roteador MULTILASER N300'), ('mlt-re163v', 'Roteador MULTILASER RE163V'), ('mlt-re160', 'Roteador MULTILASER RE160'), ('mlt-re172', 'Roteador MULTILASER RE172'), ('mlt-re015', 'Roteador MULTILASER RE015'), ('mlt-re184', 'Roteador MULTILASER RE184'), ('mlt-re185', 'Roteador MULTILASER RE185'), ('mlt-re017', 'Roteador MULTILASER RE017'), ('mlt-re063', 'Roteador MULTILASER RE063'), ('mlt-re011', 'Roteador MULTILASER RE011'), ('intbrs-2100g', 'Roteador INTELBRAS W5-2100G'), ('intbrs-rf-1200', 'Roteador INTELBRAS RF-1200'), ('intbrs-rg-1200', 'Roteador INTELBRAS RG-1200'), ('intbrs-rf-301k', 'Roteador INTELBRAS RF-301K'), ('intbrs-rf-1200f', 'Roteador INTELBRAS RF-1200F'), ('intbrs-gf-1200', 'Roteador INTELBRAS GF-1200'), ('intbrs-rx-1500', 'Roteador INTELBRAS RX-1500'), ('intbrs-w4-300f', 'Roteador INTELBRAS W4-300F'), ('intbrs-iwr-3000n', 'Roteador INTELBRAS IWR-3000N'), ('intbrs-w6-1500', 'Roteador INTELBRAS W6-1500'), ('intbrs-wrn300', 'Roteador INTELBRAS WRN300'), ('intbrs-121ac', 'Roteador INTELBRAS 121AC'), ('intbrs-win240', 'Roteador INTELBRAS WIN240'), ('hwei-ax2s', 'Roteador HUAWEI AX2S'), ('hwei-ws7000', 'Roteador HUAWEI WS7000'), ('hwei-ws7001', 'Roteador HUAWEI WS7001'), ('hwei-ws3y18n', 'Roteador HUAWEI WS318N'), ('hwei-ac1300', 'Roteador HUAWEI AC1300'), ('hwei-ws7000', 'Roteador HUAWEI WS7000'), ('hwei-ws5200', 'Roteador HUAWEI WS5200'), ('hwei-ws7206', 'Roteador HUAWEI WS7206'), ('hwei-ws7100', 'Roteador HUAWEI WS7100'), ('dlnk-d846', 'Roteador D-LINK DIR-846'), ('dlnk-d615', 'Roteador D-LINK DIR-615'), ('dlnk-d610', 'Roteador D-LINK DIR-610'), ('dlnk-d842', 'Roteador D-LINK DIR-842'), ('dlnk-d853', 'Roteador D-LINK DIR-853'), ('dlnk-610n', 'Roteador D-LINK DIR-610N'), ('dlnk-n300', 'Roteador D-LINK DIR615 N300'), ('dlnk-2730e', 'Roteador D-LINK DSR-2730E'), ('dlnk-1360', 'Roteador D-LINK DIR-1360'), ('orcamento', 'Solicitou por Orçamento')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='mensagens_area_cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=25)),
                ('mensagem', models.TextField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='PlanoPainel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('caracteristica', models.TextField()),
                ('preco', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('bairro', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=100)),
                ('numero_casa', models.CharField(max_length=10)),
                ('senha_cadastro', models.CharField(max_length=100)),
            ],
        ),
    ]
