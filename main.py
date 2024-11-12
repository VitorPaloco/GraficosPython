import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados
df = pd.read_excel('Base de dados/Analise_Tickets_TI.xlsx')
plt.rcParams.update({'figure.figsize': (10,6)})

# Cores para o nível de urgência
colors = ['#FF6666', '#FFCC99', '#99FF99', '#66B2FF']
urgency_order = ['Urgente', 'Alta', 'Média', 'Baixa']

# Título
st.title("Grupo do Paloco")
st.title("Análise de Tickets e chamados TI")
st.title("")

# 1. Número de tickets por setor
st.subheader("1. Número de tickets por setor:")
plt.figure()
df['Área de Negócio'].value_counts().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.xlabel('Área de Negócio')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

# 2. Número de tickets por Categoria
st.subheader("2. Número de tickets por categoria:")
plt.figure()
df['Categoria'].value_counts().plot(kind="bar", color='teal')
plt.xlabel('Categoria')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 3. Número de tickets por urgência
st.subheader("3. Número de tickets por urgência:")
filtro_setor_urgencia = st.selectbox("Selecione o Setor", df['Área de Negócio'].unique(), key='setor_urgencia')
df_filtrado_urgencia = df[df['Área de Negócio'] == filtro_setor_urgencia]
df_filtrado_urgencia['Urgência'] = pd.Categorical(df_filtrado_urgencia['Urgência'], categories=urgency_order, ordered=True)
plt.figure()
df_filtrado_urgencia['Urgência'].value_counts().sort_index().plot(kind='bar', color=colors)
plt.xlabel('Urgência')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 4. Número de tickets por assunto
st.subheader("4. Número de tickets por assunto:")
filtro_setor_assunto = st.selectbox("Selecione o Setor", df['Área de Negócio'].unique(), key='setor_assunto')
df_filtrado_assunto = df[df['Área de Negócio'] == filtro_setor_assunto]
plt.figure()
df_filtrado_assunto['Assunto'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Assunto')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)
st.pyplot(plt)

# 5. Distribuição de tickets por tipo
st.subheader("5. Distribuição de tickets por tipo:")
plt.figure()
df['Tipo'].value_counts().plot(kind='bar', color='blue')
plt.xlabel('Tipo de Ticket')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 6. Número de tickets por analista
st.subheader("6. Número de tickets por analista:")
plt.figure()
df['Analista'].value_counts().plot(kind="bar", color='orange')
plt.xlabel('Analista')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 7. Média de tickets por analista por nível de urgência
st.subheader("7. Média de tickets por analista por nível de urgência:")
analyst_urgency = df.pivot_table(index='Analista', columns='Urgência', aggfunc='size', fill_value=0).reindex(columns=urgency_order)
plt.figure()
analyst_urgency.plot(kind='bar', stacked=True, color=colors)
plt.xlabel('Analista')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.legend(title='Urgência')
plt.tight_layout()
st.pyplot(plt)

# 8. Contagem de tickets por status (gráfico de pizza)
st.subheader("8. Contagem de tickets por status:")
plt.figure()
df['Status'].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.ylabel('')
plt.tight_layout()
st.pyplot(plt)

# 9. Top 10 clientes por número de tickets
st.subheader("9. Top 10 clientes por número de tickets:")
top_clients = df['Cliente (Completo)'].value_counts().nlargest(10)
plt.figure()
top_clients.plot(kind="bar", color='purple')
plt.xlabel('Cliente (Completo)')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 10. Tempo médio de fechamento por mês de abertura
st.subheader("10. Tempo médio de fechamento por mês de abertura:")
df['Tempo de Fechamento (dias)'] = (df['Data de Fechamento'] - df['Aberto em']).dt.days
average_closure_time = df.groupby(df['Aberto em'].dt.to_period('M'))['Tempo de Fechamento (dias)'].mean()
plt.figure()
average_closure_time.plot(kind="line", marker='o', color='orange')
plt.xlabel('Mês de Abertura')
plt.ylabel('Tempo Médio de Fechamento (dias)')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 11. Tempo médio de fechamento por nível de urgência
st.subheader("11. Tempo médio de fechamento por nível de urgência:")
urgency_closure_time = df.groupby('Urgência')['Tempo de Fechamento (dias)'].mean().reindex(urgency_order)
plt.figure()
urgency_closure_time.plot(kind='bar', color=colors)
plt.xlabel('Nível de Urgência')
plt.ylabel('Tempo Médio de Fechamento (dias)')
plt.xticks(rotation=90)
plt.tight_layout()
st.pyplot(plt)

# 12. Tempo médio de resolução por analista
st.subheader("12. Tempo médio de resolução por analista:")
analyst_closure_time = df.groupby('Analista')['Tempo de Fechamento (dias)'].mean().sort_values()
plt.figure()
analyst_closure_time.plot(kind='bar', color='red')
plt.xlabel('Analista')
plt.ylabel('Tempo Médio de Fechamento (dias)')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 13. Média de tickets por dia da semana
st.subheader("13. Média de tickets por dia da semana:")
df['Dia da Semana'] = df['Aberto em'].dt.day_name()
tickets_per_day = df['Dia da Semana'].value_counts()
plt.figure()
tickets_per_day.plot(kind='bar', color='green')
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 14. Tempo médio de fechamento por categoria e urgência
st.subheader("14. Tempo médio de fechamento por categoria e urgência:")
closure_by_category_urgency = df.groupby(['Categoria', 'Urgência'])['Tempo de Fechamento (dias)'].mean().unstack().reindex(columns=urgency_order)
plt.figure()
closure_by_category_urgency.plot(kind='bar', stacked=True, color=colors)
plt.xlabel('Categoria')
plt.ylabel('Tempo Médio de Fechamento (dias)')
plt.xticks(rotation=45)
plt.legend(title='Urgência')
plt.tight_layout()
st.pyplot(plt)

# 15. Evolução do backlog de tickets ao longo do tempo
st.subheader("15. Evolução do backlog de tickets ao longo do tempo:")
df['Mês de Abertura'] = df['Aberto em'].dt.to_period('M')
tickets_opened = df.groupby('Mês de Abertura').size()
tickets_closed = df[df['Status'] == 'Fechado'].groupby(df['Data de Fechamento'].dt.to_period('M')).size()
backlog = tickets_opened.cumsum() - tickets_closed.cumsum()

plt.figure()
plt.plot(backlog.index.astype(str), backlog, marker='o', color='purple', label='Backlog')
plt.plot(tickets_opened.index.astype(str), tickets_opened, marker='o', color='blue', label='Tickets Abertos')
plt.plot(tickets_closed.index.astype(str), tickets_closed, marker='o', color='green', label='Tickets Fechados')
plt.xlabel('Mês')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
st.pyplot(plt)

# 16. Taxa de abertura e fechamento de tickets ao longo da semana
st.subheader("16. Taxa de abertura e fechamento de tickets ao longo da semana:")
df['Dia da Semana Abertura'] = df['Aberto em'].dt.day_name()
df['Dia da Semana Fechamento'] = df['Data de Fechamento'].dt.day_name()
opened_per_day = df['Dia da Semana Abertura'].value_counts().sort_index()
closed_per_day = df['Dia da Semana Fechamento'].value_counts().sort_index()

plt.figure()
plt.bar(opened_per_day.index, opened_per_day, color='blue', alpha=0.5, label='Abertos')
plt.bar(closed_per_day.index, closed_per_day, color='green', alpha=0.5, label='Fechados')
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Tickets')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
st.pyplot(plt)
