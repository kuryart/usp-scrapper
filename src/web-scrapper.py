import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://uspdigital.usp.br/jupiterweb/"
URL = "https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=59&codcur=59080&codhab=0&tipo=N18"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

str_result = ""

links = soup.find_all("a", class_="link_gray")

for link in links:
    link_url = link["href"]

    page = requests.get(MAIN_URL + link_url)

    soup = BeautifulSoup(page.content, "html.parser")

    disciplinas = soup.find_all("span", class_="txt_arial_10pt_black")

    str_result += str(disciplinas) + "\n"*2 + "=== | === | === | ===" + "\n"*2

with open("src/results/result.txt", "w") as file:
    file.write(str_result)