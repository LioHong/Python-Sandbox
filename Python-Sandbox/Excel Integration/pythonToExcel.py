"""
Name: pythonToExcel
Date: 20181130
Author: Lio Hong
Purpose: Create an excel spreadsheet using Python
Comments:
"""
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()

##import xlwt
##
##x=1
##y=2
##z=3
##
##list1=[2.34,4.346,4.234]
##
##book = xlwt.Workbook(encoding="utf-8")
##
##sheet1 = book.add_sheet("Sheet 1")
##
##sheet1.write(0, 0, "Display")
##sheet1.write(1, 0, "Dominance")
##sheet1.write(2, 0, "Test")
##
##sheet1.write(0, 1, x)
##sheet1.write(1, 1, y)
##sheet1.write(2, 1, z)
##
##sheet1.write(4, 0, "Stimulus Time")
##sheet1.write(4, 1, "Reaction Time")
##
##i=4
##
##for n in list1:
##    i = i+1
##    sheet1.write(i, 0, n)
##
##
##book.save("trial.xls")


##import xlsxwriter
##
##
### Create an new Excel file and add a worksheet.
##workbook = xlsxwriter.Workbook('demo.xlsx')
##worksheet = workbook.add_worksheet()
##
### Widen the first column to make the text clearer.
##worksheet.set_column('A:A', 20)
##
### Add a bold format to use to highlight cells.
##bold = workbook.add_format({'bold': True})
##
### Write some simple text.
##worksheet.write('A1', 'Hello')
##
### Text with formatting.
##worksheet.write('A2', 'World', bold)
##
### Write some numbers, with row/column notation.
##worksheet.write(2, 0, 123)
##worksheet.write(3, 0, 123.456)
##
### Insert an image.
##worksheet.insert_image('B5', 'logo.png')
##
##workbook.close()
