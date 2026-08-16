def carregar_dados(conn, df):

    if not conn:
        print("Conexão com banco de dados indisponível.")
        return False

    cursor = conn.cursor()

    sql = """
        INSERT INTO clientes (
            id_cliente,
            nome,
            email,
            cidade,
            estado,
            salario,
            data_cadastro,
            total_compras,
            categoria_cliente
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:

        for _, row in df.iterrows():

            valores = (
                int(row["id_cliente"]),
                row["nome"],
                row["email"],
                row["cidade"],
                row["estado"],
                float(row["salario"]),
                row["data_cadastro"].date(),
                float(row["total_compras"]),
                row["categoria_cliente"]
            )

            cursor.execute(sql, valores)

        conn.commit()

        return True

    except Exception as e:

        conn.rollback()

        print(f"Erro ao inserir dados: {e}")

        return False

    finally:
        cursor.close()