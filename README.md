# Gestão de Anúncios

## Descrição do Projeto
Este projeto foi desenvolvido durante o Desafio de Programação para o processo seletivo da Academina Capgemini. O projeto consiste em um sistema de gerenciamento de anúncios, no qual é possível cadastrar clientes, anúncios e emitir o relatório de anúncios.
Além disso, o sistema possui uma interface gráfica para facilitar a interação do usuário com o sistema.

## Funcionalidades
- Cadastrar um cliente; 
  - Cliente(nome:str, telefone:str, email:str, codigo);
- Cadastrar um anúncio;
  - Anuncio(título, cliente, data de início, data de término, investimento diário, codigo);
- Listar anúncios cadastrados;
- Gerar relatório de anúncios;
  - O relatório pode ser filtrado por cliente e período e mostra quanto o cliente investiu, dentro do período informado, em cada um de seus anúncios, assim como os resultados (máximo de visualiações, cliques e compartilhamentos) de cada anúncio;
 
 ## Telas do Sistema
 
 #### Menu Principal
 O menu principal é a tela que abre assim que o sistema inicia. Nela, o usuário pode escolher o que deseja executar.
 
 ![menu_principal](https://user-images.githubusercontent.com/73616453/118419438-5e63a080-b692-11eb-956f-141a4f69c09a.png)
 
 #### Cadastro de Cliente
 No cadastro de clientes, o usuário pode informar o nome, telefone e email do cliente. O único campo obrigatório é o nome. O código é gerado automaticamente.
 
 ![cadastro_cliente](https://user-images.githubusercontent.com/73616453/118419456-6de2e980-b692-11eb-8c18-0699204c9f7a.png)
 
 #### Cadastro de Anúncio
 No cadastro de anúncios, o usuário pode informar o título para o anúncio, selecionar o cliente na caixa de seleção, escolher a data de início e término no calendário e informar o investimento diário do anúncio. Todos os campos são obrigatórios. O código é gerado automaticamente.
 
 ![cadastro_anuncio](https://user-images.githubusercontent.com/73616453/118419477-7cc99c00-b692-11eb-90c3-9a6a3f30bdad.png)
 
 #### Lista de Anúncios Cadastrados
 Mostra todos os anúncios cadastrados no sistema e seus respectivos atributos. Pode ser utilizado para consultar os anúncios e suas datas para então gerar o relatório.
 
 ![lista_anuncios_cadastrados](https://user-images.githubusercontent.com/73616453/118419498-8c48e500-b692-11eb-8b76-ab523497d03a.png)
 
 #### Gerar Relatório de Anúncios
 Nesta tela, o usuário pode selecionar o cliente, a data inicial do relatório e sua data final. O sistema irá retornar (na tela Relatório de Anúncios) um relatório de todos os anúncios que este cliente tiver ativos entre a data inicial e a data final informada.
 
 ![gerar_relatorio](https://user-images.githubusercontent.com/73616453/118419509-966ae380-b692-11eb-8a66-8990fa60cd1c.png)
 
 #### Relatório de Anúncios
 Mosta os anúncios, filtrados por cliente e intervalo de data, e seus respectivos resultados (máximo de visualizações, cliques, compartilhamentos e valor total investido no período).
 
 ![relatorio_anuncios](https://user-images.githubusercontent.com/73616453/118419528-a256a580-b692-11eb-9b70-68f2912944a2.png)
 
 Os resultados são calculados com base no investimento total (investimento_diario * numero_de_dias), de acordo com as seguintes considerações:
 - a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
 - a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
 - cada compartilhamento nas redes sociais gera 40 novas visualizações.
 - 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
 - o mesmo anúncio é compartilhado no máximo 4 vezes em sequência:
    (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)
    
## Como Executar o Sistema
1. No terminal, clonar o repositório: `git clone https://github.com/bruna-nb/gestao-de-anuncios`
2. Ainda no terminal, instalar o pacote PySimple GUI: `<pip install PySimpleGui>`
3. No compilador python de sua preferência, abrir e executar o arquivo 'main.py'

 > Status do Projeto: Concluido :heavy_check_mark:


