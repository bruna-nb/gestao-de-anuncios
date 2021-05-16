import PySimpleGUI as sg

class TelaCliente():
    def __init__(self):
        self.__window = None
    
    def inserir_dados(self):
        layout = [
            [sg.Text('Cadastro de Clientes. Informe os dados soliciados.',\
                justification= 'center')],
            [sg.Text('Nome: *'), sg.InputText(key='-nome-')],
            [sg.Text('Telefone: '), sg.InputText(key='-telefone-')],
            [sg.Text('Email: '), sg.InputText(key='-email-')],
            [sg.ReadButton('Cadastrar'),sg.ReadButton('Voltar')]            
        ]
        self.__window = sg.Window('Cadastro de Cliente').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        if button == 'Cadastrar':
            dados = {'nome': values['-nome-'],'telefone': values['-telefone-'],\
                'email': values['-email-']}
        if button == 'Voltar' or button == sg.WIN_CLOSED:
            dados = None
        return dados
    
    def mensagem(self, mensagem: str):
        layout = [
            [sg.Txt(mensagem)],
            [sg.Exit('Ok', size = (20, 1))]
        ]
        self.__window = sg.Window('Aviso!', element_justification = 'c').Layout(layout)
        buttons, values = self.__window.Read()
        self.__window.Close()
