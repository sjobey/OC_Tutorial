import csv
from itertools import groupby
import math
import  SGHUtilities as Utils
import SGHCalculations as Calcs

#Path to file
pathSAPOutput = r'I:/BOS/Users/SGHComputationalTeam/Projects_WIP/Kendall MIT/SAP_TEST.csv'
pathAISC = r'I:/BOS/Users/SGHComputationalTeam/SharedPython/SAP_Utilities/aisc-shapes-database-v15.0.xlsx'


"""
with open(path, 'r') as f:
    data = list(csv.reader(f, delimiter = ','))
    #print(data[:1])
    highest = SAPUtilities.maxDCR(data,0, 17)
    SAPUtilities.writeCSV(highest,'C:/Users/chsjoberg/Documents/Python Scripts/MITK_DCR_Test.csv')
"""

asicData = list(Utils.ExcelReader(pathAISC,1))

lightest = Utils.GetLightestShapeAISC(asicData, 1000, 'W')

print('Lightest Shape: ', lightest['EDI_Std_Nomenclature'])
