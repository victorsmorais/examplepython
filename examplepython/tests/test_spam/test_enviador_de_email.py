import pytest

from examplepython.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['victorsanmorais@gmail.com', 'victorsanmorais@icloud.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'victor.morais@graduacao.ie.ufrj.br',
        'teste do enviador de e-mails',
        'Se você recebeu esta mensagem, então o enviador está funcionando.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'Victor']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'victor.morais@graduacao.ie.ufrj.br',
            'teste do enviador de e-mails',
            'Se você recebeu esta mensagem, então o enviador está funcionando.'
        )
