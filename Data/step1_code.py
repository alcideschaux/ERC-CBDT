import pandas as pd

# Load the data
cuestionario_cbdt = pd.read_excel("/path/to/Cuestionario CBDT.xlsx")
sociodemograficos = pd.read_excel("/path/to/Sociodemográficos.xlsx")

# Merge the dataframes
combined_df = pd.merge(cuestionario_cbdt, sociodemograficos, left_on="ID", right_on="Num.", how="outer")

# Standardize the responses for the questionnaire columns
combined_df.replace({"SI": "SÍ"}, inplace=True)

# Merging "Separados, madre fallecida" with "Separados"
combined_df['Estado Civil de los padres'].replace({"Separados, madre fallecida": "Separados"}, inplace=True)

# Treating "No tiene datos madre fallecida" as a missing value
combined_df['ocupacion mamá'].replace({"No tiene datos madre fallecida": None}, inplace=True)

# Removing extra spaces and standardizing the capitalization for specific columns
columns_to_clean = ['Sexo', 'Estado Civil de los padres', 'Escolaridad Mamá', 
                    'Escolaridad Papá', 'Escolaridad Paciente', 'ocupacion mamá']
for col in columns_to_clean:
    combined_df[col] = combined_df[col].str.strip().str.capitalize()

# Reordering the columns: First the sociodemographic factors and then the questionnaire responses
sociodemographic_columns = sociodemograficos.columns.tolist()
questionnaire_columns = cuestionario_cbdt.columns.tolist()
ordered_combined_df = combined_df[sociodemographic_columns + questionnaire_columns]

# Save the cleaned and ordered data to a CSV
ordered_combined_df.to_csv("/path/to/save/ordered_corrected_data.csv", index=False)
