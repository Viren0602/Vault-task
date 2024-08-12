import pandas as pd
import psycopg2

# Load the Excel file
df = pd.read_excel('reliance_data.xlsx', sheet_name='Profit and Loss')

# Connect to PostgreSQL
conn_str = {
    'dbname': 'db',
    'user': 'user',
    'password': 'password',
    'host': 'server',
    'port': '5432'  # Default port for PostgreSQL
}
conn = psycopg2.connect(**conn_str)
cur = conn.cursor()

# Insert data into the database
for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO financial_data (column1, column2) VALUES (%s, %s)",
        (row['Column1'], row['Column2'])
    )

conn.commit()
cur.close()
conn.close()





# import pandas as pd
# import pyodbc

# # Load the Excel file
# df = pd.read_excel('reliance_data.xlsx', sheet_name='Profit and Loss')

# # Connect to SQL Server
# conn_str = (
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'SERVER=server;'
#     'DATABASE=db;'
#     'UID=user;'
#     'PWD=password'
# )
# conn = pyodbc.connect(conn_str)
# cur = conn.cursor()

# # Insert data into the database
# for index, row in df.iterrows():
#     cur.execute(
#         "INSERT INTO financial_data (column1, column2) VALUES (?, ?)",
#         (row['Column1'], row['Column2'])
#     )

# conn.commit()
# cur.close()
# conn.close()
