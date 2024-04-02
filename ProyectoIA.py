import streamlit as st
import pickle
import numpy as np

# Cargar el modelo
with open("modelobosque.bin", "rb") as file:
    modelo = pickle.load(file)

def main():
    st.title("Aplicación de Inteligencia Artificial")
    st.write("Juan Pablo Pérez Bayona y Laura Daniela Cabarcas Tovar")
    st.write("¡Bienvenido! Esta es una aplicación simple de Streamlit.")
    st.write("Un modelo de inteligencia artificial es una representación matemática de un proceso de toma de decisiones que se basa en datos. Estos modelos pueden aprender patrones complejos y hacer predicciones o tomar decisiones sin ser explícitamente programados para realizar una tarea específica. La inteligencia artificial abarca una amplia gama de técnicas y algoritmos, incluidos los modelos de aprendizaje automático y de aprendizaje profundo.")
    st.write("El preprocesamiento de datos es un paso crucial en el desarrollo de modelos de inteligencia artificial. Consiste en la limpieza, transformación y selección de los datos antes de ser utilizados para entrenar un modelo. El preprocesamiento de datos es importante porque los datos sin procesar pueden contener ruido, valores atípicos, datos faltantes o inconsistencias, lo que puede afectar negativamente el rendimiento del modelo. Al preprocesar los datos, se pueden mejorar la calidad y la eficacia del modelo final, lo que lleva a mejores predicciones y decisiones.")
    st.write("Entre los modelos de inteligencia artificial, los bosques aleatorios son conocidos por su robustez y precisión en una amplia gama de problemas de aprendizaje automático. Un bosque aleatorio es un conjunto de árboles de decisión entrenados de forma independiente, donde cada árbol vota por la clase más popular. Debido a su capacidad para manejar conjuntos de datos grandes, no lineales y complejos, así como para reducir el sobreajuste, los bosques aleatorios suelen tener una alta precisión en comparación con otros modelos de aprendizaje automático. Su versatilidad y rendimiento hacen que los bosques aleatorios sean uno de los modelos más utilizados en la práctica.")
    def seleccionar():
        # Filtrar por ANTIG con un slider o entrada manual
        ANTIG = st.sidebar.number_input("Ingrese el valor de ANTIG", min_value=1, max_value=150, value=75, step=1)
        
        # Filtrar por COMP con un slider
        COMPS = st.sidebar.number_input("Seleccionar COMP", min_value=4000, max_value=18000, value=8000, step=100)
        
        # Filtrar por PROM
        PROMS = st.sidebar.number_input("Seleccionar PROM", min_value=0.7, max_value=9.0, value=5.0,step=0.5)

        # Filtrar por PROM
        CATEG = st.sidebar.number_input("Seleccionar CATEG", min_value=1000, max_value=7000, value=4000, step=100)
        
        # Filtrar por COMINT
        COMINTS = st.sidebar.number_input("Seleccionar COMINT", min_value=1500, max_value=58000, value=12000, step=100)
        
        # Filtrar por COMPPRES
        COMPPRESS = st.sidebar.number_input("Seleccionar COMPPRESS", min_value=17000, max_value=90000, value=25000, step=100)
        
        # Filtrar por RATE
        RATES = st.sidebar.number_input("Seleccionar RATE", min_value=0.5, max_value=4.2, value=2.0, step=0.1)

        # Filtrar por RATE
        VISIT = st.sidebar.number_input("Seleccionar VISIT", min_value=0, max_value=100, value=50,step= 2)
        
        # Filtrar por DIASSINQ
        DIASSINQS = st.sidebar.number_input("Seleccionar DIASSINQ", min_value=270, max_value=1800, value=500, step=10)
        
        # Filtrar por TASARET
        TASARETS = st.sidebar.number_input("Seleccionar TASARET", min_value=0.3, max_value=1.9, value=0.8, step=0.5)
        
        # Filtrar por NUMQ
        NUMQS = st.sidebar.number_input("Seleccionar NUMQ", min_value=3.0, max_value=10.0, value=4.0,step= 0.5)
        
        # Filtrar por departamento
        RETRES = st.sidebar.number_input("Ingrese el valor de RETRE entre 3 y 30", min_value=3.0, max_value=30.0, value=3.3, step=0.5)

        return [ANTIG,COMPS, PROMS,CATEG, COMINTS, COMPPRESS, RATES,VISIT, DIASSINQS, TASARETS, NUMQS, RETRES]

    dfc = seleccionar()

    st.subheader("Modelo Bosque")
    st.write(dfc)

    if st.button('RUN'):
        # Convertir la lista en una matriz 2D
        dfc = np.array(dfc).reshape(1, -1)
        resultado = modelo.predict(dfc)
        if resultado == 1:
            st.success("El cliente se retira.")
            st.success(resultado)
        else:
            st.success("El cliente no se retira.")
            st.success(resultado)
        
if __name__ == "__main__":
    main()


