<h1 align="center">:file_cabinet: README.md</h1>

## :memo: Descrição
Projeto desenvolvido com intuito de desenvolver um template de notícias utilizando as tecnologias, Django, Python e Docker. O tema escolhido foi baseado em notícias do espaço com temas de nebulosa, planetas, galáxias e estrelas. 


## :books: Funcionalidades
* <b>Home</b>: Página inicial/index da da aplicação, onde mesmo sem login, usuário consegue visualizar, filtrar e buscar por notícias. 
* <b>Login</b>: Caso usuário já tenha login é necessário somente logar, caso contrário, clica em cadastro.
* <b>Cadastro</b>: Permite que usuário se cadastre. 
* <b>Logout</b>: Faz logout do usuário, bloqueando todas as funções de nova notícia. 
* <b>Nova Notícia</b>: Permite ao usuário cadastrar novas noticias, imagens e datas de postagem. 
* <b>Notícias</b>: Possuem titulo, fonte, noticia, foto e opção de edição e delete dos usuários logados.  

## :wrench: Tecnologias utilizadas
* Python
* Django
* AWS S3
* HTML, CSS

## :rocket: Rodando o projeto
Para rodar o repositório é necessário clonar o mesmo, e logo após dar o seguinte comando para iniciar utilizar container docker:

* Docker build
* Docker up -d

## :soon: Implementação futura
* Colocar as classes de permissão de editor e escritor de forma funcional;
* Trocar AWS S3 por Min.IO (Armazenamento de objetos de alto desempenho para IA e gratuito);
* Omissão do menu principal conforme permissão das classes;

## :handshake: Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="http://github.com/GabriellaVRS">
        <sub>
          <b>GabriellaVRS</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## :dart: Status do projeto
Postado!
