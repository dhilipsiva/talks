import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')  # Create an new Excel file and add a worksheet.
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)  # Widen the first column to make the text clearer.
bold = workbook.add_format({'bold': True})  # Add a bold format to use to highlight cells.
worksheet.write('A1', 'Hello')  # Write some simple text.
worksheet.write('A2', 'World', bold)  # Text with formatting.
worksheet.write(2, 0, 123)  # Write some numbers, with row/column notation.
worksheet.write(3, 0, 123.456)
worksheet.insert_image('B5', 'logo.png')  # Insert an image.
workbook.close()
