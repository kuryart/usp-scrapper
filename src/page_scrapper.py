from bs4 import BeautifulSoup
import requester

MAIN_URL = "https://uspdigital.usp.br/jupiterweb/"
URL = "https://uspdigital.usp.br/jupiterweb/listarGradeCurricular?codcg=59&codcur=59080&codhab=0&tipo=N18"

# Download the content in HTML format
def download_content(url, file_path):
    response = requester.make_request(url)
    with open("src/content/" + file_path, 'w', -1, "utf-8") as handler:
        handler.write(response.text)

def __main():
    # Get page
    page = requester.make_request(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Obtém todos os links
    links = soup.find_all("a", class_="link_gray")

    for link in links:
        link_url = link["href"]
        download_content(MAIN_URL + link_url, link_url + ".html")

__main()