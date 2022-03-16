<h1 align="center">
    <img alt="Agility" src="images/cartola-fc-logo.png" height="100px" />
    <br>Challenge CartolaFC<br/>
    Python | Numpy | JSON |Docker
</h1>

<p align="center">

<a href="https://packagist.org/packages/laravel/framework"><img src="https://poser.pugx.org/laravel/framework/license.svg" alt="License"></a>

</p>

## Sobre

Desenvolvido usando Python3 e a biblioteca [NumPy](https://numpy.org/), biblioteca de código aberto destinada a realizar operações em arrays multidimensionais.

## Como executar a aplicação?

git clone https://github.com/slooock/process.git

cd process

docker build -t process .

docker run -v $(pwd)/src:/src process

### OBS

O usuário deverá ter o [Docker](https://www.docker.com/) instalado na máquina, sendo assim o Dockerfile fica responsável pela execução e instalação das dependências necessárias.

### Entendendo a execução

A pasta src possui 3 arquivos, (facts.json, schema.json, process.py) que são responsáveis pela execução do processo. E como resultado é criado um novo arquivo chamado response.json. Os arquivos facts.json e schema.json podem ser personalizados da maneira mais convincente a fim de realizar novos testes.

#### process.py

Este é o arquivo principal onde é definida a função exigida. Além disso este aquivo é responsável por abrir o arquivo facts.json e schema.json e processar as informações com os dados fornecido nos arquivos.

Foi desenvolvido desta maneira para facilitar o processo de teste, basta entrar com o json em facts e em schema que o processamento acontecerá de maneira dinâmica.

#### facts.json

Este é o nosso arquivo de entrada que possui os fatos.

#### schema.json

Este é o nosso arquivo de entrada que possui os o schema com as regras definidas.

Em ambos (facts.json e schema.json) estão com as entradas padrão fornecidas como exemplo no exercício. O processo pode ser executado em um outro projeto, para isso basta importar processFacts(facts, schema), em seu projeto. Lembrando que na função processFacts, os parâmetros facts e schema são opcionais, caso não sejam passados será considerado o valor default (fornecido na documentação).
