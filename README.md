<h1 align="center">
    <img alt="Agility" src="images/cartola-fc-logo.png" height="100px" />
    <br>Challenge CartolaFC<br/>
    Python | Numpy | Flask
</h1>

<p align="center">

<a href="https://packagist.org/packages/laravel/framework"><img src="https://poser.pugx.org/laravel/framework/license.svg" alt="License"></a>

</p>

## Sobre

Neste projeto foi desenvolvida uma API simples para retornar os fatos vigentes. Esta API está hospedada em [https://flaskapicartola.herokuapp.com](https://flaskapicartola.herokuapp.com).

Desenvolvido usando Python, [Flask](https://flask.palletsprojects.com/en/2.0.x/) e a biblioteca [NumPy](https://numpy.org/), biblioteca de código aberto destinada a realizar operações em arrays multidimensionais.

## Como executar a aplicação?

git clone https://github.com/slooock/flask.git

cd flask

docker build -t apiflask .

docker run -p 5000:5000 -v $(pwd):/src apiflask

Feito isso o projeto estará rodando na porta 5000.

## Endpoints

Para realizar o processo de filtro dos fatos vigentes foi desenvolvido dois endpoints.

### process/default -> GET

Retorna os fatos vigentes dos fatos fornecido na documentação.

```
    facts = [
            ('gabriel', 'endereço', 'av rio branco, 109', True),
            ('joão', 'endereço', 'rua alice, 10', True),
            ('joão', 'endereço', 'rua bob, 88', True),
            ('joão', 'telefone', '234-5678', True),
            ('joão', 'telefone', '91234-5555', True),
            ('joão', 'telefone', '234-5678', False),
            ('gabriel', 'telefone', '98888-1111', True),
            ('gabriel', 'telefone', '56789-1010', True)
        ]
```

Exemplo de execução utilizando a API hospedada em [https://flaskapicartola.herokuapp.com](https://flaskapicartola.herokuapp.com)

```
curl --location --request GET 'https://flaskapicartola.herokuapp.com/process/default'
```

### process -> POST

Recebe um JSON dos fatos e retorna os fatos vigentes.

Exemplo:

```
    {
        "facts":[
            ["gabriel", "endereço", "av rio branco, 109", "True"],
            ["joão", "endereço", "rua alice, 10", "True"],
            ["joão", "endereço", "rua bob, 88", "True"],
            ["joão", "telefone", "234-5678", "True"],
            ["joão", "telefone", "91234-5555", "True"],
            ["joão", "telefone", "234-5678", "False"],
            ["gabriel", "telefone", "98888-1111", "True"],
            ["gabriel", "telefone", "56789-1010", "True"]
        ]
    }
```

Exemplo de execução utilizando a API hospedada em [https://flaskapicartola.herokuapp.com](https://flaskapicartola.herokuapp.com)

```
    curl --location --request POST 'https://flaskapicartola.herokuapp.com/process' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "facts":[
            ["gabriel", "endereço", "av rio branco, 109", "True"],
            ["joão", "endereço", "rua alice, 10", "True"],
            ["joão", "endereço", "rua bob, 88", "True"],
            ["joão", "telefone", "234-5678", "True"],
            ["joão", "telefone", "91234-5555", "True"],
            ["joão", "telefone", "234-5678", "False"],
            ["gabriel", "telefone", "98888-1111", "True"],
            ["gabriel", "telefone", "56789-1010", "True"]
        ]
    }'
```

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
