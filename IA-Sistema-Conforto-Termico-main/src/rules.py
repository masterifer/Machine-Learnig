from dataclasses import dataclass
from typing import Callable, Dict, List
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


@dataclass
class Rule:
    """
    Representa uma regra de classificação.
    
    Atributos:
        name: nome da regra
        condition: função que recebe uma linha e retorna True/False
        label: rótulo atribuído se a condição for verdadeira
        priority: prioridade da regra (maior = avaliada primeiro)
    """
    name: str
    condition: Callable[[Dict], bool]
    label: str
    priority: int = 0


def classify_row(row: Dict, rules: List[Rule], default: str = 'Indefinido') -> str:
    """
    Classifica uma linha de dados com base nas regras fornecidas.
    Regras são avaliadas em ordem de prioridade (maior primeiro).
    
    Args:
        row: dicionário ou Series com chaves 'temperatura' e 'umidade'
        rules: lista de regras a aplicar
        default: rótulo retornado se nenhuma regra for satisfeita
    
    Returns:
        string com o rótulo de classificação
    """
    sorted_rules = sorted(rules, key=lambda r: r.priority, reverse=True)
    for r in sorted_rules:
        try:
            if r.condition(row):
                logger.debug("Regra aplicada: %s -> %s", r.name, r.label)
                return r.label
        except Exception as e:
            logger.warning("Erro avaliando regra '%s': %s", r.name, e)
    return default


DEFAULT_RULES: List[Rule] = [

    Rule(
        name='Muito Frio',
        condition=lambda r: float(r['temperatura']) <= 5,
        label='Muito Frio',
        priority=100
    ),
    Rule(
        name='Muito Quente',
        condition=lambda r: float(r['temperatura']) >= 35,
        label='Muito Quente',
        priority=100
    ),

    Rule(
        name='Muito Seco',
        condition=lambda r: float(r['umidade']) <= 30,
        label='Muito Seco',
        priority=90
    ),
    Rule(
        name='Muito Úmido',
        condition=lambda r: float(r['umidade']) >= 80,
        label='Muito Úmido',
        priority=90
    ),

    Rule(
        name='Precisa de Sol',
        condition=lambda r: 10 <= float(r['temperatura']) < 20 and 30 < float(r['umidade']) < 80,
        label='Precisa de Sol para Conforto',
        priority=50
    ),
    Rule(
        name='Confortável',
        condition=lambda r: 20 <= float(r['temperatura']) <= 25 and 30 < float(r['umidade']) < 80,
        label='Confortável',
        priority=40
    ),
    Rule(
        name='Precisa de Vento',
        condition=lambda r: 25 < float(r['temperatura']) < 35 and 30 < float(r['umidade']) < 80,
        label='Precisa de Vento para Conforto',
        priority=30
    ),

    Rule(
        name='Zona Adaptativa',
        condition=lambda r: 10 <= float(r['temperatura']) <= 32 and 30 < float(r['umidade']) < 80,
        label='Confortável (Zona Adaptativa)',
        priority=10
    ),
]
