#Keoni Decipulo
#P4HW2
#4/28/24
#Program asking for multiple employer's names, hours and pay rate to respond with
#their pay and gross pay, plus overtime pay if they worked over 40 hours with an
#1.5 mulitiplier increase from their regular pay rate. Adds up tota paid amount and hours
#for all employees.
#Initialize variables to hold totals
overtime_total = regular_pay_total = gross_pay_total = 0
num_employees = 0

# Input employee name
name = input("Enter employee name or 'Done' to terminate:")

# Begin the loop to input employee data
while name.lower() != 'done':
    # Input pay rate and hours worked
    pay_rate = float(input("Enter pay rate: "))
    hours = float(input("Enter hours worked: "))

    # Calculate regular pay and overtime pay
    if hours>40:
# Calculate overtime hours and pay               
        OT=hours-40
        OTpay=OT*(pay_rate*1.5)
#Calculate regular pay
        reg_pay= 40*pay_rate
#Calculate gross pay
        gross_pay = reg_pay+OTpay
    else:
        OT=0
        OTpay=0
#calculate reg pay if there is no overtime
        reg_pay = hours*pay_rate
        gross_pay = reg_pay
                
    print('Hourse Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print(f'{hours}          {pay_rate}          {OT}       ${OTpay}        ${reg_pay}      ${gross_pay}')      

    # Update totals
    regular_pay_total += reg_pay
    overtime_total += OTpay
    gross_pay_total += gross_pay
    num_employees += 1

    # Input next employee name
    name = input("Enter another employee name or 'Done' to terminate: ")

# Display results
print("\nEmployee Payroll Summary:")
print("========================")
print(f"Total number of Employees: {num_employees}")
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${regular_pay_total:.2f}")
print(f"Total amount paid for gross: ${gross_pay_total:.2f}")

