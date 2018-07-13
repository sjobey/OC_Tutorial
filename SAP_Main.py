import SGHUtilities as Utils
import SGHCalculations as Calcs

#Path to files
pathSAPOutput = r'I:/BOS/Users/SGHComputationalTeam/Projects_WIP/Kendall MIT/SAP_TEST.csv'
pathAISC = r'I:/BOS/Users/SGHComputationalTeam/SharedPython/SAP_Utilities/aisc-shapes-database-v15.0.xlsx'

"""
# Example 1

sapData = Utils.CSVReader(pathSAPOutput)
highest = Utils.MaxDCR(sapData,'Name','TotalDCR')
Utils.WriteCSVFromDict(highest,'C:/Users/chsjoberg/Documents/Python Scripts/MITK_DCR_Test.csv')
"""


# Example 2
Ma = 80*12 #kip inches
Fy = 50 #ksi

minZx = Calcs.MinimumZx(Ma, Fy)
print('Minimum Zx: ', minZx)

asicData = Utils.ExcelReader(pathAISC,1)
lightest = Utils.GetMinShapeByZx(asicData, minZx, 'W')

print('Minimum Shape: ', lightest['AISC_Manual_Label'])






