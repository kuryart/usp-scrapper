import requests
import re
from bs4 import BeautifulSoup

MAIN_URL = "https://uspdigital.usp.br/jupiterweb/"
URL = "https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=59&codcur=59080&codhab=0&tipo=N18"

def obterNome(soup: BeautifulSoup) -> str:
    nome = soup.find(string=lambda text : "Disciplina:" in text)

    print(nome + "\n"*2)
    return nome

def obterProgramaResumido(soup: BeautifulSoup) -> str:
    titulo = soup.find(string=lambda text : "Programa Resumido" in text)
    pai = titulo.find_parent("tr")
    programa_resumido = pai.next_sibling.next_element.span.pre.text

    return programa_resumido

def obterPrograma(soup: BeautifulSoup) -> str:
    titulo = soup.find("b", string=lambda text : "Programa" in text and "Resumido" not in text and "Programação" not in text)
    pai = titulo.find_parent("tr")

    print(pai.next_sibling.next_element)

    programa = pai.next_sibling.next_element.span.pre.text

    return programa

def obterBibliografia(soup: BeautifulSoup) -> str:
    titulo = soup.find(string=lambda text : "Bibliografia" in text)
    pai = titulo.find_parent("table")
    bibliografia = pai.pre.text

    return bibliografia

# Resultado final
str_result = ""

# Get page
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Obtém todos os links
links = soup.find_all("a", class_="link_gray")

for link in links:
    # "Clica" no link e obtém os dados
    link_url = link["href"]
    page = requests.get(MAIN_URL + link_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtém informações sobre a disciplina
    disciplina = {
        "nome": obterNome(soup),
        "programa-resumido": obterProgramaResumido(soup),
        "programa": obterPrograma(soup),
        "bibliografia": obterBibliografia(soup)
    }

    str_result += str(disciplina) + "\n"*2 + "=== | === | === | ===" + "\n"*2

with open("src/results/result.txt", "w") as file:
    file.write(str_result)