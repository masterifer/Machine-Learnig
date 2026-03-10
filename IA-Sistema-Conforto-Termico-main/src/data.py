import pandas as pd
import os


def load_csv(path: str) -> pd.DataFrame:
    """
    Carrega um CSV e valida se as colunas obrigatórias existem.

    Args:
        path: caminho para o arquivo CSV

    Returns:
        DataFrame com os dados carregados

    Raises:
        ValueError: se alguma coluna obrigatória estiver ausente
        FileNotFoundError: se o arquivo não existir
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    df = pd.read_csv(path)

    colunas_obrigatorias = ['temperatura', 'umidade']
    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente no CSV: '{coluna}'")

    return df


def save_csv(df: pd.DataFrame, path: str):
    """
    Salva um DataFrame em CSV.

    Args:
        df: DataFrame a salvar
        path: caminho de destino
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False, encoding='utf-8-sig')
    print(f"Arquivo salvo em: {os.path.abspath(path)}")


def sample_dataframe() -> pd.DataFrame:
    """
    Retorna um DataFrame de exemplo para testes.

    Returns:
        DataFrame com dados de temperatura e umidade
    """
    return pd.DataFrame({
        'temperatura': [3, 5, 15, 22, 23, 25, 28, 29, 38, 40, 18],
        'umidade':     [50, 50, 50, 45, 50, 85, 85, 50, 60, 60, 20],
    })
