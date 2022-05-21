import keyboard
import sys
# import CurrencyExchange
import requests

a=13
r=range(8,12)
if a in r:
    print("within")
else:
    print("not")
quit(0)

api_key = "37029bdc415426523c2d80c9"
# Where USD is the base currency you want to use
url1 = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
print('url1:', url1)
url2 = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/USD/ILS'
print('url2:', url2)
# Making our request
response = requests.get(url2)
data = response.json()
# Your JSON object
print("data:\n", data)
print("conversion_rate:", data["conversion_rate"])

quit(0)
# =======
currency = CurrencyExchange.Currency()
print(currency.convertCurrency(1, 'USD', 'EUR'))
# print("rate is:", c)
print(currency.validateCurrencyCode('USD'))
# Check to see if USD is a valid currency code
# if (not currency.validateCurrencyCode('USD')) and (not currency.validateCurrencyCode('NIS')):
#     print("Something wrong with the currency codes. Please check!")
quit(0)
# =========
in1 = input("what? > ")
lst1 = [12, 13, 1]
total_numbers = len(lst1)
total_chars = len(str(lst1)) + 1
#
print("This is my list. Remember it!")
print(lst1, end="")
event = keyboard.read_event()
#
print("\b"*total_chars, "? "*total_numbers)

# if event.event_type == keyboard.KEY_DOWN:
#     key = event.name
#     print(f'Pressed: {key}')
#     if key == 'q':
#         break
# sys.stdout.write('\x1b[1A')

