class Employee():
    #PRIVATE Hourlpay : REAL
    #PRIVATE EmployeeNumber : STRING
    #PRIVATE JobTitle : STRING
    #PRIVATE PayYear2022 : ARRAY[0:51] OF REAL
    
    def __init__(self, HourlyPayP, EmployeeNumberP,
                 JobTitleP):
        self.__HourlyPay = HourlyPayP
        self.__EmployeeNumber = EmployeeNumberP
        self.__JobTitle = JobTitleP
        self.__PayYear2022 = [0]
        for x in range(0,52):
            self.__PayYear2022 = [0.0 for _ in range(52)]
            
    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    
    def SetPay(self, WeekNo, HoursWorked):
        calc = self.__HourlyPay * HoursWorked
        self.__PayYear2022[WeekNo -1 ] = calc
        
    def GetTotalPay(self):
        total = 0
        for y in range(52):
            total = total + self.__PayYear2022[y] 
        return total    

class Manager(Employee):
    #PRIVATE BonusValue : REAL
    def __init__(self, HourlyPayP, EmployeeNumberP, JobTitleP, BonusValueP):
        super().__init__(HourlyPayP, EmployeeNumberP, JobTitleP)
        self.__BonusValue = BonusValueP
    
    def SetPay(self, WeekNo, HoursWorked):
        NewHours = HoursWorked + (HoursWorked* (self.__BonusValue/100)) 
        super().SetPay(WeekNo, NewHours)

EmployeeArray = [Employee(0.0, "", "")]*8

MaybeBonus = " "
JobTitle = " "
try:
    EmployeeFile = open("Employees.txt", "r")
    for x in range(8):
        hourlyPay = float(EmployeeFile.readline().strip())
        EmployeeNumber = EmployeeFile.readline().strip()
        MaybeBonus = EmployeeFile.readline().strip()
        try:
            Bonus = float(MaybeBonus)
            JobTitle = EmployeeFile.readline().strip()
            EmployeeArray[x]= Manager(hourlyPay, EmployeeNumber, JobTitle,Bonus )
        except:
            JobTitle = MaybeBonus
            EmployeeArray[x] = Employee(hourlyPay, EmployeeNumber, JobTitle)

    EmployeeFile.close()       
except IOError:
    print("file not found")
    
def EnterHours():
    try:
       HoursFile = open("HoursWeek1.txt", "r")
       for s in range(8):
            EmployeeNo = HoursFile.readline().strip()
            HoursWorked =  HoursFile.readline().strip()
            for z in range(8):
                EmpObject = EmployeeArray[z]
                if  EmpObject.GetEmployeeNumber() == EmployeeNo :
                    EmployeeArray[z].SetPay(1, HoursWorked)
            HoursFile.close()           
    except IOError():
        print("file not found")
        exit()
EnterHours()
for x in range(8):
    EmployeeNumber = EmployeeArray[x].GetEmployeeNumber()
    TotalPay = EmployeeArray[x].GetTotalPay()
    print(EmployeeNumber , " ", str(TotalPay))