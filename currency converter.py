print("----- CURRENCY CONVERTER -----")

rates = {
    "USD": 1.00,      # Base
    "EUR": 0.92,
    "GBP": 0.78,
    "ZAR": 18.50
}

def convert(amount, from_curr, to_curr):
    # Convert from original currency into USD, then into new currency
    usd_amount = amount / rates[from_curr]
    return usd_amount * rates[to_curr]

print("Available currencies: USD, EUR, GBP, ZAR")

from_curr = input("Convert FROM (e.g. USD): ").upper()
to_curr = input("Convert TO (e.g. ZAR): ").upper()
amount = float(input("Amount: "))

if from_curr in rates and to_curr in rates:
    result = convert(amount, from_curr, to_curr)
    print(f"\n{amount} {from_curr} = {round(result, 2)} {to_curr}")
else:
    print("Invalid currency code!")