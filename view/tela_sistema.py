import PySimpleGUI as sg
class TelaSistema():

    def __init__(self):
        self.__window = None

    def mostra_menu_principal(self):
        layout = [
                [sg.Txt('Bem vindo ao sistema de gerenciamento de anúncios!',\
                    justification='center')],
                [sg.Txt('Clique na opção desejada',justification='center')],
                [sg.ReadButton('Cadastrar Cliente', size = (30, 1), key = 1)],
                [sg.ReadButton('Cadastrar Anúncio', size = (30, 1), key = 2)],
                [sg.ReadButton('Listar Anuncios Cadastrados', size = (30,1),\
                    key = 4)],
                [sg.ReadButton('Gerar Relatório', size = (30, 1), key = 3)],
                [sg.ReadButton('Sair',size = (30, 1), key = 0)]
            ]
        self.__window = sg.Window('SISTEMA DE GERENCIAMENTO DE ANÚNCIOS',\
            size = (400, 250), element_justification='c').Layout(layout)
        button = self.__window.Read()
        escolhido = button
        self.__window.Close()
        return escolhido

    def seleciona_informacoes_relatorio(self, lista_clientes):
        clientes = []
        for cliente in lista_clientes:
            cod_nome = str(cliente['codigo']) + ' - ' + str(cliente['nome'])
            clientes.append(cod_nome)
        layout = [
            [sg.Text('Relatório de Anúncios. Selecione abaixo o cliente e o'+
            'intervalo de datas desejado.', justification = 'center')],
            [sg.Text('Cliente: *'), sg.InputCombo(clientes, key='-cliente-')],
            [sg.In(key = '-data_inicio-', visible = False),\
                sg.CalendarButton('Selecionar Data de Início*',\
                    target = '-data_inicio-', pad = None, key = '-cal_inicio-')],
            [sg.In(key = '-data_fim-', visible = False),\
                sg.CalendarButton('Selecionar Data de Fim*', target = '-data_fim-',\
                    pad = None, key = '-cal_fim-')],
            [sg.ReadButton('Gerar Relatório'),sg.ReadButton('Voltar')]
        ]           
        self.__window = sg.Window('Geração de Relatório').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Gerar Relatório':
            dados = {'cliente': values['-cliente-'],'data_inicio': \
                values['-data_inicio-'], 'data_fim': values['-data_fim-']}
        if button == 'Voltar' or button == sg.WIN_CLOSED:
            dados = None
        return dados
    
    def mostrar_relatorio(self,resultados):
        if len(resultados) == 0:
            self.mensagem('Não há nenhum anúncio para este cliente no'+
            'intervalo especificado')
        else:
            separator = ' '
            big_string = ''
            for resultado in resultados:
                lista = ('\nCliente:', str(resultado['cliente']), 
                        '\nTítulo do Anúncio:', str(resultado['titulo']),
                        '\nIntervalo:', str(resultado['data_inicial']), 'a',
                        str(resultado['data_final']),
                        '\nMáximo de Visualizações:', str(resultado['visualizacoes']),
                        '\nMáximo de Cliques:', str(resultado['cliques']),
                        '\nMáximo de Compartilhamentos: ',
                        str(resultado['compartilhamentos']),'\nTotal Investido: R$',
                        str(resultado['total']),'\n-------------------------')
                big_string += separator.join(lista)
            layout = [
                [sg.Txt('Relatório de Anúncios: ')],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window('Relatório de Anúncios').Layout(layout)
            button, values = self.__window.Read()
            self.__window.Close()
    
    def mensagem(self, mensagem: str):
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()