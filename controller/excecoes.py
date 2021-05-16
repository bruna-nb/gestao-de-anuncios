class CampoEmBrancoException(Exception):
    def __init__(self):
        super().__init__('Preencha todos os campos obrigatorios (*) antes de '+
        'continuar')

class DataInvalidaException(Exception):
    def __init__(self):
        super().__init__('A data final deve ser maior que a data inicial.')

class FiltroInvalidoException(Exception):
    def __init__(self):
        super().__init__('Não há registros de anúncios para este cliente no' +
        ' prazo especificado')