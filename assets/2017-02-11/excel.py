from xlsxwriter import Workbook

"""
class Workbook:
    def __init__(self, file_name):
        self.file_name = file_name
"""

workbook = Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Hello')
worksheet.write('A2', 'World', bold)
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
# worksheet.insert_image('B5', 'logo.png')
workbook.close()
