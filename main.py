import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do Dashboard
st.title('Dashboard de Vendas - Loja de Departamento')

# Upload do arquivo CSV
dados = st.file_uploader('Envie seu arquivo de vendas (.csv)', type='csv')

if dados:
    # Carregar os dados
    df = pd.read_csv(dados)

    st.subheader('Visualização dos Dados')
    st.dataframe(df.head())

    # Cálculos Gerais
    vendas_totais = df['Total_Sales'].sum()
    quantidade_total = df['Quantity_Sold'].sum()
    ticket_medio = vendas_totais / quantidade_total

    # KPIs
    st.subheader('Indicadores')
    col1, col2, col3 = st.columns(3)

    col1.metric("Vendas Totais", f"R$ {vendas_totais:,.2f}")
    col2.metric("Quantidade Vendida", f"{quantidade_total}")
    col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

    # Análise por Categoria
    receita_categoria = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
    quantidade_categoria = df.groupby('Category')['Quantity_Sold'].sum().sort_values(ascending=False)

    st.subheader('Receita por Categoria')
    fig1, ax1 = plt.subplots()
    receita_categoria.plot(kind='barh', ax=ax1)
    ax1.set_xlabel('Receita Total (R$)')
    ax1.set_ylabel('Categoria')
    ax1.invert_yaxis()
    st.pyplot(fig1)

    st.subheader('Quantidade Vendida por Categoria')
    fig2, ax2 = plt.subplots()
    quantidade_categoria.plot(kind='barh', ax=ax2)
    ax2.set_xlabel('Quantidade Vendida')
    ax2.set_ylabel('Categoria')
    ax2.invert_yaxis()
    st.pyplot(fig2)

else:
    st.info('Aguardando o envio do arquivo CSV para exibir a análise.')
