from model.dao import DAO
from model.anuncio import Anuncio

class AnuncioDAO(DAO):
    """
    Classe que faz a persistência de dados da classe Anuncio, criando e
    atualizando o arquivo anuncios.pkl.

    Métodos
    -------
    add(anuncio)
        Adiciona um objeto anuncio à base de dados.
    get(key)
        Encontra um objeto da classe anuncio por meio do código.
    remove(key)
        Remove um objeto da classe anuncio utilizando o código.
    update()
        Atualiza a base de dados.
    """

    def __init__(self):
        """Inicia classe AnuncioDAO e cria o arquivo anuncios.pkl"""
        super().__init__('anuncios.pkl')

    def add(self, anuncio: Anuncio):
        """Adiciona um novo objeto da classe Anuncio na base de dados.

        Parâmetros
        ----------
        anuncio : Anuncio
            Objeto da classe Anuncio.
        """

        if((anuncio is not None) and isinstance(anuncio, Anuncio)):
            super().add(anuncio.codigo, anuncio)

    def get(self, key:int):
        """Encontra um objeto na base de dados por meio da chave informada.

        Parâmetros
        ----------
        key : int
            Chave de identificação do objeto (usualmente o código).

        Retorna
        -------
        anuncio: Anuncio
            Retorna objeto da classe anuncio que contém o código informado.
        """

        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        """Remove um objeto da classe anuncio utilizando o código.

        Parâmetros
        ----------
        key : int
            Chave de identificação do objeto (usualmente o código).

        """

        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        """Atualiza a base de dados."""
        super().update_file()