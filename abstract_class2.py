from abc import ABC, abstractmethod

class Employee(ABC):
	def __init__(self,name,surname,social_security_number):
		self.name=name
		self.surname=surname
		self.social_security_number=social_security_number
	@abstractmethod
	def earnings(self):
		pass
    
       
print("------------------------------------------------------------------------")		
		   
class SalariedEmployee(Employee):
	def __init__(self,name,surname,social_security_number,salary):
		super().__init__(name,surname,social_security_number )
		self.salary=salary
	def earnings(self):
		      return self.salary
print("------------------------------------------------------------------------") 

class HourlyEmployee (Employee):
   def __init__(self,name,surname,social_security_number,hourlywage,hoursworked):
	     super().__init__(name,surname,social_security_number )
	     self.hourlywage=hourlywage
	     self.hoursworked=hoursworked
   def earnings(self):
		      return self.hourlywage* self.hoursworked
	     
	     
print("------------------------------------------------------------------------") 

class CommissionEmployee (Employee):
 def __init__(self,name,surname,social_security_number,sales,rate):
          super().__init__(self,name,surname,social_security_number ) 
          self.sales=sales
          self.rate=rate  
print("------------------------------------------------------------------------") 
print("------------------------------------------------------------------------") 

class BasePlusCommissionEmployee(CommissionEmployee ):
  def __init__(self,name,surname,social_security_number,sales,rate,salary):
   super().__init__(self,name,surname,social_security_number, sales,rate ) 
   self.salary=salary 
print("------------------------------------------------------------------------") 
print("SalariedEmployee's earnings")
s =SalariedEmployee( "John", "Smith", "111-11-1111",3000)

print(s.earnings())
print("------------------------------------------------------------------------")
print("HourlyEmployee's earnings")

h=  HourlyEmployee("Johnny", "Brown", "111-11-112222",3,10 )
print(h.earnings())   










