import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

response = requests.get(url)
if response.status_code == 200:
    print(f'sukses response = {response.status_code}')
    # print(f'contentnya adalah {response.text}')
    soup = BeautifulSoup(response.text, features="html.parser")
    print(f'hasil pemanggilan pada situs {url}')
    print(f'judul : {soup.title.string}')
else:
        print(f'wohooo ada kesalahan requests {response.status_code}')


