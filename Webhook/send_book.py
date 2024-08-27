import requests
import json

def send_book(title, author, year):
    url = "http://localhost:5000/"
    headers = {"Content-Type": "application/json"}
    payload = {
        "title": title,
        "author": author,
        "year": year
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("Resposta do servidor:", response.json())
    else:
        print("Erro:", response.status_code, response.text)

def remove_book(title):
    url = 'http://localhost:5000'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "action": "remove",
        "title": title
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Sucesso:", response.json().get("message"))
    elif response.status_code == 404:
        print("Erro:", response.json().get("message"))
    else:
        print("Erro:", response.json().get("message"))

if __name__ == "__main__":
    book_title = input("Digite o título do livro a ser removido: ")
    remove_book(book_title)
