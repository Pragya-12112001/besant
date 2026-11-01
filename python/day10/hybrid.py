class Employee:
  def work(self):
    return 'performs work'

class Developer(Employee):
  def code(self):
    return 'writes code'

class Trainer(Employee):
  def tech(self):
    return 'teaches student'

class Technical_Trainer(Developer, Trainer):
  pass

t = Technical_Trainer()
print(t.work())
print(t.code())
print(t.tech())