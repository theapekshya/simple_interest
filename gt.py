def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
time_period = float(input("Enter the time period (in years): "))

result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", result)
