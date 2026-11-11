prices = {'pen': 10, 'book': 20, 'bag': 56}
double_prices = {}
for key, value in prices.items():
  double_prices[key] = value*2
print(double_prices)

dict_comp = {key: value * 2 for key, value in prices.items()}
print(dict_comp)