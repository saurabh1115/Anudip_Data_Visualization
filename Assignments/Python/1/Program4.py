# calculate the simple intrest using function
def si(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

simple_interest = si(principal, rate, time)

print(f"The simple interest for principal {principal}, rate {rate}%, and time {time} years is: {simple_interest}")