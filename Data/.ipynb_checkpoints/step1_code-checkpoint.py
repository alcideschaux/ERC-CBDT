import pandas as pd
import unidecode

# Cargar los archivos
cuestionario_cbdt = pd.read_excel("Cuestionario CBDT.xlsx")
sociodemograficos = pd.read_excel("Sociodemográficos.xlsx")

# Combinar ambos DataFrames
merged_data = pd.merge(cuestionario_cbdt, sociodemograficos, left_on='ID', right_on='Num.', how='outer')

# Limpiar y homogeneizar columnas
merged_data.columns = merged_data.columns.str.lower().str.strip().str.replace('á', 'a').str.replace('ó', 'o').str.replace(' ', '_')
merged_data.drop(['num.', '_merge'], axis=1, inplace=True)
merged_data['estado_civil_padres'] = merged_data['estado_civil_padres'].replace(['Separados, madre fallecida'], ['Separados']).str.capitalize()
merged_data = merged_data.replace("No tiene datos madre fallecida", float("nan"))
merged_data['edad'] = merged_data['edad'].astype(float)

# Guardar el conjunto de datos limpio
merged_data.to_csv("data_cleaned.csv", index=False)
