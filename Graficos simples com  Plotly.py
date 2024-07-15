# %%
import plotly.express as px

# %%
import pandas as pd

# %%
#Grafico de Gantt  para o caso  de gerenciaento de projetos
import pandas as pd

df_cronograma = pd.read_excel('Tarefas.xlsx')
display(df_cronograma)
fig = px.timeline(df_cronograma, x_start="Início", x_end="Fim", y="Tarefa")
fig.update_yaxes(autorange="reversed") #reverter as categorias de cima para baixo eixo y para melhor visualização
fig.show()

# %%
dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

#estrutura da criação do grafico, dados que entra no eixo X e eixo Y
fig = px.line (x = dados_x, y = dados_y) #px pergunta qual grafico que eu quero criar - e px.line sao os argumentos
display(fig)


# %%
fig = px.line (x = dados_x, y = dados_y, title= "Vendas X Ano", width = 600, height= 300, line_shape=  'spline') #px pergunta qual grafico que eu quero criar - e px.line sao os argumentos
display(fig)

# %%
#bar
fig = px.line (x = dados_x, y = dados_y, title= "Vendas X Ano", width = 600, height= 300, line_shape=  'hv') #px pergunta qual grafico que eu quero criar - e px.line sao os argumentos
display(fig)

# %%
#Alterando o eixo Y do caso - line
dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]
fig = px.line (x = dados_x, y = dados_y, title= "Vendas X Ano", width = 600, height= 300, line_shape=  'spline') #px pergunta qual grafico que eu quero criar - e px.line sao os argumentos

fig.update_yaxes(title = 'Vendas', title_font_color = '#E8EB26') # cor pegou no color picture

display(fig)

# %%
#Grafico de Pizza - pie

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]


fig =  px.pie (names= dados_x, values = dados_y, width= 400, height = 400,)
fig.show()




# %%
#Grafico de Pizza - pie

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]


fig =  px.pie (names= dados_x, values = dados_y, width= 400, height = 400,)
fig.update_traces (title_text = 'Vendas (%)', title_position = 'bottom left')
fig.show()


# %%
#grafico de barra para o caso - bar

#Grafico de Pizza

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]


graf_coluna =  px.bar(x= dados_x, y = dados_y, height=300, width = 600)
graf_coluna.show()

# %%
#Grafico de dispersão -scatter

dados_x = [1, 4, 6, 7, 8, 4, 3, 2, 1, 5]
dados_y = [10, 20, 5, 35, 2, 3, 40, 25, 16, 27]

fig = px.scatter (x= dados_x, y= dados_y, height=300, width = 600)
display(fig)


