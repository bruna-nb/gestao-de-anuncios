from model.cliente import Cliente
from datetime import datetime

class Anuncio():
    """
    Classe de anúncios.

    Atributos
    ---------
    titulo : str
        Título do anúncio
    cliente : Cliente
        Cliente do anúncio, é um objeto da classe Cliente.
    data_de_inicio : str
        Data de ínicio do anúncio, no formato AAAA-MM-DD hh:mm:ss
    data_de_termino : str
        Data de término do anúncio, no formato AAAA-MM-DD hh:mm:ss
    investimento_diario : float
        Investimento diário no anúncio, em reais e centavos
    codigo : int
        Código de identificação gerado automaticamente. Utilizado como chave de
        acesso ao objeto.

    Métodos
    -------
    titulo()
        Retorna ou redefine título do anúncio
    cliente()
        Retorna ou redefine cliente
    data_de_inicio()
        Retorna ou redefine data de início do anúncio
    data_de_termino()
        Retorna ou redefine data de término do anúncio
    investimento_diario()
        Retorna ou redefine investimento diário no anúncio
    codigo()
        Retorna ou redefine código do anúncio
    """

    def __init__(self, titulo: str, cliente: Cliente, data_de_inicio,
                 data_de_termino, investimento_diario, codigo):
        """Inicia classe Anuncio

        Parâmetros
        ----------
        titulo : str
            Título do anúncio
        cliente : Cliente
            Cliente do anúncio, é um objeto da classe Cliente.
        data_de_inicio : str
            Data de início do anúncio
        data_de_termino : str
            Data de término do anúncio
        investimento_diario : float
            Investimento diário no anúncio, em reais e centavos
        codigo : str
            Código do anúncio
        """

        self.__titulo = titulo
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        self.__data_de_inicio = data_de_inicio
        self.__data_de_termino = data_de_termino
        self.__investimento_diario = investimento_diario
        self.__codigo = codigo

    @property
    def titulo(self):
        """Retorna ou altera o título do anúncio.

        Quando usado como getter, apenas retorna o título do anúncio.
        Quando usado como setter, aceita parâmetro de entrada `titulo`,
        que define o novo título.

        Parâmetros
        ----------
        titulo : str, opcional
            Novo título do anúncio

        Retorna
        -------
        titulo : str
            Retorna 
        """

        return self.__titulo

    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo
        return self.__titulo

    @property
    def cliente(self):
        """Retorna ou altera o cliente.

        Quando usado como getter, apenas retorna o cliente.
        Quando usado como setter, aceita parâmetro de entrada `cliente`,
        que redefine o cliente.

        Parâmetros
        ----------
        cliente : Cliente, opcional
            Novo cliente

        Retorna
        -------
        cliente : Cliente
            Cliente do anúncio, é um objeto da classe Cliente.
        """

        return self.__cliente

    @cliente.setter
    def cliente (self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        return self.__cliente

    @property
    def data_de_inicio(self):
        """Retorna ou altera a data de início.

        Quando usado como getter, apenas retorna a data.
        Quando usado como setter, aceita parâmetro de entrada
        `data_de_inicio`, que redefine a data.

        Parâmetros
        ----------
        data_de_inicio : str, opcional
            Nova data de início do anúncio

        Retorna
        -------
        data_de_inicio : str
            Data de início do anúncio
        """

        return self.__data_de_inicio
    
    @data_de_inicio.setter
    def data_de_inicio(self, data_de_inicio):
        self.__data_de_inicio = data_de_inicio
        return self.__data_de_inicio
    
    @property
    def data_de_termino(self):
        """Retorna ou altera a data de término.

        Quando usado como getter, apenas retorna a data.
        Quando usado como setter, aceita parâmetro de entrada
        `data_de_termino`, que redefine a data.

        Parâmetros
        ----------
        data_de_termino : str, opcional
            Nova data de término do anúncio

        Retorna
        -------
        data_de_termino : str
            Data de término do anúncio
        """

        return self.__data_de_termino
    
    @data_de_termino.setter
    def data_de_termino(self, data_de_termino):
        self.__data_de_termino = data_de_termino
        return self.__data_de_termino
    
    @property
    def investimento_diario(self):
        """Retorna ou altera o investimento diário no anúncio.

        Quando usado como getter, apenas retorna o valor do investimento.
        Quando usado como setter, aceita parâmetro de entrada 
        `investimento_diario`, que redefine o investimento diário no anúncio.

        Parâmetros
        ----------
        investimento_diario : float, opcional
            Novo valor de investimento diário

        Retorna
        -------
        investimento_diario : float
            Valor do investimento diário
        """

        return self.__investimento_diario
    
    @investimento_diario.setter
    def investimento_diario(self,investimento_diario):
        self.__investimento_diario = investimento_diario
        return self.__investimento_diario
    
    @property
    def codigo(self):
        """Retorna ou altera o código do anúncio

        Quando usado como getter, apenas retorna o código do anúncio.
        Quando usado como setter, aceita parâmetro de entrada `codigo`,
        que redefine o código do anúncio.

        Parâmetros
        ----------
        codigo : str, opcional
            Novo código do anúncio

        Retorna
        -------
        codigo : str
            Código do anúncio
        """

        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        return self.__codigo