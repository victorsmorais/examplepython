from unittest.mock import Mock

import pytest

from examplepython.spam.main import EnviadorDeSpam
from examplepython.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Victor', email='victorsanmorais@gmail.com'),
            Usuario(nome='Victor 2', email='victorsanmorais@gmail.com')
        ],
        [
            Usuario(nome='Victor', email='victorsanmorais@gmail.com')
        ]

    ]
)

def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Victor', email='victorsanmorais@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
    enviador.enviar.asser_called_once_with(
        'victorsanmorais@gmail.com',
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
