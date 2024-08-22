import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
from sqlalchemy import create_engine, Integer
from sqlalchemy.sql import text

# URL of the webpage to scrape
url = 'https://screener.in/company/RELIANCE/consolidated/'

try:
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses

    # Parse the content with BeautifulSoup
    soup = bs(response.text, 'html.parser')

    # Find the section containing the profit-loss data
    profit_loss_section = soup.find('section', id="profit-loss")
    if not profit_loss_section:
        raise ValueError("Failed to find the profit-loss section in the webpage.")
    
    # Find the table within the section
    table = profit_loss_section.find("table")
    if not table:
        raise ValueError("Failed to find the table in the profit-loss section.")
    
    # Extract table data
    table_data = []
    for row in table.find_all('tr'):
        row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)
    
    # Write table data to a CSV file
    with open("table_data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table_data)
    
    # Convert table data to a Pandas DataFrame
    df_table = pd.DataFrame(table_data)
    
    # Set the first row as the header and drop it from data
    df_table.columns = df_table.iloc[0]
    df_table = df_table[1:]
    df_table.reset_index(drop=True, inplace=True)

    # Ensure 'Narration' is set correctly
    df_table.insert(0, 'id', range(1, len(df_table) + 1))
    df_table.insert(1, 'Narration', df_table.iloc[:, 1])
    df_table = df_table.drop(df_table.columns[2], axis=1)

    # Check DataFrame columns before melting
    print("Columns before melting:", df_table.columns)
    print(df_table.head())

    df_table = df_table.drop(df_table.columns[0],axis=1)
    # Reshape the DataFrame including 'id'
    df_melted = pd.melt(df_table, id_vars=['Narration'], var_name='Year', value_name='Value')
    df_melted = df_melted.sort_values(by=['Narration', 'Year']).reset_index(drop=True)

    # Generate new unique ids
    df_melted.insert(0, 'id', range(1, len(df_melted) + 1))
    
    print("Melted DataFrame:")
    print(df_melted.head(20))

    # Database connection details
    db_user = "root"
    db_password = "test"
    db_host = "localhost"
    db_name = "connect_test"
    db_port = "3307"  # Change to '3306' if running inside Docker
    
    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    # Load the DataFrame into the MySQL database
    df_melted.to_sql('profit_loss_data', con=engine, if_exists='replace', index=False, dtype={'id': Integer})

    # Add primary key constraint to 'id' column
    with engine.connect() as connection:
        alter_table_sql = """
            ALTER TABLE profit_loss_data
            ADD PRIMARY KEY (id);
        """
        connection.execute(text(alter_table_sql))
    
    print("Data loaded successfully into MySQL database!")

except requests.RequestException as e:
    print(f"Error fetching data from URL: {e}")
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")








# # original code

# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import csv
# from sqlalchemy import create_engine

# # URL of the webpage to scrape
# url = 'https://screener.in/company/RELIANCE/consolidated/'

# try:
#     # Get the webpage content
#     webpage = requests.get(url)
#     webpage.raise_for_status()  # Raise an HTTPError for bad responses
#     soup = bs(webpage.text, 'html.parser')

#     # Find the section containing the profit-loss data
#     data = soup.find('section', id="profit-loss")
#     if not data:
#         raise ValueError("Failed to find the profit-loss section in the webpage.")
    
#     tdata = data.find("table")
#     if not tdata:
#         raise ValueError("Failed to find the table in the profit-loss section.")
    
#     # Extract table data
#     table_data = []
#     for row in tdata.find_all('tr'):
#         row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
#         table_data.append(row_data)
    
#     # Write the table data to a CSV file
#     with open("table_data.csv", 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(table_data)

#     # Convert the table data to a Pandas DataFrame
#     df_table = pd.DataFrame(table_data)
   
    


#     # Debug the DataFrame
#     print("Initial DataFrame:")
#     print(df_table.head(5))

#     # Check for blank or invalid column names
#     print("Column names before setting header:")
#     print(df_table.columns.tolist())

#     # Fix column names: The first row should be the header
#     df_table.columns = df_table.iloc[0]  # Set the first row as the header
#     df_table = df_table[1:]  # Remove the header row from the data

#     if not df_table.empty:
#         df_table.columns = ['Narration'] + df_table.columns[1:].tolist()

    

#     # Drop any columns with blank names or invalid data
#     df_table = df_table.loc[:, df_table.columns.notna()]
#     df_table.columns = df_table.columns.str.strip()

#     # Reset index
#     # df_table.reset_index(drop=True, inplace=True)

#     # Check DataFrame columns and data after cleanup
#     print("DataFrame columns after cleanup:")
#     print(df_table.columns)
#     print(df_table.head(5))

#     # Ensure all column names are non-blank and unique
#     if df_table.columns.duplicated().any():
#         raise ValueError("Duplicate column names found in DataFrame.")
    
#     if df_table.columns.isnull().any() or (df_table.columns == '').any():
#         raise ValueError("Blank column names found in DataFrame.")


#     # Ensure percentage columns are handled correctly
#     if 'OPM %' in df_table.columns:
#         df_table['OPM %'] = df_table['OPM %'].str.replace('%', '').astype(float) / 100
#     if 'Tax %' in df_table.columns:
#         df_table['Tax %'] = df_table['Tax %'].str.replace('%', '').astype(float) / 100
#     if 'Dividend Payout %' in df_table.columns:
#         df_table['Dividend Payout %'] = df_table['Dividend Payout %'].str.replace('%', '').astype(float) / 100

#     # Print DataFrame and column names before database upload
#     print("DataFrame before loading to database:")
#     print(df_table.head(5))

#     # Database connection details
#     db_user = "root"
#     db_password = "test"
#     db_host = "localhost"
#     db_name = "connect_test"
#     db_port = "3307"  # Change to '3306' if running inside Docker

#     # Create SQLAlchemy engine
#     engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
#     # Load the DataFrame into the MySQL database
#     df_table.to_sql('profit_loss_data', engine, if_exists='replace', index=False)

#     print("Data loaded successfully into MySQL database!")
# except requests.RequestException as e:
#     print(f"Error fetching data from URL: {e}")
# except ValueError as e:
#     print(f"Value Error: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")





























# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import csv
# import psycopg2
# from sqlalchemy import create_engine
 
# url = 'https://screener.in/company/RELIANCE/consolidated/'
# webpage = requests.get(url)
# soup = bs(webpage.text, 'html.parser')
 
# data = soup.find('section', id="profit-loss")
# tdata = data.find("table")
 
# table_data = []
# for row in tdata.find_all('tr'):
#     row_data = []
#     for cell in row.find_all(['th', 'td']):
#         row_data.append(cell.text.strip())
#     table_data.append(row_data)
 
# with open("table_data.csv", 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(table_data)
 
# df_table = pd.DataFrame(table_data)
# df_table.iloc[0, 0] = 'Section'
# df_table.columns = df_table.iloc[0]
# df_table = df_table[1:]
 
# # Ensure only valid numeric data is processed with eval
# def safe_eval(val):
#     try:
#         return eval(val)
#     except:
#         return val
 
# for i in df_table.iloc[:, 1:].columns:
#     df_table[i] = df_table[i].str.replace(',', '').str.replace('%', '/100').apply(safe_eval)
 
# db_host = "192.168.3.174"
# db_name = "concourse"
# db_user = "concourse_user"
# db_password = "concourse_pass"
# db_port = "5432"
 
# engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
 
# # Load the DataFrame into the PostgreSQL database
# df_table.to_sql('profit_loss_data', engine, if_exists='replace', index=False)
 
# print("Data loaded successfully into PostgreSQL database!")
