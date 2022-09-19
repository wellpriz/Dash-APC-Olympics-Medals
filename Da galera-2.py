import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from dash import Dash, dcc, html, Output, Input
#leitura do dados do dataFrame

data = pd.read_csv('https://raw.githubusercontent.com/leticia-oliveira/Exercicios-de-APC-UnB/main/dashboard/datasets/medalhaspaises.csv')
df = pd.DataFrame(data)
dados = df.values.tolist()

second_data = pd.read_excel("https://github.com/VampiraoN/Pai-ta-on/blob/main/athlete_events.xlsx?raw=true")
second_data = second_data.sort_values(['Year','Event'])
second_data = second_data.values.tolist()

#inicio do grafiico de raling individual de paises

def cria_grafico_mais_medalha_ouro(qtd_paises):

    #importa/lê a base de dados
    df = pd.read_csv(
        'https://raw.githubusercontent.com/leticia-oliveira/Exercicios-de-APC-UnB/main/dashboard/datasets/medalhaspaises.csv')
    df_ordenado = df.sort_values(by='total_gold', ascending=False)
    dados = df_ordenado.values.tolist()  # enumera as células como lista


    #prepara uma lista para receber os valores de *países e *medalhas de ouro
    p = []
    o = []

    #laço de repetição que coleta os dados da planilha e "entrega" eles para as listas
    for i in range(qtd_paises):  #  valor quantidade de paises a ser mostrado
        p.append(dados[i][0])  # agrupando todos os paises
        o.append(dados[i][-5])  # agrupando todos os valores de medalha

    fig = px.bar(template="plotly_white")  # define o formato do gráfico
    #adiciona cada barra do gráfico
    fig.add_trace(go.Bar(x=o, y=p, name='Medalhas de ouro', marker_color='#FFDF00',
                marker_pattern_shape="x", text=o, texttemplate='%{text}', textposition='outside', orientation='h'))
    #edita a aparência do gráfico
    titulo='Os '+ str(qtd_paises) + ' países com mais medalhas de ouro'
    fig.update_layout(
        title=titulo,
        xaxis_tickfont_size=14,
        yaxis=dict(title='Quantidade de medalhas',
                titlefont_size=16, tickfont_size=14),
    )

    fig.show()
    
    return fig


#fim do grafico de raling individual de paises


#inicio do grafiico de continentes

#prepara uma lista para receber os valores de *continentes, *medalhas de ouro, *prata e *bronze


continente = []


#seleciona lista de continentes
for coluna in dados:
  if coluna not in continente:
    continente.append(coluna[-1])  # coluna de continentes
# remove os valores repetidos da lista
continente = list(dict.fromkeys(continente))

def cria_grafico_continente(edicoes_olimpicas):

    ouros = [0, 0, 0, 0, 0, 0, 0, 0]
    pratas = [0, 0, 0, 0, 0, 0, 0, 0]
    bronzes = [0, 0, 0, 0, 0, 0, 0, 0]

      #['Inverno', 'Verão', 'Todas']
    if edicoes_olimpicas == "Todas":
        id_ouro = -5
        id_prata = -4
        id_bronze = -3  
                
    if edicoes_olimpicas == "Verão":
        id_ouro = -15
        id_prata = -14
        id_bronze = -13
       
    if edicoes_olimpicas == "Inverno":
        id_ouro = -10
        id_prata = -9
        id_bronze = -8
        

    for coluna_continente in dados:
        if coluna_continente[-1] == continente[0]:
            ouros[0] = ouros[0]+coluna_continente[id_ouro]
            pratas[0] = pratas[0]+coluna_continente[id_prata]
            bronzes[0] = bronzes[0]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[1]:
            ouros[1] = ouros[1]+coluna_continente[id_ouro]  
            pratas[1] = pratas[1]+coluna_continente[id_prata]
            bronzes[1] = bronzes[1]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[2]:
            ouros[2] = ouros[2]+coluna_continente[id_ouro]
            pratas[2] = pratas[2]+coluna_continente[id_prata]
            bronzes[2] = bronzes[2]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[3]:
            ouros[3] = ouros[3]+coluna_continente[id_ouro]
            pratas[3] = pratas[3]+coluna_continente[id_prata]
            bronzes[3] = bronzes[3]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[4]:
            ouros[4] = ouros[4]+coluna_continente[id_ouro]
            pratas[4] = pratas[4]+coluna_continente[id_prata]
            bronzes[4] = bronzes[4]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[5]:
            ouros[5] = ouros[5]+coluna_continente[id_ouro]
            pratas[5] = pratas[5]+coluna_continente[id_prata]
            bronzes[5] = bronzes[5]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[6]:
            ouros[6] = ouros[6]+coluna_continente[id_ouro]
            pratas[6] = pratas[6]+coluna_continente[id_prata]
            bronzes[6] = bronzes[6]+coluna_continente[id_bronze]

        if coluna_continente[-1] == continente[7]:
            ouros[7] = ouros[7]+coluna_continente[id_ouro]
            pratas[7] = pratas[7]+coluna_continente[id_prata]
            bronzes[7] = bronzes[7]+coluna_continente[id_bronze]
       # print(" ------ ")
       


    #define o formato do gráfico
    fig = px.bar(template="plotly_white", barmode='group')
    #adiciona cada barra do gráfico

    fig.add_trace(go.Bar(x=continente, y=pratas, name='Medalhas de prata',
              marker_color='#BBBFC9', text=pratas, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=ouros, name='Medalhas de ouro', marker_color='#FFDF00',
              text=ouros, texttemplate='%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=continente, y=bronzes, name='Medalhas de bronze',
              marker_color='#FFA366', text=bronzes, texttemplate='%{text:.2s}', textposition='outside'))

#edita a aparência do gráfico
    fig.add_layout_image(
    x=0.25,
    sizex=4500,
    y=4590,
    sizey=4500,
    xref="x",
    yref="y",
    opacity=0.3,
    layer="below",
    source="https://cdn-icons-png.flaticon.com/512/523/523676.png"  # imagem das olimpíadas
    )
    fig.update_layout(
    title='Continentes e suas medalhas olímpicas',
    xaxis_tickfont_size=14,
    yaxis=dict(title='Quantidade de medalhas', titlefont_size=16, tickfont_size=14
               ),
    legend=dict(
        x=0.87, y=0.5
    ),
    barmode='group',
    bargroupgap=0.1  # espaço entre as barras do mesmo continente
    )
    #fig.show()
    return fig

#cria_grafico_continente('Inverno')

#cria_grafico_continente('Verão')
#cria_grafico_continente('Todas')


#fim do grafico de continentes




# inicio do grafico PIZZA MEDALHAS DE TODOS 

def cria_grafico_pizza(edicao_olimpica):
#criar listas
    paises = []
    valores = []
    estrutura = []

    #############VARIÁVEIS
    listsummertot = []
    listsummern = []
    listwintertot = []
    listwintern = []
    estrutura2 = []
    estrutura3 = []

    def seleciona_valor(indice_estrutura): #buscando os valores de medalha relacionado a um pais
        return indice_estrutura[1] 

    def seleciona_valor2(indice_estrutura):
        return indice_estrutura[1]

    def seleciona_valor3(indice_estrutura):
        return indice_estrutura[1]

    if edicao_olimpica == 'Todas':
    
        for coluna in dados:
            pais_valor = []   #lista que armazena o pais e o valor da repetição da coluna
            pais_valor.append(coluna[0]) #coluna de paises
            pais_valor.append(coluna[-2]) #coluna de valores totais
            estrutura.append(pais_valor) #lista de lista para armazenar pais e valor de todas iteraçoes
                                    #para ordenar baseado no parametro valor mantendo a conexão com o n
                #e retorna o valor de medalhas como um criterio de ordenaçao

        estrutura.sort(reverse=True,key=seleciona_valor) #ordenando de forma decrescente atraves do atributo valor_total da lista

        for i in range(15):   #15 paises e 1 se5 valores
            paises.append(estrutura[i][0]) #agrupando todos os paises
            valores.append(estrutura[i][1]) #agrupando todos os valores de medalha

        grafico = px.pie(template="plotly_white", values=valores, names=paises, title='15 países que mais conquistaram medalhas em todas as edições das Olimpíadas')

############### GRAFICO DE OLIMIPADAS DE VERÃO - SUMMERTOT
    if edicao_olimpica == 'Verão':

        for coluna in dados:
            pais_valor2 = []
            pais_valor2.append(coluna[0])
            pais_valor2.append(coluna[6])
            estrutura2.append(pais_valor2)

        estrutura2.sort(reverse=True, key=seleciona_valor2)

        for i in range(15):
            listsummern.append(estrutura2[i][0])
            listsummertot.append(estrutura2[i][1])
        grafico = px.pie(df, values=listsummertot, names=listsummern,
                            hole=.2, color_discrete_sequence=px.colors.sequential.OrRd,title='15 países que mais conquistaram medalhas em edições de Verão das Olimpíadas')


############### GRAFICO DE OLIMIPADAS DE INVERNO - SUMMERTOT
    if edicao_olimpica == 'Inverno':
        for coluna in dados:
            pais_valor3 = []
            pais_valor3.append(coluna[0])
            pais_valor3.append(coluna[11])
            estrutura3.append(pais_valor3)

        estrutura3.sort(reverse=True, key=seleciona_valor3)

        for i in range(15):
            listwintern.append(estrutura3[i][0])
            listwintertot.append(estrutura3[i][1])

        grafico = px.pie(df, values=listwintertot, names=listwintern,
                      hole=.2, color_discrete_sequence=px.colors.sequential.PuBu, title='15 países que mais conquistaram medalhas em edições de Inverno das Olimpíadas')
       

    return grafico 
################# FIM DO GRAFICO PIZZA


opcoes_grafico_pizza = ['Inverno', 'Verão', 'Todas']


#inicio do Grafico quadro de medalhas
def list_siglas(): 
    list_sigla = []    
    for coluna in dados:
      list_sigla.append(coluna[1]) 
    return list_sigla

def name_pais(values):
    nome_do_pais = ' '
    for coluna in dados:
      if coluna[1]==values:
        nome_do_pais=coluna[0]

    return nome_do_pais


# Criar o opções da lista drop Down

opcoes = list(list_siglas())
opcoes.append("Todos")




def quadroMedalhas(nome_pais):
  # Criação das variáveis
  gold = []
  silver = []
  bronze = []
  cat_gold = []
  cat_silver = []
  cat_bronze = []

  # Estrutura de repetição que vai escanear o Dataframe e capturar os valores
  for i in dados:
      if i[0] == nome_pais:
          sum_gold = int(i[3])
          sum_silver = int(i[4])
          sum_bronze = int(i[5])

  # Tratamento dos dados para transformá-los em lista
  medalhas = sum_gold, sum_silver, sum_bronze
  
  lst_medalhas = list(medalhas)
  return lst_medalhas


def cria_grafico_quadro_medalhas(value):
    fig = px.bar(template="plotly_white")
    if value == "Todos":
        lst_medalhas = quadroMedalhas('Brazil')
    else:
        lst_medalhas= quadroMedalhas(name_pais(value))
        # Armazenamento dos dados capturados
    cat_medalhas = ['Ouro', 'Prata', 'Bronze']  
    gold = [lst_medalhas[0]]
    silver = [lst_medalhas[1]]
    bronze = [lst_medalhas[2]]
    cat_gold = [cat_medalhas[0]]
    cat_silver = [cat_medalhas[1]]
    cat_bronze = [cat_medalhas[2]]


    fig = px.bar(template="plotly_white")

    fig.add_trace(go.Bar(x=cat_gold, y=gold, name='Medalhas de Ouro', marker_color='#FFDF00', text = gold, texttemplate = '%{text:.1s}', textposition='outside'))
    fig.add_trace(go.Bar(x=cat_silver, y=silver, name='Medalhas de Prata', marker_color='#BBBFC9', text = silver, texttemplate = '%{text:.2s}', textposition='outside'))
    fig.add_trace(go.Bar(x=cat_bronze, y=bronze, name='Medalhas de Bronze', marker_color='#FFA366', text = bronze, texttemplate = '%{text:.2s}', textposition='outside'))

    fig.update_layout(
        title='Medalhas Olímpicas conquistadas pelo '+ name_pais(value)  +' (1896-2016)',
            title_font_size=32,
            xaxis_tickfont_size=28,
            yaxis=dict(title='Quantidade de Medalhas', titlefont_size=28, tickfont_size=18
            ),
            legend=dict(
                x=0, y=1.0
            ))

    return fig   

#Início do grafico de medalhas por esporte

comite = []
base_nova = []

for i in dados:
    comite.append(i[1])

for cell in second_data:
    var_temp = []
    if cell[-1] == 'Gold' or cell[-1] == 'Silver' or cell[-1] == 'Bronze':
        var_temp.append(cell[7])          # 0-NOC
        var_temp.append(cell[8])          # 1-Games
        var_temp.append(cell[12])         # 2-Esporte
        var_temp.append(cell[13])         # 3-Evento
        var_temp.append(cell[14])         # 4-Medalha
        base_nova.append(var_temp)

def pesquisa_e_coleta_de_dados(pais):
    games = []
    sport = []
    event = []
    medal = []
    

    def adicionar_dados():
        games.append(item[1])
        sport.append(item[2])
        event.append(item[3])  
        medal.append(item[4])

    global esportes
    global num_de_medalhas
    esportes = []
    num_de_medalhas = []

    for item in base_nova:
        if item[0] == pais:
            if len(sport) == 0:
                adicionar_dados()
                
            else:
                if item[2] != sport[-1] or item[1] != games[-1] or item[3] != event[-1] or item[4] != medal[-1]:
                    adicionar_dados()
                    
                    if item[2] not in esportes:
                        esportes.append(item[2])
                        num_de_medalhas.append(1)
                    else:
                        indice = esportes.index(item[2])
                        num_de_medalhas[indice] += 1

    indices = list(range(len(num_de_medalhas)))
    indices.sort(key=lambda i: num_de_medalhas[i])
    num_de_medalhas = [num_de_medalhas[i] for i in indices]
    esportes = [esportes[i] for i in indices]

def cria_o_grafico_medalhas_por_esporte(pais):
    pesquisa_e_coleta_de_dados(pais)
    fig = px.bar(template="plotly_white", barmode='relative')
    fig.add_trace(go.Bar(x=esportes[-15:], y=num_de_medalhas[-15:], marker_color='#FFDF00', text=num_de_medalhas[-15:], texttemplate = '%{text:.2s}', textposition = 'outside'))
    return fig

#Fim do gráfico de medalhas por esporte

# INICIO DO DASH
app = Dash(__name__)

colors = {
    'background': '#fffff',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig = cria_grafico_quadro_medalhas("USA")
fig1 = cria_grafico_pizza("Todas")
fig2 = cria_grafico_continente("Verão")
fig4 =  cria_grafico_mais_medalha_ouro(15)
fig5 =  cria_o_grafico_medalhas_por_esporte('BRA')


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.RadioItems(
        options=[
         {'label': 'Todas', 'value': 'Todas'},
         {'label': 'Verão', 'value': 'Verão'},
         {'label': 'Inverno', 'value': 'Inverno'},
        ],
         value='Verão',
         id='edicao_olimpicas'
    ),

    
    dcc.Graph(
        id='grafico_continente',
        figure=fig2),

    dcc.Dropdown(opcoes_grafico_pizza,value='Verão', id='summ_wint'),

    dcc.Graph(
        id='grafico_setor',
        figure=fig1),

      

    html.Div(children='Dash: Grafico de medalhas.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Dropdown(comite, value='Todos', id='siglas_pais'),

    dcc.Graph(
        id='quadro_de_medalhas',
        figure=fig
    ),

    
    dcc.Slider(0, 15, 1, value=15, marks=None, id='slider_qtd_medalhas',
               tooltip={"placement": "bottom", "always_visible": True}),

    dcc.Graph(
        id='medalhas_de_ouro',
        figure=fig4
    ),

    dcc.Dropdown(comite, value = 'BRA', id='otaldodrop'),
    dcc.Graph(
        id='ografico',
        figure= fig5
    ),    

])

@app.callback(
    Output('grafico_continente', 'figure'),
      
    Input('edicao_olimpicas', 'value'),
   
  
)

def update_output1(value):
   
    fig2 = cria_grafico_continente(value)
    return  fig2

@app.callback(
  
    Output('grafico_setor', 'figure'),
        
    Input('summ_wint', 'value'),
  
)

def update_output2(value):

    
    fig1 = cria_grafico_pizza(value)
    
    return  fig1

@app.callback(
   
    Output('quadro_de_medalhas', 'figure'),
    Input('siglas_pais', 'value')
)

def update_output3(value):
    fig = cria_grafico_quadro_medalhas(value)
    return  fig 

@app.callback(
   
    Output('medalhas_de_ouro', 'figure'),
    Input('slider_qtd_medalhas', 'value')
)

def update_output4(value):
    fig4 = cria_grafico_mais_medalha_ouro(value)
    return  fig4 

@app.callback(
    Output('ografico','figure'),
    Input('otaldodrop','value'),
)

def update_output5(value):
    fig5 = cria_o_grafico_medalhas_por_esporte(value)
    return fig5

if __name__ == '__main__':
    app.run_server(debug=False)