# IA - Sistema de Conforto Térmico (Regras)

## Descrição
Sistema simbólico baseado em regras para classificar o conforto térmico
com base em temperatura e umidade. Projeto desenvolvido para a disciplina
de Inteligência Artificial — Aula 3.

---

## Estrutura do Projeto
IA-Sistema-Conforto-Termico/
├── data/
│ └── sample_input.csv # dataset de exemplo
├── outputs/ # resultados gerados (CSV e gráficos)
├── src/
│ ├── init.py
│ ├── rules.py # definição das regras e classificador
│ ├── data.py # utilitários para carregar/salvar dados
│ ├── run.py # script principal
│ └── visualize.py # geração de gráficos
├── .gitignore
├── requirements.txt
└── README.md

---

## Regras de Classificação

| Classificação                  | Condição                                      | Prioridade |
|-------------------------------|-----------------------------------------------|------------|
| Muito Frio                    | temperatura ≤ 5°C                             | 100        |
| Muito Quente                  | temperatura ≥ 35°C                            | 100        |
| Muito Seco                    | umidade ≤ 30%                                 | 90         |
| Muito Úmido                   | umidade ≥ 80%                                 | 90         |
| Precisa de Sol para Conforto  | 10°C ≤ temperatura < 20°C e 30% < umidade < 80% | 50       |
| Confortável                   | 20°C ≤ temperatura ≤ 25°C e 30% < umidade < 80% | 40       |
| Precisa de Vento para Conforto| 25°C < temperatura < 35°C e 30% < umidade < 80% | 30       |
| Confortável (Zona Adaptativa) | 10°C ≤ temperatura ≤ 32°C e 30% < umidade < 80% | 10       |
| Indefinido                    | nenhuma regra satisfeita                      | —          |

---

## Como Usar

### 1. Clonar o repositório
```bash
git clone https://github.com/RhuanrSantos/IA-Sistema-Conforto-Termico.git
cd IA-Sistema-Conforto-Termico