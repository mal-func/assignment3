class student:
 
  def getData(self,id,name,department):
    self.id=id
    self.name=name
    self.dept=department
    string = 'id: '+str(id)+' name: '+name+' department: '+department
    return string
    
id=int(input('Enter the id '))
name=input('Enter the name ')
department=input('Enter the department ')
ob=student()
print(ob.getData(id,name,department))
