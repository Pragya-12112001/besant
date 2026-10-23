def rec_area(length, width):
  return length * width

print(rec_area(10, 12))


def total_cost(price, quant):
  return price * quant

print(total_cost(230, 4))


def discounted_bill(amount, discount = 10):
  return amount - (amount * discount/100)

discounted_bill(1000)


def electricity_bill(units):
  amount = units*8
  if amount <= 100:
    return f'no service charge till as your amount is {amount}'
  return f'final amount {amount}'

print(electricity_bill(14))