def rec_area(length, width):
  return length * width

length = 12
width = 14
print('area of rectangle: ', rec_area(length, width))


def total_cost(price, quant):
  return price * quant

price = 230
quant = 4
print('total price: ', total_cost(price, quant))


def discounted_bill(amount, discount = 10):
  return amount - (amount * discount//100)

amount = 1200
print('discounted bill: ', discounted_bill(amount))
print('discounted bill: ', discounted_bill(amount, discount=12))


def electricity_bill(units, rate = 8):
  amount = units * rate
  service_charge = 100

  return f'final amount {amount + service_charge}'

units = 15
print('total electricity bill: ', electricity_bill(units))