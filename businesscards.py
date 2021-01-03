from faker import Faker
fake =Faker()

class BaseContact():
  def __init__(self,name, surname,mobile_phone_private,email):
    self.name=name
    self.surname=surname
    self.mobile_phone_private=mobile_phone_private
    self.email=email
  def __str__(self):
    return f"Wybieram number +48 {self.mobile_phone_private} i dzwonię do  {self.name} {self.surname}"
  def contact(self):
    print(f"Wybieram number +48 {self.mobile_phone_private} i dzwonię do  {self.name} {self.surname}")
 #def __len__(self):
    #return self.name
class BusinessContact(BaseContact):
  def __init__(self, name,surname,mobile_phone_private,email, position,company,mobile_phone):
    super(self.__class__,self).__init__(name,surname,mobile_phone_private,email)
    self.position=position
    self.company=company
    self.mobile_phone=mobile_phone
  def businesscontact(self):
    print(f"Wybieram number +48 {self.mobile_phone} i dzwonię do  {self.name} {self.surname}")
 
Karolina=BaseContact(name="Karolina",surname="Kuram",mobile_phone_private="564 879 786",email="kar.cho@o2.pl")

Agnieszka=BusinessContact(name="Agnieszka", surname="Jurfas",mobile_phone_private="456 879 786",email="aga.jur@o2.pl", mobile_phone="666 222 399",position="analyst", company="Aon")

print(Karolina.contact())
print(Agnieszka.businesscontact())


for i in range(3):
  print(fake.name())