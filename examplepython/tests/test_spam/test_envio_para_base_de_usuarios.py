import pytest

from examplepython.spam.enviador_de_email import Enviador
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
    enviador = EnviadorMock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
    assert len(usuarios) == enviador.qte_emails_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qte_emails_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Victor', email='victorsanmorais@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
    assert enviador.parametros_de_envio == (
        'victorsanmorais@gmail.com',
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
