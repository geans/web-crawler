import json
import requests

cities=['AGUA BRANCA', 'ANADIA', 'ARAPIRACA', 'ATALAIA', 'BARRA DE SANTO ANTONIO', 'BARRA DE SAO MIGUEL', 'BATALHA', 'BELEM', 'BELO MONTE', 'BOCA DA MATA', 'BRANQUINHA', 'CACIMBINHAS', 'CAJUEIRO', 'CAMPESTRE', 'CAMPO ALEGRE', 'CAMPO GRANDE', 'CANAPI', 'CAPELA', 'CARNEIROS', 'CHA PRETA', 'COITE DO NOIA', 'COLONIA LEOPOLDINA', 'COQUEIRO SECO', 'CORURIPE', 'CRAIBAS', 'DELMIRO GOUVEIA', 'DOIS RIACHOS', 'ESTRELA DE ALAGOAS', 'FEIRA GRANDE', 'FELIZ DESERTO', 'FLEXEIRAS', 'GIRAU DO PONCIANO', 'IBATEGUARA', 'IGACI', 'IGREJA NOVA', 'INHAPI', 'JACARE DOS HOMENS', 'JACUIPE', 'JAPARATINGA', 'JARAMATAIA', 'JEQUIA DA PRAIA', 'JOAQUIM GOMES', 'JUNDIA', 'JUNQUEIRO', 'LAGOA DA CANOA', 'LIMOEIRO DE ANADIA', 'MACEIO', 'MAJOR ISIDORO', 'MAR VERMELHO', 'MARAGOGI', 'MARAVILHA', 'MARECHAL DEODORO', 'MARIBONDO', 'MATA GRANDE', 'MATRIZ DE CAMARAGIBE', 'MESSIAS', 'MINADOR DO NEGRAO', 'MONTEIROPOLIS', 'MURICI', 'NOVO LINO', "OLHO D'AGUA DAS FLORES", "OLHO D'AGUA DO CASADO", "OLHO D'AGUA GRANDE", 'OLIVENCA', 'OURO BRANCO', 'PALESTINA', 'PALMEIRA DOS INDIOS', 'PAO DE ACUCAR', 'PARICONHA', 'PARIPUEIRA', 'PASSO DE CAMARAGIBE', 'PAULO JACINTO', 'PENEDO', 'PIACABUCU', 'PILAR', 'PINDOBA', 'PIRANHAS', 'POCO DAS TRINCHEIRAS', 'PORTO CALVO', 'PORTO DE PEDRAS', 'PORTO REAL DO COLEGIO', 'QUEBRANGULO', 'RIO LARGO', 'ROTEIRO', 'SANTA LUZIA DO NORTE', 'SANTANA DO IPANEMA', 'SANTANA DO MUNDAU', 'SAO BRAS', 'SAO JOSE DA LAJE', 'SAO JOSE DA TAPERA', 'SAO LUIS DO QUITUNDE', 'SAO MIGUEL DOS CAMPOS', 'SAO MIGUEL DOS MILAGRES', 'SAO SEBASTIAO', 'SATUBA', 'SENADOR RUI PALMEIRA', "TANQUE D'ARCA", 'TAQUARANA', 'TEOTONIO VILELA', 'TRAIPU', 'UNIAO DOS PALMARES', 'VICOSA']

url_builder = 'https://nominatim.openstreetmap.org/?addressdetails=1&format=json&limit=1&polygon_geojson=1&q={} Alagoas Brasil'.format

class City:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def to_json(self):
        return json.dumps({'city': self.name, 'points': self.points})

    def to_str(self):
        return f'"{self.name}","{self.points}"'

err_file  = open('erro.csv', 'w')
df_file   = open('points_cities.csv', 'w')
json_file = open('points_cities.json', 'w')
err_file.write('address,response\n')
df_file.write('city,points\n')
json_file.write('[\n')

total = len(cities)
i = 0

for city_addr in cities:
    url = url_builder(city_addr)
    r = requests.get(url)
    if r.status_code != 200:
        err_file.write(f'{city_addr},\n')
        continue
    j = r.json()
    addr = j[0]['address']
    if addr['state'] != 'Alagoas' and addr['country'] != Brasil:
        err_file.write(f'"{city_addr}","{addr}"\n')
        continue
    points = j[0]['geojson']['coordinates'][0]
    c = City(city_addr, points)
    df_file.write(c.to_str()+'\n')
    json_file.write(f'{c.to_json()},\n')
    
    i += 1
    print(i*100/total, i, c.name)
json_file.write(']')

err_file.close()
df_file.close()
json_file.close()
