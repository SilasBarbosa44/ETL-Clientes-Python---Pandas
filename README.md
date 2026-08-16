<<<<<<< HEAD
#  ETL - Base de Clientes com Python e MySQL

Pipeline de ETL para extrair dados de uma planilha Excel, tratar e carregar em um banco de dados MySQL. Projeto feito para simular um fluxo real de tratamento de dados.

## O que o projeto faz

Extrai dados de clientes de um arquivo .xlsx, aplica limpeza e validações com Pandas e carrega tudo na tabela `clientes` do MySQL. 

Durante a transformação são removidas duplicatas, padronizados textos, convertidos tipos e aplicadas regras de negócio como salario >= 0 e campos obrigatórios. A carga tem tratamento de erro com rollback para garantir integridade.

## Tecnologias utilizadas

Python, Pandas, MySQL Connector, MySQL 8.0

## Como rodar o projeto

Clone o repositório e entre na pasta. 
Crie um ambiente virtual e instale as dependências: `pip install pandas mysql-connector-python openpyxl`

Crie o banco e a tabela executando o script em `sql/create_table.sql` no MySQL.

Ajuste as credenciais de conexão no arquivo `src/etl_clientes.py`.

Execute com: `python src/etl_clientes.py`

Se der tudo certo vai aparecer: `ETL finalizado com sucesso`

## Estrutura de pastas
ETL Clientes/
│
├── data/
│   └── etl_clientes.xlsx
│
├── sql/
│   └── database.sql
│
├── src/
│   ├── __pycache__/
│   ├── carga.py
│   ├── conexao.py
│   ├── extracao.py
│   ├── main.py
│   └── transformacao.py
│
├── .gitignore
├── README.md
└── requirements.txt


## Script da tabela

Use o arquivo em `sql/create_table.sql`:
```sql
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    salario DECIMAL(10,2),
    data_cadastro DATE,
    total_compras DECIMAL(10,2),
    categoria_cliente VARCHAR(50)
);

## Aprendizados
Pratiquei manipulação de dados com Pandas, conexão Python com MySQL, validação e limpeza de dados e boas práticas de ETL como tratamento de erro e commit/rollback


Feito por **Silas Barbosa da Silva**
![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
