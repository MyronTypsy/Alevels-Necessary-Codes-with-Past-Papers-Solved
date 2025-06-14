class Employee():
    #PRIVATE HourlyPay : REAL
    #PRIVATE EmployeeNumber : STRING
    #PRIVATE JobTitle : STRING
    #PRIVATE PayYear2022 : ARRAY[0:51] OF REAL
    def __init__(self, HourlyPayP,EmployeeNumberP, JobTitleP ):
        self.__HourlyPay = HourlyPayP
        self.__EmployeeNumber = EmployeeNumberP
        self.__JobTitle = JobTitleP
        self.__PayYear2022 = [0.0]*52
        
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self,WeekNo, HourNo):
        WeeklyPay = self.__HourlyPay* (HourNo)
        self.__PayYear2022[WeekNo-1] = WeeklyPay
    
    def GetTotalPay(self):
        TotalPay = 0
        for x in range(52):    
            TotalPay += (self.__PayYear2022[x])
        
        return TotalPay
    
class Manager(Employee):
    #PRIVATE BonusValue : REAL
    def __init__(self, HourlyPayP, EmployeeNumberP, JobTitleP, BonusValueP):
        super().__init__(HourlyPayP, EmployeeNumberP, JobTitleP)
        self.__BonusValue = BonusValueP
        
    def SetPay(self, WeekNo,HourNo):
        NewHours = HourNo + (HourNo*(self.__BonusValue/100))
        super().SetPay(WeekNo, NewHours)

#DECLARE EmployeeArray : Array[0:7] OF Employee
EmployeeArray = [Employee(0.0," "," ")]*8

MaybeBonusValue = ""
JobTitle = ""
try : 
    EmployeeFile = open("Employees.txt","r")
    for x in range(8):
        HourlyPays = float(EmployeeFile.readline().strip())
        EmployeeNumber = EmployeeFile.readline().strip()
        MaybeBonusValue = EmployeeFile.readline().strip()
        try:
            BonusValue = float(MaybeBonusValue)
            JobTitle = EmployeeFile.readline().strip()
            EmployeeArray[x] = Manager(HourlyPays,EmployeeNumber,JobTitle, BonusValue)
        except:
                JobTitle = MaybeBonusValue
                EmployeeArray[x] = Employee(HourlyPays,EmployeeNumber,JobTitle)
    EmployeeFile.close()
except IOError:
    print("file not found")
    
def EnterHours():
    try:
        HoursFile = open("HoursWeek1.txt", "r")
        for x in range(8):
            EmployeeID = HoursFile.readline().strip()
            Hours = float(HoursFile.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber() == EmployeeID:
                    EmployeeArray[y].SetPay(1,Hours)
        HoursFile.close()         
    except IOError:
        print("file not found")
        
EnterHours()
for x in range (8):
    EmployeeNumber = EmployeeArray[x].GetEmployeeNumber()
    TotalPay = EmployeeArray[x].GetTotalPay()
    print(EmployeeNumber + " "+ str(TotalPay))