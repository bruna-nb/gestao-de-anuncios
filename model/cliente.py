class Cliente():
    """
    Classe usada para definir clientes

    (Explicação mais detalhada...)

    Atributos
    ---------
    nome : str
        Nome do cliente
    telefone : str
        Telefone do cliente
    email : str
        E-mail do cliente
    codigo : int
        Código do cliente

    Métodos
    -------
    nome()
        Retorna ou altera o nome do cliente
    telefone()
        Retorna ou altera o telefone do cliente
    email()
        Retorna ou altera o e-mail do cliente
    codigo()
        Retorna ou altera o código do cliente
    """

    def __init__(self, nome: str, telefone, email, codigo: int):
        """Inicia classe Cliente

        Parâmetros
        ----------
        nome : str
            Nome do cliente
        telefone : str
            Telefone do cliente
        email : str
            E-mail do cliente
        codigo : int
            Código do cliente
        """

        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__codigo = codigo
    
    @property
    def nome(self):
        """Retorna ou altera o nome do cliente

        Quando usado como getter, apenas retorna o nome do cliente.
        Quando usado como setter, aceita parâmetro de entrada `nome`,
        que redefine o nome do cliente.

        Parâmetros
        ----------
        nome : str, opcional
            Novo nome do cliente

        Retorna
        -------
        nome : str
            Nome do cliente
        """

        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        return self.__nome

    @property
    def telefone(self):
        """Retorna ou altera o telefone do cliente

        Quando usado como getter, apenas retorna o telefone do cliente.
        Quando usado como setter, aceita parâmetro de entrada 
        `telefone`, que redefine o telefone do cliente.

        Parâmetros
        ----------
        telefone : str, opcional
            Novo telefone do cliente

        Retorna
        -------
        telefone : str
            Telefone do cliente
        """

        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        return self.__telefone

    @property
    def email(self):
        """Retorna ou altera o e-mail do cliente

        Quando usado como getter, apenas retorna o e-mail do cliente.
        Quando usado como setter, aceita parâmetro de entrada `email`,
        que redefine o e-mail do cliente.

        Parâmetros
        ----------
        email : str, opcional
            Novo e-mail do cliente

        Retorna
        -------
        email : str
            E-mail do cliente
        """

        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
        return self.__email

    @property
    def codigo(self):
        """Retorna ou altera o código do cliente

        Quando usado como getter, apenas retorna o código do cliente.
        Quando usado como setter, aceita parâmetro de entrada
        `codigo`, que redefine o código do cliente.

        Parâmetros
        ----------
        codigo : int, opcional
            Novo código do cliente

        Retorna
        -------
        codigo : int
            Código do cliente
        """
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
