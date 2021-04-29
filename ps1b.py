#Saving, with a raise
annual_salary = float(input("kindly Enter your annual sallary  : "))

#portion_saved is the certain amount of salary you saved for payment
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ​")) 

#the total cost of your dream house  
total_cost = float(input("Enter the cost of your dream home: ​"))

semi_annual_raise = float(input("Enter the semi annual raise , as a decimal:"))

portion_down_payment = 0.25 * total_cost

current_savings = 0 #the amount you have saved

months = 0 #nno. of months to save money to make down_payment


r = 0.04 #investments earn a Annual return of r


while current_savings < portion_down_payment:
    monthly_sallary  = annual_salary / 12
    
    monthly_return = (monthly_sallary) * portion_saved #additional savings at end of month to put in saving
    additional_savings = (current_savings*r/12)
    
    current_savings += monthly_return + additional_savings
    
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print("No. of month :" , months)
