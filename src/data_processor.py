from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# Nome da disciplina
def obterNome(soup: BeautifulSoup) -> str:
    nome = soup.find(string=lambda text : "Disciplina:" in text)

    print(nome + "\n"*2)
    return nome

# Obtém informações sobre a programa resumido
def obterProgramaResumido(soup: BeautifulSoup) -> str:
    titulo = soup.find(string=lambda text : "Programa Resumido" in text)
    pai = titulo.find_parent("tr")
    programa_resumido = pai.next_sibling.next_element.span.pre.text

    return programa_resumido

# Obtém informações sobre a programa
def obterPrograma(soup: BeautifulSoup) -> str:
    titulo = soup.find("b", string=lambda text : "Programa" in text and "Resumido" not in text and "Programação" not in text)
    pai = titulo.find_parent("tr")

    programa = pai.next_sibling.next_element.span.pre.text

    return programa

# Obtém informações sobre a bibliografia
def obterBibliografia(soup: BeautifulSoup) -> str:
    titulo = soup.find(string=lambda text : "Bibliografia" in text)
    pai = titulo.find_parent("table")
    bibliografia = pai.pre.text

    return bibliografia

# Obtém informações sobre a disciplina
def obterDisciplina(soup: BeautifulSoup) -> dict[str, str]:
    disciplina = {
        "nome": obterNome(soup),
        "programa_resumido": obterProgramaResumido(soup),
        "programa": obterPrograma(soup),
        "bibliografia": obterBibliografia(soup)
    }

    return disciplina

def __main():
    files = [f for f in listdir("src/content") if isfile(join("src/content", f))]
    str_result = "# Ciências da Computação" + "\n"*2

    for file in files:
        page = open("src/content/" + file, "r")
        soup = BeautifulSoup(page, "html.parser")
        disciplina = obterDisciplina(soup)

        str_result += "## " + disciplina["nome"] + "\n"*2
        str_result += "**Programa Resumido** " + "\n"*2
        str_result += disciplina["programa_resumido"] + "\n"*2
        str_result += "**Programa** " + "\n"*2
        str_result += disciplina["programa"] + "\n"*2
        str_result += "**Bibliografia** " + "\n"*2
        str_result += disciplina["bibliografia"] + "\n"*2

    with open("src/results/result2.md", "w") as file:
        file.write(str_result)

__main()