from examplepython.spam.modelos import Conexao, Sessao

import pytest


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


@pytest.fixture
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Victor')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Victor'), Usuario(nome='Victor 2')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
