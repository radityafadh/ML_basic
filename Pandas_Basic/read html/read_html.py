import pandas as pd
import urllib.request

url = "https://pokemondb.net/pokedex/dialga"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

try:
    # Fetch HTML with custom headers
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    # Parse all HTML tables
    tables = pd.read_html(html)

    # Print number of tables found
    print(f"Total tables found: {len(tables)}\n")

    # Loop through each table and display its content
    for i, table in enumerate(tables, 1):
        print(f"=== Table {i} ===")
        print(table.head())  # Show first 5 rows
        print("\nColumns:", table.columns.tolist())  # Show column names
        print("-" * 50 + "\n")

except Exception as e:
    print(f"Error: {e}")