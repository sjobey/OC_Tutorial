import csv
from itertools import groupby
import math
import xlrd, mmap
import mmap
import xlrd 


def ExcelReader(filePath, sheet_index=0):
    """Reads a .xlsx file and returns a list of dictionaries"""
    with open(filePath, 'r') as f:
        book    = xlrd.open_workbook(file_contents=mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ))
        sheet   = book.sheet_by_index(sheet_index)
        headers = dict( (i, sheet.cell_value(0, i) ) for i in range(sheet.ncols) ) 
        return list( dict( (headers[j], sheet.cell_value(i, j)) for j in headers ) for i in range(1, sheet.nrows) )


def CSVReader(filePath):
    """Reads a csv file and returns a list of dictionaries"""
    with open(filePath, 'r') as f:
        data = list(csv.DictReader(f, delimiter = ','))
        return data


def GetMinShapeByZx(aiscData, minZx, prefix = None):
    """Gets the minimum section from AISC table data that has at least the Zx provided, and begins with the provided prefix"""
    sortedZx = sorted(aiscData, key = lambda x:float(x['Zx']))
    for shape in sortedZx:
        if shape['Zx'] > minZx:
            if prefix is None:
                return shape
            elif(shape['AISC_Manual_Label'].startswith(prefix)):
                return shape
    raise ValueError('No shape was found with the provided criteria')



def MaxDCR(data,name, dcr, skips = 1):
    """Gets the controling dcr case for each frame in the dataset."""
    data = data[skips:]
    rows = []
    for key, group in groupby(data, lambda x: x[name]):
        g = list(group)
        sLast = sorted(g, key = lambda x:float(x[dcr]))
        maxDCRRow = dict(sLast[-1])
        rows.append(maxDCRRow)
    return rows


def WriteCSVFromList(data, name, headerRow = []):
    """Writes a .csv file from a list of lists"""
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',',lineterminator = '\n')
        if len(headerRow) > 0:
            writer.writerow(headerRow)
        for s in data:
            writer.writerow(s)
        print("CSV Write Complete.")


def WriteCSVFromDict(data, name):
    """Writes a .csv file from a Dictionary"""
    headerRow = list(data[0].keys())
    with open(name, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',',lineterminator = '\n')
        if len(headerRow) > 0:
            writer.writerow(headerRow)
        for s in data:
            r = [s[k] for k in headerRow]
            writer.writerow(r)
        print("CSV Write Complete.")



if __name__ == "__main__":
        print("Main")
