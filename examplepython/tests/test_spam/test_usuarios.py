from examplepython.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Victor')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Victor'), Usuario(nome='Victor 2')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
