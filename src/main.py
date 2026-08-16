from conexao import conectar
from extracao import ler_excel
from transformacao import transformar_dados
from carga import carregar_dados


def main():

    df_bruto = ler_excel()

    if df_bruto is None:
        return

    df_tratado = transformar_dados(df_bruto)

    conn = conectar()

    if conn:

        sucesso = carregar_dados(conn, df_tratado)

        conn.close()

        if sucesso:
            print("ETL finalizado com sucesso!")
        else:
            print("ETL finalizado com erro!")


if __name__ == "__main__":
    main()