# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

stateTax = salary * 0.065
federalTax = salary * 0.280
dependentDeduction = round(salary * (0.025 * numDependents),1)
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print ('State Tax: $' + str(stateTax))
print ('Federal Tax: $' + str(federalTax))
print ('Dependents: $' + str(dependentDeduction))
print("Salary: $" + str(salary))
print ('Take-Home Pay: $' + str(takeHomePay))



