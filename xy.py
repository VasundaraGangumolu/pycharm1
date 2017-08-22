import xlrd
import unicodecsv
def xls2csv (xls_filename, csv_filename):
   wb = xlrd.open_workbook(xls_filename)
   sh = wb.sheet_by_index(0)
   fh = open(csv_filename,"wb")
   csv_out = unicodecsv.writer(fh, encoding='utf-8')
   for row_number in xrange (sh.nrows):
       print sh.cell(row_number,0)
   for col_number in xrange (sh.ncols):
       print sh.cell(col_number,0)
      # csv_out.writerow(sh.row_values(row_number))
   fh.close()

xls2csv ("Copy.xls","output.csv")
