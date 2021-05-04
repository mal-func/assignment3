class excep:
  def func(self):

      self.num=float(input("Enter the numerator: "))
      self.den=float(input("Enter the denominator: "))

  def div(self):
    
    try:
      div=self.num/self.den
      print(div)
    except ZeroDivisionError:
      print("denominator cant be zero")
    
ob=excep()
ob.func()
ob.div()
