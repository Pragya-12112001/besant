# allows function to accept any number of arguments
# in dictionary format
def food_order(**order):
  for key, value in order.items():
    print(f"{key} : {value}")

food_order(dish='dosa', quantity=2, price=120)

print('-------------------')

food_order(dish='biryani', quantity=1, spice_level='medium', takeaway=True)