# Portfólio de Disign Digital #

> |Dono do portfólio|Email|Apelido|
> |----|-----|-----|
> |**Gabriel Souza Bicho Nunes**|gabriel0gsbn@gmail.com|***Zeropirata***|

---

## Pastas do GitHub ##

* Doc.
    > Pasta contendo o Wireframe, onde foi a base para o inicio do protótipo do Website

* Src
    > Pasta que amarzena todos os codigos e arquivos necessarios do portifólio.
  * Static.
    * Pasta ***CSS***
      * Arquivos ***.css*** do portifolio
    * Pasta ***Imagen***
      * Contem as ***imagens*** do portifolio
    * Pasta ***Bootstrap***
      * Contem os arquivos do framework ***Bootstrap [CSS & JavaScript]***
  * template.
    * Contem os código-fonte ***.html*** do website.
  
---
## Coisas feitas na segunda entrega ##
> Utilização do ***Bootstrap 5***

> Manutenção do portifolio, excluindo páginas e códigos obsoletos
> * Junção do ***Index*** com o ***Sobre mim***
> * ***global.css*** para ***style.css*** com o ***Bootstrap 5***
> * Redesign da interface para a utilização do ***Bootstrap 5***
---
## Framework Utilizado ##

<a href="https://getbootstrap.com/">![Youtube](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)</a>

## Coisas feitas na Terceira entrega ##

> ### utilização da micro framework Flask ###
> 
> ### Implementação do Jinja em paginas que tem a mesma quantidade de colunas ###
> 
> ### Implementação no Heroku ###

----
## Como fazer a aplicação rodar com flask ##
Tendo a ferramenta Git e o Python instalados em seu computador:
- Abra o Prompt de Comando no caminho de um novo diretório e copie o seguinte comando para clonar o nosso repositório:

```
git clone https://github.com/ZeroPirata/portifolio
```
- Dentro da pasta root do projeto, crie um Ambiente Virtual com o seguite comando:
```
python3 -m venv venv
```
ou caso tenha o python3 já instalado
```
python -m venv venv
```
(Obs.: caso você utilize um sistema operacional diferente do Windows, verifique comandos alternativos neste [Link](https://docs.python.org/pt-br/3/library/venv.html) .)
- Isso criará o diretório  ```venv```. Agora ative o Ambiente Virtual com o comando:
```
venv\Scripts\activate
```
- Você deverá ver o ambiente virtual ativado antes do caminho do seu diretório, assim:
``` (venv) C:\...```
- Agora instale as dependências do projeto:
``` 
pip install -r requirements.txt
```
- Agora certifique-se que está no diretório ```src``` e para executar a aplicação, execute o comando:
```
flask run
```
- A aplicação estará rodando por padrão na porta :5000, caso já tenha uma aplicação rodando nesta porta, certifique-se de selecionar uma porta livre na hora de rodar a aplicação:
``` 
flask run -p 9000
```
- Vá até o caminho indicado http://127.0.0.1:5000/ ou http://127.0.0.1:9000/ e navegue na aplicação.
---
|Demonstração do WebSite|Link|Numero da Entrega|
| :----: |:---:|:---:|
| ![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)|<a href="https://www.youtube.com/watch?v=JCPDhqW1_6o">Click Aqui</a>|Entrega Nº 1|
| ![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)|<a href="https://www.youtube.com/watch?v=G9SlitMFbJo">Click Aqui</a>|Entrega Nº 2|
| ![GitHubPages](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)|<a href="https://zeropirata.github.io/portifolio/src/template/index.html">Click Aqui</a>|Teste do Portifolio|