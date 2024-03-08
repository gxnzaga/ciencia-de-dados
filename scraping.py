from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate

html = urlopen("https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2023")
bs = BeautifulSoup(html, 'html.parser')

dados_jogadores = {}

table_data = [['Nome', 'Apelido', 'Gols']] # create a list

lines = bs.find_all('tr') # find all rows (tr) in table

for i, line in enumerate(lines[45:], 1):  # Start from index 1 to ignore the header and other tr inserted into the site
    cols = line.find_all(['th', 'td'])  # find all rows (td and tr) in line

    if len(cols) >= 4: # check if the cols list has the expected number of elements

        nome = cols[2].text.strip()
        apelido = cols[3].text.strip()
        gols = cols[1].text.strip()

        jogador_info = [nome, apelido, gols]
        dados_jogadores[f'Jogador_{i}'] = jogador_info
        table_data.append(jogador_info)

print(tabulate(table_data, headers='firstrow', tablefmt='grid'))


