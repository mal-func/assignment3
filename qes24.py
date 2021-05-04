class college:
  nm_of_clg="UEM"
  pincd="303807"
  add="Gurukul, Sikar Road Near Udaipuria Mod, Jaipur, Rajasthan"

  def initialize(self):
    print("Enter departments details")
    self.dep=input("enter department: ")
    self.incharge=input("enter incharge: ")
  
  @staticmethod
  def stdisplay(self):
    print(f'Name of the college: {college.nm_of_clg}\nAddress: {college.add}\nPincode: {college.pincd}')

  def display(self):
    print(f'Department: {self.dep},Incharge: {self.incharge}')
  



class company:

  def __init__(self):
    print("Enter company details")
    self.nm_of_cmp=input("enter name of company: ")
    self.no_se=int(input("enter the number of software engineers: "))
    self.amt_inv=int(input("enter the amount invested: "))

  def display(self):
    print(f'Name Of company: {self.nm_of_cmp},No. of softawre engineers: {self.no_se}')
