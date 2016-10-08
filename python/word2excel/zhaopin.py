#-*- coding: utf-8 -*-
import os
import os.path
import re
import win32com

from win32com.client import Dispatch

class easyExcel:
    """A utility to make it easier to get at Excel. Remembering
    to save the data is your problem, as is error handling.
    Operates on one workbook at a time."""

    def __init__(self, filename=None):
        if not hasattr(self, 'xlApp'):
            self.xlApp = win32com.client.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ""

    def save(self, newfilename=None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()

    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def setCell(self, sheet, row, col, value):
        sht = self.xlBook.Worksheets(sheet)
        #sht.Cells(row, col).Value = value
        my_col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O']
        #字符串格式化,A1,A2
        my_range = "%s%s" % (my_col[col], row)
        #print my_range
        sht.Range(my_range).Value = value

    def quit(self):
        self.xlApp.Quit()
        
 class easyWord:
    def __init__(self, filename=None):
        if not hasattr(self, 'xlApp'):
            self.xlApp = win32com.client.Dispatch('Word.Application')
            self.xlApp.Visible = 0
            self.xlApp.DisplayAlerts = 0
        if filename:
            self.filename = filename
            self.xlDoc = self.xlApp.Documents.Open(
                FileName=filename, Encoding='gb18030')

    def quit(self):
        self.xlApp.Quit()
        
        
  def read_doc(path):
    if USE_DATE is None or path.find(USE_DATE) == -1:
        return
    wd = None
    wd = easyWord(filename=path)
    try:
        if wd.xlDoc.Content.End <= 0:
            return

        out = wd.xlDoc.Range(wd.xlDoc.Content.Start, wd.xlDoc.Content.End)
        text = unicode(out())

        zhilian(path, text)
        liepin(path, text)
    except Exception as e:
        print "Exception: ", e
    finally:
        if wd is not None:
            wd.quit()
            
            
  my_school.split('\r', 3)
  re.split('\xa0\xa0', tmp_school)
