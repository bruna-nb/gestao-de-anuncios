from model.dao import DAO
from model.cliente import Cliente

class ClienteDAO(DAO):
    """
    Classe usada para persistencia de objetos da classe cliente

    Métodos
    -------
    add(cliente)
        Adiciona um objeto cliente à base de dados.
    get(key)
        Retorna um cliente a partir do seu código.
    remove(key)
        Remove um cliente a partir do seu código.
    update()
        Atualiza a base de dados
    """

    def __init__(self):
        """Inicia classe ClienteDAO e cria o arquivo cliente.pkl."""
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        """Adiciona um novo cliente à base de dados.

        Parâmetros
        ----------
        cliente : Cliente
            objeto da classe Cliente
        """

        if((cliente is not None) and isinstance(cliente, Cliente)):
            super().add(cliente.codigo, cliente)

    def get(self, key:int):
        """Encontra um cliente pelo seu código.

        Parâmetros
        ----------
        key : int
            Chave de identificação do objeto (usualmente o código).

        Retorna
        -------
        cliente : Cliente
            Objeto cliente que possui como código a chave informada.
        """

        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        """Remove um objeto da classe cliente utilizando o código.

        Parâmetros
        ----------
        key : int
            Chave de identificação do objeto (usualmente o código).

        """

        if(isinstance(key, int)):
            return super().remove(key)
    
    def update(self):
        """Explicação do método."""
        super().update_file()