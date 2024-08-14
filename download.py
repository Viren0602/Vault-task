# import hvac
# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import csv
 
# # URL for the data you want to scrape
# url = 'https://www.screener.in/company/RELIANCE/consolidated/'
 
# # Perform web scraping
# webpage = requests.get(url)# Sends a GET request to the specified URL and retrieves the webpage's content.
# # Parses the HTML content of the webpage. soup now contains the entire HTML structure of the webpage.
# soup = bs(webpage.text, 'html.parser')
 
# # Extract profit and loss data
# data = soup.find('section', id="profit-loss", class_="card card-large") #Locates the section of the HTML document where the Profit and Loss data is stored by matching the id and class attributes.
# tdata = data.find("table")
# table_data = []
# for row in tdata.find_all('tr'):        # Iterates through all rows (<tr> elements) in the table
#    row_data = []
#    for cell in row.find_all(['th', 'td']):  #For each row, it finds all header (<th>) and data (<td>) cells.
#        row_data.append(cell.text.strip()) #Extracts and cleans the text from each cell, removing any leading or trailing whitespace.
#    table_data.append(row_data) #The cleaned data for each row is appended to row_data, and row_data is then appended to table_data.
 
# # Save table data to a CSV file
# with open("profit_loss.csv", 'w', newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows(table_data)
 
# # Load table data into DataFrame
# df_table = pd.DataFrame(table_data)
# df_table.columns = df_table.iloc[0]
# df_table = df_table[1:]
# df_table = df_table.set_index('')
# df_table
 
# # Save DataFrame to a CSV file
# df_table.to_csv('profit_loss.csv')



# import psycopg2
# import pandas as pd

# # Data as a dictionary
# data = {
#     "Year": ["Mar 2013", "Mar 2014", "Mar 2015", "Mar 2016", "Mar 2017", "Mar 2018", "Mar 2019", "Mar 2020", "Mar 2021", "Mar 2022", "Mar 2023", "Mar 2024", "TTM"],
#     "Sales": ["395,957", "433,521", "374,372", "272,583", "303,954", "390,823", "568,337", "596,679", "466,307", "694,673", "876,396", "899,041", "925,289"],
#     "Expenses": ["362,802", "398,586", "336,923", "230,802", "257,647", "326,508", "484,087", "507,413", "385,517", "586,092", "734,078", "736,543", "762,384"],
#     "Operating Profit": ["33,155", "34,935", "37,449", "41,781", "46,307", "64,315", "84,250", "89,266", "80,790", "108,581", "142,318", "162,498", "162,905"],
#     "OPM %": ["8%", "8%", "10%", "15%", "15%", "16%", "15%", "15%", "17%", "16%", "16%", "18%", "18%"],
#     "Other Income": ["7,757", "8,865", "8,528", "12,212", "9,222", "9,869", "8,406", "8,570", "22,432", "19,600", "12,020", "16,179", "16,438"],
#     "Interest": ["3,463", "3,836", "3,316", "3,691", "3,849", "8,052", "16,495", "22,027", "21,189", "14,584", "19,571", "23,118", "23,199"],
#     "Depreciation": ["11,232", "11,201", "11,547", "11,565", "11,646", "16,706", "20,934", "22,203", "26,572", "29,782", "40,303", "50,832", "52,653"],
#     "Profit before tax": ["26,217", "28,763", "31,114", "38,737", "40,034", "49,426", "55,227", "53,606", "55,461", "83,815", "94,464", "104,727", "103,491"],
#     "Tax %": ["20%", "22%", "24%", "23%", "25%", "27%", "28%", "26%", "3%", "19%", "22%", "25%", ""],
#     "Net Profit": ["20,886", "22,548", "23,640", "29,861", "29,833", "36,080", "39,837", "39,880", "53,739", "67,845", "74,088", "79,020", "78,207"],
#     "EPS in Rs": ["30.31", "32.62", "34.14", "43.03", "43.11", "53.39", "58.55", "58.20", "77.50", "89.74", "98.59", "102.90", "101.61"],
#     "Dividend Payout %": ["13%", "12%", "12%", "10%", "11%", "10%", "10%", "10%", "9%", "9%", "9%", "10%", ""]
# }

# # Convert the dictionary into a DataFrame
# df = pd.DataFrame(data)

# # Replace commas in numeric columns and convert them to numeric types
# for col in df.columns[1:]:
#     df[col] = df[col].str.replace(',', '').str.rstrip('%').apply(pd.to_numeric, errors='coerce')

# # Connect to PostgreSQL
# conn = psycopg2.connect(
#     host="localhost",  # Use just "localhost" here
#     port="5432",  # Specify the port separately
#     database="concourse",
#     user="concourse_user",
#     password="viren@9999"
# )
# cur = conn.cursor()

# # Create a table in PostgreSQL
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS profit_loss (
#     year VARCHAR PRIMARY KEY,
#     sales NUMERIC,
#     expenses NUMERIC,
#     operating_profit NUMERIC,
#     opm_percentage NUMERIC,
#     other_income NUMERIC,
#     interest NUMERIC,
#     depreciation NUMERIC,
#     profit_before_tax NUMERIC,
#     tax_percentage NUMERIC,
#     net_profit NUMERIC,
#     eps NUMERIC,
#     dividend_payout NUMERIC
# );
# '''
# cur.execute(create_table_query)

# # Insert DataFrame into PostgreSQL
# for i, row in df.iterrows():
#     insert_query = sql.SQL('''
#     INSERT INTO profit_loss (year, sales, expenses, operating_profit, opm_percentage, other_income, interest, depreciation, profit_before_tax, tax_percentage, net_profit, eps, dividend_payout)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     ON CONFLICT (year) DO NOTHING;
#     ''')
#     cur.execute(insert_query, tuple(row))

# # Commit changes and close the connection
# conn.commit()
# cur.close()
# conn.close()

# print("Profit & Loss data inserted into PostgreSQL.")





















import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2
 
# URL of the webpage to scrape
url = "https://www.screener.in/company/RELIABLE/consolidated/"
 
# Send a GET request to the URL
response = requests.get(url)
 
# Check if the request was successful
if response.status_code == 200:
    print("Page retrieved successfully.")
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()
 
# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")
 
# Scrape the "Profit & Loss" data
profit_loss_table = soup.find("section", {"id": "profit-loss"}, class_="card card-large")
 
if profit_loss_table:
    datatable = profit_loss_table.find("table")
    
    table_data = []
    for row in datatable.find_all('tr'):
        row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)
 
    # Convert the data into a DataFrame
    df = pd.DataFrame(table_data)
 
    # Display the DataFrame
    print(df)
 
    # Save the DataFrame to a CSV file
    df.to_csv("reliable_profit_loss.csv", index=False)
    print("Profit & Loss data saved to 'reliable_profit_loss.csv'.")
else:
    print("Profit & Loss table not found on the page.")
    exit()
 
# Clean the data
df.replace(',', '', regex=True, inplace=True)
df.replace('%', '', regex=True, inplace=True)
 
# Assuming the first row is the header and the rest is data
df.columns = df.iloc[0]
df = df.drop(0).reset_index(drop=True)
 
# Convert columns to numeric, ignoring errors
df = df.apply(lambda x: pd.to_numeric(x, errors='coerce'))
 
# Fill NaN values with 0
df.fillna(0, inplace=True)
 
# Database connection parameters (retrieved from Vault or environment variables)
db_name = "concourse"
db_user = "concourse_user"
db_password = "concourse_pass"
db_host = "localhost"
db_port = "5432"
 
# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)
cursor = conn.cursor()
 
# Create table if not exists
create_table_query = '''
CREATE TABLE IF NOT EXISTS profit_loss (
    year TEXT,
    sales BIGINT,
    expenses BIGINT,
    operating_profit BIGINT,
    opm_percentage FLOAT,
    other_income BIGINT,
    interest BIGINT,
    depreciation BIGINT,
    profit_before_tax BIGINT,
    tax_percentage FLOAT,
    net_profit BIGINT,
    eps_in_rs FLOAT,
    dividend_payout_percentage FLOAT
);
'''
cursor.execute(create_table_query)
conn.commit()
 
# Insert data into the PostgreSQL table
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO profit_loss (
        year, sales, expenses, operating_profit, opm_percentage,
        other_income, interest, depreciation, profit_before_tax,
        tax_percentage, net_profit, eps_in_rs, dividend_payout_percentage
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    ''', tuple(row[:13]))  # Ensure the tuple matches the columns
 
conn.commit()
 
cursor.close()
conn.close()





















# v

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
 
# # URL of the webpage to scrape
# url = "https://www.screener.in/company/RELIABLE/consolidated/"
 
# # Send a GET request to the URL
# response = requests.get(url)
 
# # Check if the request was successful
# if response.status_code == 200:
#     print("Page retrieved successfully.")
# else:
#     print(f"Failed to retrieve page. Status code: {response.status_code}")
#     exit()
 
# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, "html.parser")
 
# # Scrape the "Profit & Loss" data
# # Finding the table that contains the "Profit & Loss" data
# profit_loss_table = soup.find("section", {"id": "profit-loss"})  # Adjust the selector as necessary
 
# if profit_loss_table:
#     # Extracting table rows
#     rows = profit_loss_table.find_all("tr")
 
#     # Extracting the header (year) and the data
#     headers = [th.text.strip() for th in rows[0].find_all("th")]
#     data = []
#     for row in rows[1:]:
#         cols = [td.text.strip() for td in row.find_all("td")]
#         data.append(cols)
 
#     # Convert the data into a DataFrame
#     df = pd.DataFrame(data, columns=headers)
 
#     # Display the DataFrame
#     print(df)
 
#     # Save the DataFrame to an Excel file
#     df.to_csv("reliable_profit_loss.csv", index=False)
#     print("Profit & Loss data saved to 'reliable_profit_loss.csv'.")
# else:
#     print("Profit & Loss table not found on the page.")