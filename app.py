import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generar datos de ejemplo
np.random.seed(0)
dates = pd.date_range(start='2022-01-01', periods=100)
values = np.random.randn(100).cumsum()
data = pd.DataFrame({'Date': dates, 'Value': values})

# Configurar la interfaz de usuario de Streamlit
st.title("Mi primer sitio con streamlit");

# Dividir la página en dos columnas
col1, col2 = st.columns(2)

# Primera columna: gráfico de línea de tiempo
with col1:
    st.header('Gráfico de Línea de Tiempo')
    fig = px.line(data, x='Date', y='Value', title='Valores a lo largo del tiempo')
    st.plotly_chart(fig)

# Segunda columna: selector de datos y botón de calcular
with col2:
    st.header('Selector de Datos y Cálculo')
    
    # Selector de datos
    date_selected = st.date_input('Selecciona una fecha', value=data['Date'].iloc[0])
    
    # Botón de calcular
    if st.button('Calcular'):
        # Realizar algún cálculo con la fecha seleccionada
        result = data[data['Date'] == date_selected]['Value'].values
        if result.size > 0:
            st.write(f'El valor para {date_selected} es {result[0]:.2f}')
        else:
            st.write('Fecha no encontrada en los datos')
