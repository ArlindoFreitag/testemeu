import streamlit as st
import mysql.connector
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Função para criar a conexão com o MySQL
def create_connection():
    return mysql.connector.connect(
        host="homeotag.com.br",  # Substitua pelo host do seu banco de dados
        user="homeotag_user",       # Substitua pelo usuário do banco de dados
        password="Homeotag@2024",  # Substitua pela senha do seu banco de dados
        database="homeotag_base"  # Substitua pelo nome do banco de dados
    )

# Estabelecer a conexão
conn = create_connection()

# Criar um cursor para executar consultas SQL
cursor = conn.cursor()

st.write('Cadastro de Reinos')

# Executar uma consulta
cursor.execute('SELECT reino_nome FROM tab_reinos')

# Buscar os resultados
rows = cursor.fetchall()

# Pegar os nomes das colunas
colunas = [i[0] for i in cursor.description]

# Converter os dados para um DataFrame do pandas
df = pd.DataFrame(rows, columns=colunas)

# Configurar opções da AgGrid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gridOptions = gb.build()

# Mostrar o DataFrame como uma grid com linhas zebradas usando AgGrid
AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True, theme="streamlit", fit_columns_on_grid_load=True)

# Fechar a conexão e o cursor
cursor.close()
conn.close()
