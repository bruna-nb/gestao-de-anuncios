from controller.controlador_anuncio import ControladorAnuncio
from view.tela_anuncio import TelaAnuncio
from controller.controlador_cliente import ControladorCliente
from view.tela_cliente import TelaCliente
from view.tela_sistema import TelaSistema
from controller.excecoes import CampoEmBrancoException
from controller.excecoes import DataInvalidaException
from controller.calculadora import calcula_totais
from controller.excecoes import FiltroInvalidoException
import datetime


class ControladorSistema():
    def __init__(self, tela_sistema: TelaSistema):
        self.__tela_sistema = tela_sistema
        self.__controlador_cliente = ControladorCliente(TelaCliente())
        self.__controlador_anuncio = ControladorAnuncio(TelaAnuncio(),\
             self.__controlador_cliente)
    
    def gerar_relatorio(self):
        if len(self.__controlador_anuncio.listar_todos_os_anuncios()) == 0:
            self.__tela_sistema.mensagem('Insira pelo menos um anúncio para'+
            'gerar um relatório.')
        else:
            relatorio = True
            while True:
                selecionado = self.__tela_sistema.seleciona_informacoes_relatorio(\
                    self.__controlador_cliente.listar_todos_clientes())
                if selecionado is None:
                    break
                try:
                    if selecionado['cliente'] == '' or \
                        selecionado['data_inicio'] == '' or\
                            selecionado['data_fim']== '':
                            relatorio = False
                            raise CampoEmBrancoException
                    else:
                        try:
                            if self.__controlador_anuncio.verifica_datas(\
                                selecionado['data_inicio'],\
                                    selecionado['data_fim']) is False:
                                    relatorio = False
                                    raise DataInvalidaException
                        except DataInvalidaException as mensagem:
                            self.__tela_sistema.mensagem(mensagem)
                    if selecionado is not None:
                        break
                except CampoEmBrancoException as mensagem:
                    self.__tela_sistema.mensagem(mensagem)
            if selecionado is not None and relatorio:
                codigo_cliente = int(selecionado['cliente'].split('-')[0])
                cliente = self.__controlador_cliente.encontrar_cliente_por_codigo(\
                    codigo_cliente)
                resultados=[]
                for anuncio in \
                    self.__controlador_anuncio.listar_todos_os_anuncios():
                    filtro = self.filtro_relatorio(anuncio, selecionado[\
                        'data_inicio'],selecionado['data_fim'])
                    if anuncio['codigo_cliente'] == cliente.codigo and \
                        filtro is not None:
                            total_investido = float(anuncio['investimento']) *\
                                filtro['dias']
                            quant = calcula_totais(total_investido)
                            r = {'cliente': str(cliente.nome), 'titulo': anuncio['titulo'],
                                'visualizacoes':quant['visualizacoes'],
                                'cliques':quant['cliques'],
                                'compartilhamentos':quant['compartilhamentos'],
                                'total':total_investido, 'data_inicial':filtro['data_inicio'],
                                'data_final':filtro['data_fim']
                                }
                            resultados.append(r)
                try:
                    if len(resultados) == 0:
                        raise FiltroInvalidoException
                    else:
                        self.__tela_sistema.mostrar_relatorio(resultados)
                except FiltroInvalidoException as mensagem:
                    self.__tela_sistema.mensagem(mensagem)
    
    def verifica_datas_iguais(self, data_1, data_2):
        verificacao = True
        ano_data_1 = str(data_1).split('-')[0]
        ano_data_2 = str(data_2).split('-')[0]
        if ano_data_1 != ano_data_2:
            verificacao = False
        else:
            mes_data_1 = str(data_1).split('-')[1]
            mes_data_2 = str(data_2).split('-')[1]
            if mes_data_1 != mes_data_2:
                verificacao = False
            else:
                dia_data_1 = str(str(data_1).split('-')[2]).split(' ')[0]
                dia_data_2 = str(str(data_2).split('-')[2]).split(' ')[0]
                if dia_data_1 != dia_data_2:
                    verificacao = False
        return verificacao
    
    def filtro_relatorio(self,anuncio, inicio_filtro, fim_filtro):
        data_inicio = None
        data_fim = None
        dias = 0
        while data_inicio is None:
            #definição da data inicial
            if self.__controlador_anuncio.verifica_datas(inicio_filtro,\
                anuncio['data_de_inicio']): #se a data inicial do filtro for
                #anterior a data inicial do anúncio
                if self.__controlador_anuncio.verifica_datas(\
                    anuncio['data_de_inicio'],fim_filtro): #se a data inicial do
                    #anuncio for anterior a data de fim do filtro
                    data_inicio = anuncio['data_de_inicio']
                elif self.verifica_datas_iguais(anuncio['data_de_inicio'],\
                    fim_filtro): #se a data de fim do filtro e inicio do anuncio
                    #forem iguais
                    dias = 1
                    data_inicio = anuncio['data_de_inicio']
                    data_fim = anuncio['data_de_inicio']
                else: #se inicio_filtro < fim_filtro < inicio_anuncio, então
                    #o anúncio não foi feito no intervalo filtrado
                    break
            elif self.verifica_datas_iguais(anuncio['data_de_inicio'],\
                inicio_filtro): #se as datas de inicio do anúncio e do filtro
                #forem iguais
                data_inicio = inicio_filtro
            else: #se a data de inicio do filtro for posterior ao inicio do anuncio
                if self.__controlador_anuncio.verifica_datas(inicio_filtro,\
                    anuncio['data_de_termino']): #se o inicio do filtro for
                    #anterior ao fim do anuncio
                    data_inicio = inicio_filtro
                elif self.verifica_datas_iguais(inicio_filtro,\
                    anuncio['data_de_termino']): #se o inicio do filtro for
                    #igual ao fim do anuncio
                    dias = 1
                    data_inicio = anuncio['data_de_termino']
                    data_fim = anuncio['data_de_termino']
                else: #se inicio_anuncio < fim_anuncio < inicio_filtro, então
                    #o anúncio não foi feito no intervalo filtrado
                    print('inicio_anuncio < fim_anuncio < inicio_filtro')
                    break
        if data_inicio is not None and dias == 0: #se existem dias de anuncio
            #ativo dentro do intervalo especificado e forem diferentes de 1.
            #definição da data final
            if self.__controlador_anuncio.verifica_datas(fim_filtro,\
                anuncio['data_de_termino']): #se o fim do filtro for
                #anterior ao fim do anuncio
                data_fim = fim_filtro
            else: #se o fim do anuncio for anterior ou igual ao fim do filtro
                data_fim = anuncio['data_de_termino']
            data_1 = datetime.date(int(data_inicio.split('-')[0]),\
                int(data_inicio.split('-')[1]),\
                    int((data_inicio.split('-')[2]).split(' ')[0]))
            data_2 = datetime.date(int(data_fim.split('-')[0]),\
                int(data_fim.split('-')[1]),\
                    int((data_fim.split('-')[2]).split(' ')[0]))
            dias = int((data_2-data_1).days)+1 #intervalo de dias que inclui as
            #datas selecionadas
        if data_inicio is None or data_fim is None or dias == 0:
            retorno = None
        else:
            retorno = {'data_inicio': str(data_inicio).split(' ')[0],\
                'data_fim': str(data_fim).split(' ')[0], 'dias': dias}
        return retorno
                                  
    def abre_menu_principal(self):
        lista_opcoes = {1: self.__controlador_cliente.inserir_cliente,\
            2: self.__controlador_anuncio.inserir_novo_anuncio,\
                3: self.gerar_relatorio,\
                    4: self.__controlador_anuncio.mostrar_todos_os_anuncios}
        while True:
            valor_lido = self.__tela_sistema.mostra_menu_principal()[0]
            if valor_lido == 0 or valor_lido == None:
                break
            else:
                lista_opcoes[valor_lido]()