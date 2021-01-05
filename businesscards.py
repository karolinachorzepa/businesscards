from faker import Faker
import random
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
  def label_lenght(self):
    return len(self.name) + len(self.surname)
class BusinessContact(BaseContact):
  def __init__(self, name,surname,mobile_phone_private,email, position,company,mobile_phone):
    super(self.__class__,self).__init__(name,surname,mobile_phone_private,email)
    self.position=position
    self.company=company
    self.mobile_phone=mobile_phone
  def businesscontact(self):
    print(f"Wybieram number +48 {self.mobile_phone} i dzwonię do  {self.name} {self.surname}")
 
Karolina=BaseContact(name="Karolina",surname="Chorzepa",mobile_phone_private=564879786,email="kar.cho@o2.pl")
Klaudia=BaseContact(name="Klaudia",surname="Klosek",mobile_phone_private=768900786,email="kla.klo@o2.pl")
Agnieszka=BusinessContact(name="Agnieszka", surname="Jurfas",mobile_phone_private=456879786,email="aga.jur@o2.pl", mobile_phone=666222399,position="analyst", company="Aon")
Mariusz=BusinessContact(name="Mariusz", surname="Micalek",mobile_phone_private=767898900,email="mar.mic@o2.pl", mobile_phone=645222870,position="analyst", company="Aon")

for i in range(1):
  print(fake.name())

  def create_contacts():
    for t in range(10):
      print(f"Business card {fake.name()} in amount: {fake.random_int(0, 150)}")
print(Karolina.contact())
print(Klaudia.contact())
print(Agnieszka.businesscontact())
print(Karolina.label_lenght())
print(create_contacts())

