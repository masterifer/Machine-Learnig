import matplotlib.pyplot as plt
import pandas as pd
from src.rules import DEFAULT_RULES, classify_row


COLORS = {
    'Muito Frio':                    'blue',
    'Muito Quente':                  'red',
    'Muito Seco':                    'orange',
    'Muito Úmido':                   'green',
    'Precisa de Sol para Conforto':  'yellow',
    'Confortável':                   'cyan',
    'Precisa de Vento para Conforto':'magenta',
    'Confortável (Zona Adaptativa)': 'lightgreen',
    'Indefinido':                    'gray',
}


def plot_dataset(df: pd.DataFrame, rules=None, save_path: str = None):
    """
    Gera um gráfico de dispersão com os pontos classificados por cor.

    Args:
        df: DataFrame com colunas 'temperatura' e 'umidade'
        rules: lista de regras (usa DEFAULT_RULES se None)
        save_path: se fornecido, salva o gráfico no caminho indicado
    """
    rules = rules or DEFAULT_RULES

    labels = df.apply(lambda row: classify_row(row, rules), axis=1)

    plt.figure(figsize=(10, 7))

    for lbl in labels.unique():
        subset = df[labels == lbl]
        plt.scatter(
            subset['temperatura'],
            subset['umidade'],
            label=lbl,
            color=COLORS.get(lbl, 'gray'),
            s=80,
            alpha=0.85,
            edgecolors='black',
            linewidths=0.5
        )

    plt.axvline(x=5,  color='blue',   linestyle='--', linewidth=0.8, alpha=0.5, label='Limite Muito Frio (5°C)')
    plt.axvline(x=35, color='red',    linestyle='--', linewidth=0.8, alpha=0.5, label='Limite Muito Quente (35°C)')
    plt.axhline(y=30, color='orange', linestyle='--', linewidth=0.8, alpha=0.5, label='Limite Muito Seco (30%)')
    plt.axhline(y=80, color='green',  linestyle='--', linewidth=0.8, alpha=0.5, label='Limite Muito Úmido (80%)')

    plt.xlabel('Temperatura (°C)', fontsize=12)
    plt.ylabel('Umidade (%)', fontsize=12)
    plt.title('Classificação de Conforto Térmico', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico salvo em: {save_path}")

    plt.show()


if __name__ == '__main__':
    df = pd.DataFrame({
        'temperatura': [3, 5, 15, 22, 23, 25, 28, 29, 38, 40, 18],
        'umidade':     [50, 50, 50, 45, 50, 85, 85, 50, 60, 60, 20],
    })
    plot_dataset(df, save_path='outputs/grafico_conforto.png')
