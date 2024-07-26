import requests
from fake_useragent import UserAgent
from time import sleep

def make_request(url):
    user_agent = UserAgent()
    header = {"User-Agent": str(user_agent.chrome)}

    response = None

    while response is None:
        try:
            response = requests.get(url, headers=header, timeout=30)
            return response
        except requests.ConnectionError as e:
            print('Connection error occurred', e)
            sleep(1.5)
            continue
        except requests.Timeout as e:
            print('Timeout error - request took too long', e)
            sleep(1.5)
            continue
        except requests.RequestException as e:
            print('General error', e)
            sleep(1.5)
            continue
        except KeyboardInterrupt:
            print('The program has been canceled')