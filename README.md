# 🌍 REST Countries API Explorer (Python)

Um script em Python desenvolvido para consumir e interagir com a [REST Countries API (v3.1)](https://restcountries.com/). 

Este projeto tem fins educacionais e demonstra conceitos fundamentais de integração com APIs externas, tratamento de dados em JSON, e manipulação de dicionários/listas no Python.

## ✨ Funcionalidades

O script possui funções modulares que permitem:
- **Buscar todos os países:** Faz uma requisição à API para trazer a base completa de países do mundo.
- **Contagem de países:** Retorna o número total de países registrados na base de dados.
- **Listagem de nomes:** Extrai e exibe o nome comum (`common name`) de todos os países.
- **Busca específica (População):** Permite pesquisar um país pelo seu nome em inglês (ex: "brazil") e retorna a sua população total atualizada.

## 🛠️ Tecnologias Utilizadas

- **[Python 3.x](https://www.python.org/):** Linguagem principal.
- **[Requests](https://pypi.org/project/requests/):** Biblioteca para realizar as requisições HTTP.
- **JSON (built-in):** Biblioteca nativa do Python para fazer o parsing dos dados recebidos.

## ⚙️ Estrutura do Código

O código foi refatorado utilizando boas práticas de separação de responsabilidades (Clean Code):
- `requisicao(url)`: Lida exclusivamente com a chamada HTTP e retorna o texto da resposta.
- `parsing(texto)`: Responsável por transformar a string da resposta em um dicionário Python (JSON).
- Funções de regra de negócio: `contagem_de_paises`, `listar_paises` e `mostrar_populacao`.

## 🚀 Como executar o projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Você também precisará instalar a biblioteca `requests`.

Abra o seu terminal e rode o comando:
```bash
pip install requests
