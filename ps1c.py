starting_salary = float(input("enter your starting_salary:"))

total_cost = 1000000 #the total cost of your dream house 

semi_annual_raise = .07

r = 0.04 #annual return of invesments
down_payment = 0.25 * total_cost
no_of_steps = 0 #noof bisection steps involved 
x1 = 0 
x2 = 10000
current_savings = 0
avg = (x1 + x2 )// 2 #integer division

epsilon = 100 #the range with which downpayment should not increase'


while abs(current_savings - down_payment)>= epsilon:
    if x2 == starting_salary:
        break
    current_savings = 0
    annual_sallary = starting_salary
    rate = avg / 10000

    for months in range(0, 37):
        
            if months % 6 == 0:
                annual_sallary += annual_sallary * semi_annual_raise
            additional_savings = current_savings * r/12
            monthly_sallary = annual_sallary/ 12
            current_savings += additional_savings + monthly_sallary * rate
    
    if current_savings < down_payment:
        x1 = avg
    else:
        x2 =avg 
    no_of_steps += 1
    avg = ( x1 + x2 )// 2
if x2 == starting_salary:
    print("not possible")
else:
        
    print("best saving rate :" ,  rate)
    print("no of bisection steps :",  no_of_steps)