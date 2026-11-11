employee_name = input("Employee:")
hourly_rate = float(input("Hourly rate: "))
hours_worked = int(input("Hours worked: "))
monthly_salary = (hourly_rate*hours_worked)

print(f"Employee: {employee_name}")
print(f"Hourly rate: {hourly_rate} MAD")
print(f"Hours worked {hours_worked}")
print(f"Monthly salary: {monthly_salary} MAD")