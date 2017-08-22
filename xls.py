import xlrd
import unicodecsv
def xls2csv (xls_filename, csv_filename):
   # Converts an Excel file to a CSV file.
   # If the excel file has multiple worksheets, only the first worksheet is converted.
   # Uses unicodecsv, so it will handle Unicode characters.
   # Uses a recent version of xlrd, so it should handle old .xls and new .xlsx equally well.
   wb = xlrd.open_workbook(xls_filename)
   sh = wb.sheet_by_index(0)
   fh = open(csv_filename,"wb")
   csv_out = unicodecsv.writer(fh, encoding='utf-8')
  # for row_number in xrange (sh.nrows):
   #    csv_out.writerow(sh.row_values(row_number))


   for i in range(1, sh.nrows):
      #  row = sh.row_slice(i)
      #  Gname = row[0].value
       # Fname = row[1].value
        #Lname = row[2].value
        for j in range(0, sh.ncols):
            col = sh.col_slice(j)
            Gn=col[0].value
            Fn=col[1].value
          #  print  Gn, Fn
            if j==1:
              print i, Gn, Fn


          #  print  Fn
           # print Lname

xls2csv ("Copy.xls","output.csv")
