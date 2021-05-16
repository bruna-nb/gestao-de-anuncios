from model.cliente import Cliente
from model.cliente_dao import ClienteDAO
from view.tela_cliente import TelaCliente
from controller.excecoes import CampoEmBrancoException

class ControladorCliente():
    def __init__(self, tela_cliente: TelaCliente):
        self.__tela_cliente = tela_cliente
        self.__cliente_dao = ClienteDAO()
        if len(self.__cliente_dao.get_all()) == 0:
            self.__gera_codigo = 100
        else:
            self.__gera_codigo = 100
            for cliente in self.__cliente_dao.get_all():
                if cliente.codigo > self.__gera_codigo:
                    self.__gera_codigo = cliente.codigo
            self.__gera_codigo += 1
    
    def inserir_cliente(self):
        while True:
            dados_cliente = self.__tela_cliente.inserir_dados()
            if dados_cliente is None:
                break
            else:
                nome = dados_cliente['nome']
                try:
                    if nome == '':
                        raise CampoEmBrancoException
                    else:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_cliente.mensagem(mensagem)
        if dados_cliente is not None and nome != '':
            if dados_cliente['telefone'] == '':
                telefone = 'nao cadastrado'
            else:
                telefone = dados_cliente['telefone']
            if dados_cliente['email'] == '':
                email = 'nao cadastrado'
            else:
                email = dados_cliente['email']
            self.__cliente_dao.add(Cliente(nome, telefone, email,\
                self.__gera_codigo))
            self.__gera_codigo += 1
    
    def listar_todos_clientes(self):
        lista = []
        for cliente in self.__cliente_dao.get_all():
            lista.append({'nome': cliente.nome, 'telefone': cliente.telefone,
            'email': cliente.email,'codigo': cliente.codigo})
        return lista
    
    def encontrar_cliente_por_codigo(self, codigo):
        return self.__cliente_dao.get(codigo)
        
        
        

            
