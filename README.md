# CNAB Transactions

A aplicação consiste em parsear arquivo de texto(CNAB) e salvar suas informações (transações financeiras) em uma base de dados a critério do candidato.
Esta aplicação foi feita em python, utilizando do Django como framework.

# Instruções de configuração:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
source venv/Scripts/activate
```

3. Instale todas as dependências:

```
pip install -r requirements.txt
```

4. Rode as migrações:

```
python manage.py migrate
```

# Rotas da aplicação:

```
POST: /api/form/
```

Endpoint onde o usuário deverá preencher o formulário com o envio de um arquivo CNAB.

<hr></hr>

## Documentação do CNAB

![alt text](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/documentacao_cnab.png)

## Documentação sobre os tipos das transações

![alt text](https://conteudo-kenzie-fullstack.vercel.app/modulo_6/desafio_backend/img/tipo_transacao.png)

<hr></hr>
<br></br>

```
GET: /api/transactions/
```

Endpoint onde o usuário poderá visualizar uma lista das operações importadas por lojas, além de poder visualizar o saldo em conta totalizando todas as transações.

<hr></hr>

```json
[
  {
    "id": 1,
    "type": "3",
    "date": "01/03/2019",
    "value": 142,
    "cpf": "096.206.760-17",
    "card": "4753****3153",
    "hour": "15:34:53",
    "store_owner": "JOÃO MACEDO",
    "store_name": "BAR DO JOÃO"
  },
  {
    "id": 2,
    "type": "5",
    "date": "01/03/2019",
    "value": 132,
    "cpf": "556.418.150-63",
    "card": "3123****7687",
    "hour": "14:56:07",
    "store_owner": "MARIA JOSEFINA",
    "store_name": "LOJA DO Ó - MATRIZ"
  },
  {
    "id": 3,
    "type": "3",
    "date": "01/03/2019",
    "value": 122,
    "cpf": "845.152.540-73",
    "card": "6777****1313",
    "hour": "17:27:12",
    "store_owner": "MARCOS PEREIRA",
    "store_name": "MERCADO DA AVENIDA"
  },
  {
    "total_value": "R$ 252,00"
  }
]
```

<hr></hr>
