import csv
from itertools import groupby
import math
import xlrd, mmap
import mmap
import xlrd 


def ExcelReader(filePath, sheet_index=0):
    with open(filePath, 'r') as f:
        book    = xlrd.open_workbook(file_contents=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ))
        sheet   = book.sheet_by_index(sheet_index)
        headers = dict( (i, sheet.cell_value(0, i) ) for i in range(sheet.ncols) ) 
        return ( dict( (headers[j], sheet.cell_value(i, j)) for j in headers ) for i in range(1, sheet.nrows) )


def Get_CSV_Data(filePath):
    with open(filePath, 'r') as f:
        data = list(csv.DictReader(f, delimiter = ','))
        print(data[:10])
        return data


def GetLightestShapeAISC(aiscData, minZx, prefix = None):
    sortedZx = sorted(aiscData, key = lambda x:float(x['Zx']))
    for shape in sortedZx:
        if shape['Zx'] > minZx:
            if prefix is None:
                return shape
            elif(shape['AISC_Manual_Label'].startswith(prefix)):
                return shape
    raise ValueError('No shape was found with the provided criteria')



def maxDCR(data,nameIndex, dcrIndex, skips = 1):
    """Docstring Test"""
    headers = data[0]
    data = data[skips:]
    rows = []
    rows.append(headers)
    for key, group in groupby(data, lambda x: x[nameIndex]):
        g = list(group)
        sLast = sorted(g, key = lambda x:float(x[dcrIndex]))
        maxDCRRow = sLast[-1]
        rows.append(maxDCRRow)
    
    return rows


def writeCSV(data, name, headerRow = []):
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',',lineterminator = '\n')
        if len(headerRow) > 0:
            writer.writerow(headerRow)
        for s in data:
            writer.writerow(s)
        print("CSV Write Complete.")



if __name__ == "__main__":
        print("Main")
