CREATE DATABASE etl_clientes;
USE etl_clientes;

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(150),
    cidade VARCHAR(100),
    estado CHAR(2),
    salario DECIMAL(10,2),
    data_cadastro DATE,
    total_compras DECIMAL(12,2),
    categoria_cliente VARCHAR(20)
); 