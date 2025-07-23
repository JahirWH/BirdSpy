import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def check():
    try: 
        archivo = pl.read_csv("data.csv")
        nombre = archivo.select(pl.col("divide")).to_numpy().flatten()
        if len(nombre := nombre) == 0:
            raise ValueError("Archivo sin nombre")
        print(f"Nombre: {nombre[0]}")
        try:
            nombre = compare(nombre)
           
            
        









def init():
    check()
