import xlrd
import datetime
import unicodecsv
def xls2csv (xls_filename, csv_filename):
   wb = xlrd.open_workbook(xls_filename)
   sh = wb.sheet_by_index(0)
   fh = open(csv_filename,"wb")
   csv = unicodecsv.writer(fh, encoding='utf-8')
   for i in range(sh.nrows):
      for j in range(sh.ncols):
         if sh.cell(0,0).value=='LQ DSL':
             print sh.cell(0,0+1).value
         if sh.cell(10,0).value=='LQ ETH':
             print sh.cell(10,0+1).value
       #for i, cell1 in enumerate(sh.ncols):
        #   if i==idx:
         #      print cell
          #     print ("%s %s" % (cell[0].value,cell1[2].value))

   fh.close()

xls2csv ("Copy.xls","sg.csv")
