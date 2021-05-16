import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import CalendarButton, InputCombo

class TelaAnuncio():
    def __init__(self):
        self.__window = None
    
    def obter_dados(self, lista_clientes):
        clientes = []
        for cliente in lista_clientes:
            cod_nome = str(cliente['codigo']) + ' - ' + str(cliente['nome'])
            clientes.append(cod_nome)
        layout = [
            [sg.Text('Cadastro de Anúncios. Informe os dados soliciados.',\
                justification = 'center')],
            [sg.Text('Título: *'), sg.InputText(size=(30,10),key='-titulo-')],
            [sg.Text('Cliente: *'), sg.InputCombo(clientes, key='-cliente-')],
            [sg.In(key = '-data_inicio-', visible = False),\
                sg.CalendarButton('Selecionar Data de Inicio*',\
                    target = '-data_inicio-', pad = None, key = '-cal_inicio-')],
            [sg.In(key = '-data_fim-', visible = False),\
                sg.CalendarButton('Selecionar Data de Fim*',\
                    target = '-data_fim-', pad = None, key = '-cal_fim-')],
            [sg.Text('Investimento Diário: *R$'), \
                sg.InputText(size=(17,10),key='-investimento-')],
            [sg.ReadButton('Cadastrar'),sg.ReadButton('Voltar')]            
        ]
        self.__window = sg.Window('Cadastro de Anúncio').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Cadastrar':
            dados = {'titulo': values['-titulo-'],'cliente': values['-cliente-'],\
                'data_inicio': values['-data_inicio-'], 'data_fim': \
                    values['-data_fim-'], 'investimento': values['-investimento-']}
        if button == 'Voltar' or button == sg.WIN_CLOSED:
            dados = None
        return dados

    def listar_anuncios(self,anuncios):
        if len(anuncios) == 0:
            self.mensagem('Não há nenhum anúncio cadastrado')
        else:
            separator = ' '
            big_string = ''
            for anuncio in anuncios:
                lista = ('\nCliente:', str(anuncio['cliente']), 
                        '\nTítulo do Anúncio:', str(anuncio['titulo']),
                        '\nIntervalo:', str(anuncio['data_de_inicio']).split(' ')[0],
                        'a', str(anuncio['data_de_termino']).split(' ')[0],
                        '\nInvestimento Diario: R$', str(anuncio['investimento']),
                        '\n-------------------------')
                big_string += separator.join(lista)
            layout = [
                [sg.Txt('Lista de Anúncios Cadastrados: ')],
                [sg.Txt(big_string)],
                [sg.Exit('Ok', size = (20, 1))]
                ]
            self.__window = sg.Window('Lista de Anúncios').Layout(layout)
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
