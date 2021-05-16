from controller.controlador_cliente import ControladorCliente
from view.tela_anuncio import TelaAnuncio
from model.anuncio_dao import AnuncioDAO
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import DataInvalidaException
from model.anuncio import Anuncio

class ControladorAnuncio():
    def __init__(self, tela_anuncio: TelaAnuncio,
                controlador_cliente: ControladorCliente):
        self.__tela_anuncio = tela_anuncio
        self.__controlador_cliente = controlador_cliente
        self.__anuncio_dao = AnuncioDAO()
        if len(self.__anuncio_dao.get_all()) == 0:
            self.__gera_codigo = 500
        else:
            self.__gera_codigo = 500
            for anuncio in self.__anuncio_dao.get_all():
                if anuncio.codigo > self.__gera_codigo:
                    self.__gera_codigo = anuncio.codigo
            self.__gera_codigo += 1
    
    def inserir_novo_anuncio(self):
        if len(self.__controlador_cliente.listar_todos_clientes()) == 0:
            self.__tela_anuncio.mensagem('Cadastre um cliente antes de '+
                'cadastrar um anúncio.')
        else:
            novo_anuncio = True
            while True:
                dados_anuncio = self.__tela_anuncio.obter_dados(\
                    self.__controlador_cliente.listar_todos_clientes())
                if dados_anuncio is None:
                    break
                else:
                    try:
                        if (dados_anuncio['titulo'] == '' or \
                            dados_anuncio['cliente'] == '' or \
                                dados_anuncio['data_inicio'] == '' or \
                                    dados_anuncio['data_fim'] == '' or \
                                        dados_anuncio['investimento'] == ''):
                                        novo_anuncio = False
                                        raise CampoEmBrancoException
                        else:
                            try:
                                if self.verifica_datas(\
                                    dados_anuncio['data_inicio'],\
                                        dados_anuncio['data_fim']) is False:
                                        novo_anuncio = False
                                        raise DataInvalidaException
                                else:                            
                                    try:
                                        float(dados_anuncio['investimento'])
                                    except ValueError:
                                        novo_anuncio = False
                                        self.__tela_anuncio.mensagem('O ' + 
                                        'investimento diário deve ser um número.')
                                if dados_anuncio is not None:
                                    break
                            except DataInvalidaException as mensagem:
                                self.__tela_anuncio.mensagem(mensagem)
                    except CampoEmBrancoException as mensagem:
                        self.__tela_anuncio.mensagem(mensagem)
            if dados_anuncio is not None and novo_anuncio:
                codigo_cliente = int(dados_anuncio['cliente'].split(' ')[0])
                cliente = self.__controlador_cliente.encontrar_cliente_por_codigo(codigo_cliente)
                self.__anuncio_dao.add(Anuncio(dados_anuncio['titulo'], cliente,\
                    dados_anuncio['data_inicio'], dados_anuncio['data_fim'],\
                        dados_anuncio['investimento'], self.__gera_codigo))
                self.__gera_codigo +=1
    
    def verifica_datas(self,data_inicio,data_fim):
        verificacao = True
        ano_data_inicio = str(data_inicio).split('-')[0]
        ano_data_fim = str(data_fim).split('-')[0]
        if ano_data_inicio > ano_data_fim:
            verificacao = False
        elif ano_data_inicio == ano_data_fim:
            mes_data_inicio = str(data_inicio).split('-')[1]
            mes_data_fim = str(data_fim).split('-')[1]
            if mes_data_inicio > mes_data_fim:
                verificacao = False
            elif mes_data_inicio == mes_data_fim:
                dia_data_inicio = str(str(data_inicio).split('-')[2]).split(' ')[0]
                dia_data_fim = str(str(data_fim).split('-')[2]).split(' ')[0]
                if dia_data_inicio > dia_data_fim:
                    verificacao = False
        return verificacao
    
    def encontra_anuncio_por_codigo(self,codigo):
        return self.__anuncio_dao.get(codigo)
    
    def listar_todos_os_anuncios(self):
        lista = []
        for anuncio in self.__anuncio_dao.get_all():
            lista.append({'titulo': anuncio.titulo, 'cliente': anuncio.cliente.nome,
            'data_de_inicio': anuncio.data_de_inicio,
            'data_de_termino': anuncio.data_de_termino,
            'investimento': anuncio.investimento_diario,
            'codigo': anuncio.codigo, 'codigo_cliente': anuncio.cliente.codigo})
        return lista
    
    def mostrar_todos_os_anuncios(self):
        self.__tela_anuncio.listar_anuncios(self.listar_todos_os_anuncios())

    


                            


    