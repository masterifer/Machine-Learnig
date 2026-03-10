import argparse
import os
from src.data import load_csv, save_csv, sample_dataframe
from src.rules import classify_row, DEFAULT_RULES


def main():
    """
    Script principal para classificar conforto térmico.

    Uso:
        python -m src.run --sample
        python -m src.run -i data/sample_input.csv -o outputs/result.csv
    """
    parser = argparse.ArgumentParser(
        description='Classificador de Conforto Térmico baseado em Regras'
    )
    parser.add_argument(
        '--input', '-i',
        type=str,
        default=None,
        help='Caminho para o CSV de entrada (colunas: temperatura, umidade)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='outputs/classified.csv',
        help='Caminho para o CSV de saída (padrão: outputs/classified.csv)'
    )
    parser.add_argument(
        '--sample',
        action='store_true',
        help='Usar dataset de exemplo interno para teste'
    )

    args = parser.parse_args()

    if args.sample:
        print("Usando dataset de exemplo...")
        df = sample_dataframe()
    else:
        if args.input is None:
            parser.error("Forneça --input/-i com o caminho do CSV ou use --sample para dados de exemplo.")
        print(f"Carregando dados de: {args.input}")
        df = load_csv(args.input)

    print("Aplicando regras de classificação...")
    df['classificacao'] = df.apply(
        lambda row: classify_row(row, DEFAULT_RULES), axis=1
    )

    print("\nResultado da Classificação:")
    print("-" * 45)
    print(df.to_string(index=True))
    print("-" * 45)

    save_csv(df, args.output)
    print(f"\nProcessamento concluído! {len(df)} registros classificados.")


if __name__ == '__main__':
    main()
