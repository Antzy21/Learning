
def IncomeTax(YearlySalary):
    Tax = 0
    untaxedSalary = YearlySalary
    if untaxedSalary > 150000:
        Tax = (untaxedSalary - 150000) * .45
        untaxedSalary = 150000
    if untaxedSalary > 50000:
        Tax += (untaxedSalary - 50000) * .40
        untaxedSalary = 50000
    if untaxedSalary > 12500:
        Tax += (untaxedSalary - 12500) * .20
    return Tax

def NationalInsuranceTax(Salary):
    Tax = 0
    untaxedWeeklySalary = Salary/52
    if untaxedWeeklySalary > 962:
        Tax = (untaxedWeeklySalary - 962) * .02
        untaxedWeeklySalary = 962
    if untaxedWeeklySalary > 183:
        Tax = (untaxedWeeklySalary - 183) * .12
    return Tax*52

def ConvertToLondon(salary):
    """     
    Converts a non London Salary to an equivalent in London
    """
    print('Income Tax:',IncomeTax(salary))
    print('National Insurance Tax:',NationalInsuranceTax(salary))
    Tax = IncomeTax(salary) + NationalInsuranceTax(salary)
    print('Total Tax:',Tax)
    netIncome = salary - Tax
    print('\nMonthly:',netIncome/12, '\n')

ConvertToLondon(26500)
ConvertToLondon(29000)
ConvertToLondon(34000)
ConvertToLondon(36500)