import openpyxl
from random import randint, uniform

# Function to generate random product names
def generate_product_name():
    products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Keyboard", "Mouse", "Monitor", "Camera", "Speaker"]
    return products[randint(0, len(products) - 1)]

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Write headers to the sheet
sheet['A1'] = 'ID'
sheet['B1'] = 'Name'
sheet['C1'] = 'Quantity'
sheet['D1'] = 'Price'

# Generate and write sales data for 100 rows
for row in range(2, 102):
    sheet[f'A{row}'] = row - 1  # ID
    sheet[f'B{row}'] = generate_product_name()  # Name
    sheet[f'C{row}'] = randint(1, 10)  # Quantity (1 to 10)
    sheet[f'D{row}'] = round(uniform(100, 1000), 2)  # Price (random between 100 and 1000)

# Save the workbook to a file
file_path = r'C:\work\sales.xlsx'
wb.save(file_path)

print(f"Sales list has been generated and saved to {file_path}")
