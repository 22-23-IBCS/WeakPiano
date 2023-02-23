def currency_converter(amount, from_currency, to_currency):
    exchange_rate = 0.0  # update this value with the latest exchange rate

    # convert 'amount' from 'from_currency' to 'to_currency' using the 'exchange_rate'
    converted_amount = amount * exchange_rate

    return converted_amount

# example usage
amount = 100
from_currency = "USD"
to_currency = "EUR"

converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
