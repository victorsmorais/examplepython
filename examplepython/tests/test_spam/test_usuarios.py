def test_salvar_usuario():
    conexao = Conexao()
    sessao = Sessao()
    usuario = Usuario(nome='Victor')
    sessao.salvar(usuario)
    assert isinstance(usuario_id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listarar_usuario():
    conexao = Conexao()
    sessao = Sessao()
    usuarios = [Usuario(nome='Victor'), Usuario(nome='Victor 2')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
