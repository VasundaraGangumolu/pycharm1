import xlrd
import datetime
import unicodecsv
def xls2csv (xls_filename, csv_filename):
   wb = xlrd.open_workbook(xls_filename)
   sh = wb.sheet_by_index(0)
   fh = open(csv_filename,"wb")
   csv = unicodecsv.writer(fh, encoding='utf-8')
   row = sh.row(1)
   row1 = sh.row(0)
   row2 = sh.row(10)
   row3 = sh.row(11)
   row4 = sh.row(19)
   row5 = sh.row(20)
   row6 = sh.row(29)
   row7 = sh.row(30)
   fh.write("Assigned, Month, TicketsOpened")
   fh.write("\n")
   for idx, cell_obj1 in enumerate(row1):
            for i, cell_obj in enumerate(row):
                if i==idx and i!=0:
                     a1_tuple = xlrd.xldate_as_tuple(row1[i].value, wb.datemode)
                     a1_datetime = datetime.datetime(*a1_tuple)
                     fh.write("%s,%s,%s" % (row1[0].value, a1_datetime.strftime("%b-%y"), row[i].value))
                     fh.write("\n")
   for idx, cell_obj1 in enumerate(row2):
               for i, cell_obj in enumerate(row3):
                    if i == idx and i!= 0:
                         a1_tuple = xlrd.xldate_as_tuple(row2[i].value, wb.datemode)
                         a1_datetime = datetime.datetime(*a1_tuple)
                         fh.write("%s,%s,%s" % (row2[0].value, a1_datetime.strftime("%b-%y"), row3[i].value))
                         fh.write("\n")
   for idx, cell_obj1 in enumerate(row4):
                for i, cell_obj in enumerate(row5):
                     if i == idx and i!= 0:
                          a1_tuple = xlrd.xldate_as_tuple(row4[i].value, wb.datemode)
                          a1_datetime = datetime.datetime(*a1_tuple)
                          fh.write("%s,%s,%s" % (row4[0].value,a1_datetime.strftime("%b-%y"), row5[i].value))
                          fh.write("\n")
   for idx, cell_obj1 in enumerate(row6):
                 for i, cell_obj in enumerate(row7):
                      if i == idx and i!= 0:
                        a1_tuple = xlrd.xldate_as_tuple(row6[i].value, wb.datemode)
                        a1_datetime = datetime.datetime(*a1_tuple)
                        fh.write("%s,%s,%s" % (row6[0].value,a1_datetime.strftime("%b-%y"),row7[i].value))
                        fh.write("\n")
   fh.close()

xls2csv ("Copy.xls","output1.csv")
