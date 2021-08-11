from examplepython.spam.enviador_de_email import Enviador
from examplepython.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'victorsanmorais@gmail.com',
        'teste enviador spam',
        "IT'S WORKING!"
    )
