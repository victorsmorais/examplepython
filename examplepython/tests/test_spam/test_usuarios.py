from examplepython.spam.modelos import Conexao, Sessao


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Victor')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = Sessao()
    usuarios = [Usuario(nome='Victor'), Usuario(nome='Victor 2')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
