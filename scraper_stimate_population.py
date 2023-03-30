import requests
import lxml.html

'''
Scraper for stimate population of cities of Alagoas state in Brazil from IBGE's site. And save it to csv file.
'''

cities=['AGUA BRANCA', 'ANADIA', 'ARAPIRACA', 'ATALAIA', 'BARRA DE SANTO ANTONIO', 'BARRA DE SAO MIGUEL', 'BATALHA', 'BELEM', 'BELO MONTE', 'BOCA DA MATA', 'BRANQUINHA', 'CACIMBINHAS', 'CAJUEIRO', 'CAMPESTRE', 'CAMPO ALEGRE', 'CAMPO GRANDE', 'CANAPI', 'CAPELA', 'CARNEIROS', 'CHA PRETA', 'COITE DO NOIA', 'COLONIA LEOPOLDINA', 'COQUEIRO SECO', 'CORURIPE', 'CRAIBAS', 'DELMIRO GOUVEIA', 'DOIS RIACHOS', 'ESTRELA DE ALAGOAS', 'FEIRA GRANDE', 'FELIZ DESERTO', 'FLEXEIRAS', 'GIRAU DO PONCIANO', 'IBATEGUARA', 'IGACI', 'IGREJA NOVA', 'INHAPI', 'JACARE DOS HOMENS', 'JACUIPE', 'JAPARATINGA', 'JARAMATAIA', 'JEQUIA DA PRAIA', 'JOAQUIM GOMES', 'JUNDIA', 'JUNQUEIRO', 'LAGOA DA CANOA', 'LIMOEIRO DE ANADIA', 'MACEIO', 'MAJOR ISIDORO', 'MAR VERMELHO', 'MARAGOGI', 'MARAVILHA', 'MARECHAL DEODORO', 'MARIBONDO', 'MATA GRANDE', 'MATRIZ DE CAMARAGIBE', 'MESSIAS', 'MINADOR DO NEGRAO', 'MONTEIROPOLIS', 'MURICI', 'NOVO LINO', "OLHO D'AGUA DAS FLORES", "OLHO D'AGUA DO CASADO", "OLHO D'AGUA GRANDE", 'OLIVENCA', 'OURO BRANCO', 'PALESTINA', 'PALMEIRA DOS INDIOS', 'PAO DE ACUCAR', 'PARICONHA', 'PARIPUEIRA', 'PASSO DE CAMARAGIBE', 'PAULO JACINTO', 'PENEDO', 'PIACABUCU', 'PILAR', 'PINDOBA', 'PIRANHAS', 'POCO DAS TRINCHEIRAS', 'PORTO CALVO', 'PORTO DE PEDRAS', 'PORTO REAL DO COLEGIO', 'QUEBRANGULO', 'RIO LARGO', 'ROTEIRO', 'SANTA LUZIA DO NORTE', 'SANTANA DO IPANEMA', 'SANTANA DO MUNDAU', 'SAO BRAS', 'SAO JOSE DA LAJE', 'SAO JOSE DA TAPERA', 'SAO LUIS DO QUITUNDE', 'SAO MIGUEL DOS CAMPOS', 'SAO MIGUEL DOS MILAGRES', 'SAO SEBASTIAO', 'SATUBA', 'SENADOR RUI PALMEIRA', "TANQUE D'ARCA", 'TAQUARANA', 'TEOTONIO VILELA', 'TRAIPU', 'UNIAO DOS PALMARES', 'VICOSA']

def get_html(city):
    c = city.replace("'","").lower().split(' ')
    c = '-'.join(c)
    url = f'https://www.ibge.gov.br/cidades-e-estados/al/{c}.html'
    # print('Consulta para:', url)
    return requests.get(url)

def scrap_population(response):
    htmlDocument = lxml.html.fromstring(response.text)
    p=htmlDocument.xpath('/html/body/main/section/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/div/p')
    return p[0].text_content().split(' ')[:1][0].replace('.','')

f = open('stimate_population.csv', 'w')
f.write('city,population\n')
i = 1
for city in cities:
    response = get_html(city)
    population = scrap_population(response)
    f.write(f'{city},{population}\n')
    print(f'[{i:3}]', city)
    i+=1
f.close()
