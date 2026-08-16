import pandas as pd


def transformar_dados(df):

    df = df.drop_duplicates()

    df["nome"] = df["nome"].str.strip()
    df["email"] = df["email"].str.strip().str.lower()
    df["cidade"] = df["cidade"].str.strip().str.title()
    df["estado"] = df["estado"].str.strip().str.upper()
    df["categoria_cliente"] = df["categoria_cliente"].str.strip().str.title()

    df["id_cliente"] = pd.to_numeric(
        df["id_cliente"],
        errors="coerce"
    )

    df["data_cadastro"] = pd.to_datetime(
        df["data_cadastro"],
        errors="coerce"
    )

    df["salario"] = pd.to_numeric(
        df["salario"],
        errors="coerce"
    )

    df["total_compras"] = pd.to_numeric(
        df["total_compras"],
        errors="coerce"
    )

    df["total_compras"] = df["total_compras"].fillna(0).round(2)

    df = df[df["salario"] >= 0]

    df = df.dropna(
        subset=["nome", "email", "id_cliente", "data_cadastro"]
    )

    df["id_cliente"] = df["id_cliente"].astype(int)

    return df