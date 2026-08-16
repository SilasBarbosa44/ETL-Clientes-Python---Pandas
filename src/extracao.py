import pandas as pd


def ler_excel():
    try:
        df = pd.read_excel("data/etl_clientes.xlsx")

        print("Planilha carregada com sucesso!")

        return df

    except Exception as e:
        print(f"Erro ao carregar planilha: {e}")
        return None