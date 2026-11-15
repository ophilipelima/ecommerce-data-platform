from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/raw")

for file in DATA_PATH.glob("*.csv"):

    df = pd.read_csv(file)

    print(f"\nArquivo: {file.name}")

    print(f"Quantidade de registros: {len(df)}")

    print(f"Quantidade de colunas: {len(df.columns)}")

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nValores nulos:")
    print(df.isnull().sum())

    print("\nRegistros duplicados:")
    print(df.duplicated().sum())

    print("-" * 50)