# Fecha de última modificación: 2023-12-19

# Considerar que, por defecto, el marco de datos se denomina df

# Importar las librerías requeridas
import pandas as pd

# Crear una tabla de frecuencias absolutas y relativas
def create_count_table(df, column_name):
    count_table = pd.DataFrame(df[column_name].value_counts(sort=False))
    count_table.columns = ['Total']
    count_table['%'] = df[column_name].value_counts(normalize=True).mul(100).round(0)
    return count_table

# Crear una tabla de contingencia con frecuencias absolutas y relativas
def create_cross_table(df, column_name, groupby):
    count_table = df.groupby(groupby)[column_name].value_counts(sort=False).unstack().fillna(0)
    count_table = count_table.astype(int)

    for column in count_table.columns:
        total = count_table[column].sum()
        count_table[column] = count_table[column].astype(str) + " (" + ((count_table[column] / total) * 100).round(0).astype(int).astype(str) + "%)"
    return count_table