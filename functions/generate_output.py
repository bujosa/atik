import pandas as pd
from functions.get_crypto_symbol import get_crypto_symbol

def generate_output():
    df = pd.read_csv('./data/dataset.csv')
    unique_crypto_names = df['crypto_name'].unique()

    df2 = pd.DataFrame(columns=['name', 'symbol'])

    for crypto_name in unique_crypto_names:
        symbol = get_crypto_symbol(crypto_name)
        df2.loc[len(df2)] = [crypto_name, symbol]
        
    df2.to_csv('./data/output.csv', index=False)

