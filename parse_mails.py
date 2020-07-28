import openpyxl
from pathlib import Path

xlsx_file = Path('.', 'Recruiter-emails.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file) 

# Read the active sheet:
sheet = wb_obj.active

data = []

for i, row in enumerate(sheet.iter_rows(values_only=True)):
    name = None
    if row[0] != None and row[1] != None:
        if row[2] != None: name = row[2][:row[2].find('[')]
        data.append({"company":row[0], "email":row[1], "name":name})