# Define any constants or libraries that are needed in this library


def GetComm(WeeklySales):
    #Find and return the commission earned by an employee.
    
    #Or comm =0 and erase the comm=0 at the end
    if WeeklySales > 10000.00:
        Comm = WeeklySales * .02
    elif WeeklySales > 5000.00:
        Comm = WeeklySales * .01
    else:
        Comm = 0
    
    return Comm

def FindGrossPay(WeeklySales, Comm, BaseSalary):
    #Find the GrossPay using a draw against commission.
    
    if WeeklySales < 5000.00:
        Ded = (5000.00 - WeeklySales) * .10
        BaseSalary -= Ded
    GrossPay = BaseSalary + Comm
    
    return GrossPay
        