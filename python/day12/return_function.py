def make_tax_calculator(rate):
  def claculate(price):
    return price + (price * rate/100)
  return claculate

gst_18 = make_tax_calculator(18)
gst_5 = make_tax_calculator(5)

print(gst_18(1000))
print(gst_5(1000))