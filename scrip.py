import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def load_data():
    try: 
        df = pl.read_csv("GlobalLandTemperaturesByCountry.csv")
        print("Datos cargados exitosamente!")
        print("\nInformación básica del dataset:")
        print(f"Filas: {df.height}, Columnas: {df.width}")
        print("\nPrimeras 5 filas:")
        print(df.head())
        print("\nEstadísticas descriptivas:")
        print(df.describe())
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def visualize_data(df):
    if df is None:
        return
        
    # Convertir a pandas para visualización (polars aún tiene limitaciones con matplotlib)
    df_pd = df.to_pandas()
    
    # Convertir la columna de fecha a datetime
    df_pd['dt'] = pd.to_datetime(df_pd['dt'])
    
    # 1. Evolución de la temperatura promedio mundial a lo largo del tiempo
    plt.figure(figsize=(12, 6))
    global_avg = df_pd.groupby('dt')['AverageTemperature'].mean()
    global_avg.plot(title='Temperatura promedio global a lo largo del tiempo')
    plt.xlabel('Año')
    plt.ylabel('Temperatura (°C)')
    plt.grid()
    plt.show()
    
    # 2. Boxplot de temperaturas por país
    plt.figure(figsize=(12, 8))
    # Tomamos solo los países con más datos para no saturar el gráfico
    top_countries = df_pd['Country'].value_counts().nlargest(20).index
    filtered_df = df_pd[df_pd['Country'].isin(top_countries)]
    sns.boxplot(data=filtered_df, x='Country', y='AverageTemperature')
    plt.title('Distribución de temperaturas por país (top 20)')
    plt.xticks(rotation=90)
    plt.ylabel('Temperatura (°C)')
    plt.show()
    
    # 3. Mapa de calor de correlaciones (si hay suficientes variables numéricas)
    numeric_cols = df_pd.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df_pd[numeric_cols].corr(), annot=True, cmap='coolwarm')
        plt.title('Mapa de calor de correlaciones')
        plt.show()

def init():
    df = load_data()
    visualize_data(df)

if __name__ == "__main__":
    init()