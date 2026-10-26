def total_prices(*prices):
  # return sum(prices)
  total = 0
  for i in prices:
    total += i
  return total

print(total_prices(120, 34, 46, 70))

# conversts extra arguments into a tuple  
