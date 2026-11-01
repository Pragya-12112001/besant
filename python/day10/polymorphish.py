class CashPayment:
  def pay(self):
    print('cash Paayment')

class UpiPayment:
  def pay(self):
    print('UPI Paayment')

def process(payment):
  payment.pay()
  
process(CashPayment())