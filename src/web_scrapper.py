import requests
import re
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent
import data_processor

MAIN_URL = "https://uspdigital.usp.br/jupiterweb/"
URL = "https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=59&codcur=59080&codhab=0&tipo=N18"

def __main():
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
            "nome": data_processor.obterNome(soup),
            "programa-resumido": data_processor.obterProgramaResumido(soup),
            "programa": data_processor.obterPrograma(soup),
            "bibliografia": data_processor.obterBibliografia(soup)
        }

        str_result = ""

        str_result += str(disciplina) + "\n"*2 + "=== | === | === | ===" + "\n"*2

    with open("src/results/result2.txt", "w") as file:
        file.write(str_result)

__main()