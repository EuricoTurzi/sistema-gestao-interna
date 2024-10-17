# Generated by Django 5.1.1 on 2024-10-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0015_alter_estoque_antenista_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque_antenista',
            name='nome',
            field=models.CharField(choices=[('RODRIGO SILVA', 'RODRIGO SILVA'), ('FELIPPE CAMELO', 'FELIPPE CAMELO'), ('FILIPPE CAMELO', 'FILIPPE CAMELO'), ('JOSÉ ANTONIO', 'JOSÉ ANTONIO'), ('CESAR RODRIGO - SPO', 'CESAR RODRIGO - SPO'), ('LUCIO', 'LUCIO'), ('FELIPE MACEDO - SPO', 'FELIPE MACEDO - SPO'), ('RAFAEL ALVES - SPO', 'RAFAEL ALVES - SPO'), ('ANDERSON COSTA / L', 'ANDERSON COSTA / L'), ('YURI NETTO', 'YURI NETTO'), ('HERCULES / FILIPE', 'HERCULES / FILIPE'), ('ALEXANDRE', 'ALEXANDRE'), ('AILTON', 'AILTON'), ('SATURNINO', 'SATURNINO'), ('CLEBSON ARANDU - SPO', 'CLEBSON ARANDU - SPO'), ('TENORIO', 'TENORIO'), ('WILSON JOSE', 'WILSON JOSE'), ('WESLEY RODRIGO', 'WESLEY RODRIGO'), ('WESLEY RODRIGO - SPO', 'WESLEY RODRIGO - SPO'), ('ANGELO/AGATHA', 'ANGELO/AGATHA'), ('STEVERSON ROGGER', 'STEVERSON ROGGER'), ('IGOR BARBOSA', 'IGOR BARBOSA'), ('CAIQUE GONÇALVES', 'CAIQUE GONÇALVES'), ('GIOVAN MENDES', 'GIOVAN MENDES'), ('RONALDO/SILVA', 'RONALDO/SILVA'), ('CARDOSO/PAULA', 'CARDOSO/PAULA'), ('BORGES / ALMEIDA - JONAS', 'BORGES / ALMEIDA - JONAS'), ('DINAYDER/CLEITON - JONAS', 'DINAYDER/CLEITON - JONAS'), ('IVAN/LEANDRO - ALEX', 'IVAN/LEANDRO - ALEX'), ('WILSON JOSE - SPO', 'WILSON JOSE - SPO'), ('VINICIUS SUHE', 'VINICIUS SUHE'), ('AURELIO ANDRADE - RJ', 'AURELIO ANDRADE - RJ'), ('THAISY/JOAO PEDRO', 'THAISY/JOAO PEDRO'), ('PAULO VICENTE/LUCIA - JONAS', 'PAULO VICENTE/LUCIA - JONAS'), ('ANDERSON NOGUEIRA', 'ANDERSON NOGUEIRA'), ('THIAGO MATHEUS - SPO', 'THIAGO MATHEUS - SPO'), ('SIMEI SANTANA - SPO', 'SIMEI SANTANA - SPO'), ('FLORIANO FERREIRA - SPO', 'FLORIANO FERREIRA - SPO'), ('AURELIO', 'AURELIO'), ('RAPHAEL/LIMA', 'RAPHAEL/LIMA'), ('RIBEIRO/DUTRA', 'RIBEIRO/DUTRA'), ('HUGO/MOTTA', 'HUGO/MOTTA'), ('ANDRADE/LEONARDO', 'ANDRADE/LEONARDO'), ('ANDERSON/MARCIO', 'ANDERSON/MARCIO'), ('SILVIO ROMERO', 'SILVIO ROMERO'), ('ALEX SILVA', 'ALEX SILVA'), ('GABRIEL QUILANTE', 'GABRIEL QUILANTE'), ('VITOR ROGERIO', 'VITOR ROGERIO'), ('MARCIO JUNIOR', 'MARCIO JUNIOR'), ('TADEU', 'TADEU'), ('LEANDRO FERREIRA - RJ', 'LEANDRO FERREIRA - RJ'), ('NASCIMENTO/AMERSON', 'NASCIMENTO/AMERSON'), ('IZABEL/SAMPAIO', 'IZABEL/SAMPAIO'), ('ANDRE/TELES', 'ANDRE/TELES'), ('ALLAN/CRISTINA', 'ALLAN/CRISTINA'), ('CARLOS MAIA/FELIPE SOUSA', 'CARLOS MAIA/FELIPE SOUSA'), ('FELIPE SOUZA', 'FELIPE SOUZA'), ('ROBSON RAMIRO', 'ROBSON RAMIRO'), ('WASHINGTON FERNANDES - RJ', 'WASHINGTON FERNANDES - RJ'), ('CARLOS CARVALHO/DIOGO SENA', 'CARLOS CARVALHO/DIOGO SENA'), ('ROGERIO/ISMAEL', 'ROGERIO/ISMAEL'), ('JANDERSO FERNANDES', 'JANDERSO FERNANDES'), ('JOAO MARCOS', 'JOAO MARCOS'), ('ADRIANO GONÇALVES', 'ADRIANO GONÇALVES'), ('COUTINHO/SANTOS', 'COUTINHO/SANTOS'), ('NUNES/CRYSOSTOMO', 'NUNES/CRYSOSTOMO'), ('ESTEVAO/ULYSSES', 'ESTEVAO/ULYSSES'), ('ALCIDES', 'ALCIDES'), ('EZEQUIEL', 'EZEQUIEL'), ('NILDO', 'NILDO'), ('ALEX', 'ALEX'), ('ANDERSON', 'ANDERSON'), ('ANTONIEQUE', 'ANTONIEQUE'), ('OSNI', 'OSNI'), ('ELTON', 'ELTON'), ('NEY', 'NEY'), ('ANDRÉ', 'ANDRÉ'), ('RILDO', 'RILDO'), ('WELLINGTHON', 'WELLINGTHON'), ('GERSON WALACE', 'GERSON WALACE'), ('JUSTINO', 'JUSTINO'), ('ANTONIO', 'ANTONIO'), ('FRANCISCO', 'FRANCISCO'), ('OSMAN', 'OSMAN'), ('TONHARA', 'TONHARA'), ('EMERSON', 'EMERSON'), ('MARCELO', 'MARCELO'), ('JEFFERSON', 'JEFFERSON'), ('GUILHERME', 'GUILHERME'), ('MARCIO', 'MARCIO'), ('SAMPAIO', 'SAMPAIO'), ('DIOGO', 'DIOGO'), ('WESLEY', 'WESLEY'), ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'), ('ERIK', 'ERIK'), ('LUCAS CARVALHO', 'LUCAS CARVALHO'), ('RODRIGO', 'RODRIGO'), ('PITTA', 'PITTA'), ('JUSTO', 'JUSTO'), ('PAULO HENRIQUE', 'PAULO HENRIQUE'), ('EDUARDO', 'EDUARDO'), ('YURI', 'YURI'), ('RAFAEL', 'RAFAEL'), ('MARLON', 'MARLON'), ('MALLONE ROCHA DA SILVA', 'MALLONE ROCHA DA SILVA'), ('Ian Carlos Severino', 'Ian Carlos Severino')], max_length=50),
        ),
        migrations.AlterField(
            model_name='requisicoes',
            name='antenista',
            field=models.CharField(blank=True, choices=[('RODRIGO SILVA', 'RODRIGO SILVA'), ('FELIPPE CAMELO', 'FELIPPE CAMELO'), ('FILIPPE CAMELO', 'FILIPPE CAMELO'), ('JOSÉ ANTONIO', 'JOSÉ ANTONIO'), ('CESAR RODRIGO - SPO', 'CESAR RODRIGO - SPO'), ('LUCIO', 'LUCIO'), ('FELIPE MACEDO - SPO', 'FELIPE MACEDO - SPO'), ('RAFAEL ALVES - SPO', 'RAFAEL ALVES - SPO'), ('ANDERSON COSTA / L', 'ANDERSON COSTA / L'), ('YURI NETTO', 'YURI NETTO'), ('HERCULES / FILIPE', 'HERCULES / FILIPE'), ('ALEXANDRE', 'ALEXANDRE'), ('AILTON', 'AILTON'), ('SATURNINO', 'SATURNINO'), ('CLEBSON ARANDU - SPO', 'CLEBSON ARANDU - SPO'), ('TENORIO', 'TENORIO'), ('WILSON JOSE', 'WILSON JOSE'), ('WESLEY RODRIGO', 'WESLEY RODRIGO'), ('WESLEY RODRIGO - SPO', 'WESLEY RODRIGO - SPO'), ('ANGELO/AGATHA', 'ANGELO/AGATHA'), ('STEVERSON ROGGER', 'STEVERSON ROGGER'), ('IGOR BARBOSA', 'IGOR BARBOSA'), ('CAIQUE GONÇALVES', 'CAIQUE GONÇALVES'), ('GIOVAN MENDES', 'GIOVAN MENDES'), ('RONALDO/SILVA', 'RONALDO/SILVA'), ('CARDOSO/PAULA', 'CARDOSO/PAULA'), ('BORGES / ALMEIDA - JONAS', 'BORGES / ALMEIDA - JONAS'), ('DINAYDER/CLEITON - JONAS', 'DINAYDER/CLEITON - JONAS'), ('IVAN/LEANDRO - ALEX', 'IVAN/LEANDRO - ALEX'), ('WILSON JOSE - SPO', 'WILSON JOSE - SPO'), ('VINICIUS SUHE', 'VINICIUS SUHE'), ('AURELIO ANDRADE - RJ', 'AURELIO ANDRADE - RJ'), ('THAISY/JOAO PEDRO', 'THAISY/JOAO PEDRO'), ('PAULO VICENTE/LUCIA - JONAS', 'PAULO VICENTE/LUCIA - JONAS'), ('ANDERSON NOGUEIRA', 'ANDERSON NOGUEIRA'), ('THIAGO MATHEUS - SPO', 'THIAGO MATHEUS - SPO'), ('SIMEI SANTANA - SPO', 'SIMEI SANTANA - SPO'), ('FLORIANO FERREIRA - SPO', 'FLORIANO FERREIRA - SPO'), ('AURELIO', 'AURELIO'), ('RAPHAEL/LIMA', 'RAPHAEL/LIMA'), ('RIBEIRO/DUTRA', 'RIBEIRO/DUTRA'), ('HUGO/MOTTA', 'HUGO/MOTTA'), ('ANDRADE/LEONARDO', 'ANDRADE/LEONARDO'), ('ANDERSON/MARCIO', 'ANDERSON/MARCIO'), ('SILVIO ROMERO', 'SILVIO ROMERO'), ('ALEX SILVA', 'ALEX SILVA'), ('GABRIEL QUILANTE', 'GABRIEL QUILANTE'), ('VITOR ROGERIO', 'VITOR ROGERIO'), ('MARCIO JUNIOR', 'MARCIO JUNIOR'), ('TADEU', 'TADEU'), ('LEANDRO FERREIRA - RJ', 'LEANDRO FERREIRA - RJ'), ('NASCIMENTO/AMERSON', 'NASCIMENTO/AMERSON'), ('IZABEL/SAMPAIO', 'IZABEL/SAMPAIO'), ('ANDRE/TELES', 'ANDRE/TELES'), ('ALLAN/CRISTINA', 'ALLAN/CRISTINA'), ('CARLOS MAIA/FELIPE SOUSA', 'CARLOS MAIA/FELIPE SOUSA'), ('FELIPE SOUZA', 'FELIPE SOUZA'), ('ROBSON RAMIRO', 'ROBSON RAMIRO'), ('WASHINGTON FERNANDES - RJ', 'WASHINGTON FERNANDES - RJ'), ('CARLOS CARVALHO/DIOGO SENA', 'CARLOS CARVALHO/DIOGO SENA'), ('ROGERIO/ISMAEL', 'ROGERIO/ISMAEL'), ('JANDERSO FERNANDES', 'JANDERSO FERNANDES'), ('JOAO MARCOS', 'JOAO MARCOS'), ('ADRIANO GONÇALVES', 'ADRIANO GONÇALVES'), ('COUTINHO/SANTOS', 'COUTINHO/SANTOS'), ('NUNES/CRYSOSTOMO', 'NUNES/CRYSOSTOMO'), ('ESTEVAO/ULYSSES', 'ESTEVAO/ULYSSES'), ('ALCIDES', 'ALCIDES'), ('EZEQUIEL', 'EZEQUIEL'), ('NILDO', 'NILDO'), ('ALEX', 'ALEX'), ('ANDERSON', 'ANDERSON'), ('ANTONIEQUE', 'ANTONIEQUE'), ('OSNI', 'OSNI'), ('ELTON', 'ELTON'), ('NEY', 'NEY'), ('ANDRÉ', 'ANDRÉ'), ('RILDO', 'RILDO'), ('WELLINGTHON', 'WELLINGTHON'), ('GERSON WALACE', 'GERSON WALACE'), ('JUSTINO', 'JUSTINO'), ('ANTONIO', 'ANTONIO'), ('FRANCISCO', 'FRANCISCO'), ('OSMAN', 'OSMAN'), ('TONHARA', 'TONHARA'), ('EMERSON', 'EMERSON'), ('MARCELO', 'MARCELO'), ('JEFFERSON', 'JEFFERSON'), ('GUILHERME', 'GUILHERME'), ('MARCIO', 'MARCIO'), ('SAMPAIO', 'SAMPAIO'), ('DIOGO', 'DIOGO'), ('WESLEY', 'WESLEY'), ('EVERALDO / SAMUEL', 'EVERALDO / SAMUEL'), ('ERIK', 'ERIK'), ('LUCAS CARVALHO', 'LUCAS CARVALHO'), ('RODRIGO', 'RODRIGO'), ('PITTA', 'PITTA'), ('JUSTO', 'JUSTO'), ('PAULO HENRIQUE', 'PAULO HENRIQUE'), ('EDUARDO', 'EDUARDO'), ('YURI', 'YURI'), ('RAFAEL', 'RAFAEL'), ('MARLON', 'MARLON'), ('MALLONE ROCHA DA SILVA', 'MALLONE ROCHA DA SILVA'), ('Ian Carlos Severino', 'Ian Carlos Severino')], max_length=50, null=True),
        ),
    ]
