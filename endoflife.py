import json
import urllib3
from openpyxl import Workbook
from tqdm import tqdm  # Import tqdm for the progress bar

# Disable warnings for certificate verification (for simplicity, not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Step 1: Make a request to https://endoflife.date/api/all.json
all_products_url = "https://endoflife.date/api/all.json"
http = urllib3.PoolManager()
response_all_products = http.request('GET', all_products_url)

# Check if the request was successful (status code 200)
if response_all_products.status == 200:
    # Parse the JSON response
    all_products_data = json.loads(response_all_products.data.decode('utf-8'))

    # Set the export path
    export_path = 'output.xlsx'

    # Create an Excel workbook and get the active sheet
    wb = Workbook()
    ws = wb.active

    # Add headers to the Excel sheet
    ws.append(['Product', 'Cycle', 'EOL'])

    # Step 2: Iterate over the products and make individual requests
    for product in tqdm(all_products_data, desc="Exporting", unit="product"):
        # Make a request to https://endoflife.date/api/{product}.json
        product_url = f"https://endoflife.date/api/{product}.json"
        response_product = http.request('GET', product_url)

        # Check if the request was successful (status code 200)
        if response_product.status == 200:
            # Parse the JSON response
            json_output = json.loads(response_product.data.decode('utf-8'))

            for entry in json_output:
                cycle_value = entry.get('cycle')
                eol_value = entry.get('eol')

                # Add data to the Excel sheet
                ws.append([product, cycle_value, eol_value])
        else:
            print(f"Error fetching data for {product}. Status code: {response_product.status}")

    # Save the Excel file
    wb.save(export_path)

    # Print the export path
    print(f"Exported data to: {export_path}")

else:
    print(f"Error fetching all products data. Status code: {response_all_products.status}")
