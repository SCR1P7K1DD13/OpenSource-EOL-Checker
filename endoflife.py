import json
import aiohttp
import asyncio
from openpyxl import Workbook
from tqdm import tqdm
import requests
import logging
import warnings

# Suppress warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)

# Suppress RequestsDependencyWarning
warnings.filterwarnings("ignore", category=requests.exceptions.RequestsDependencyWarning)

async def fetch_product(session, product):
    product_url = f"https://endoflife.date/api/{product}.json"
    async with session.get(product_url, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Error fetching data for {product}. Status code: {response.status}")
            return None

async def main():
    all_products_url = "https://endoflife.date/api/all.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(all_products_url, ssl=False) as response_all_products:
            if response_all_products.status == 200:
                all_products_data = await response_all_products.json()

                export_path = 'output.xlsx'
                wb = Workbook()
                ws = wb.active
                ws.append(['Product', 'Cycle', 'EOL'])

                tasks = []
                for product in tqdm(all_products_data, desc="Exporting", unit="product"):
                    tasks.append(fetch_product(session, product))

                results = await asyncio.gather(*tasks)

                for product, result in zip(all_products_data, results):
                    if result:
                        for entry in result:
                            cycle_value = entry.get('cycle')
                            eol_value = entry.get('eol')
                            ws.append([product, cycle_value, eol_value])

                wb.save(export_path)
                print(f"Exported data to: {export_path}")
            else:
                print(f"Error fetching all products data. Status code: {response_all_products.status}")

if __name__ == "__main__":
    asyncio.run(main())
