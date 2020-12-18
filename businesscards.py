from faker import Faker
fake =Faker()
print(fake.name())

class BaseContact():
  def __init__(self,name, surname,mobile_phone_private,email):
    self.name=name
    self.surname=surname
    self.mobile_phone_private=mobile_phone_private
    self.email=email
  def __str__(self):
    return f"Wybieram numer +48 {self.mobile_phone_private} i dzwonię do  {self.name} {self.surname}"

class BusinessContact(BaseContact):
  def __init__(self,position,company,mobile_phone):
    self.position=position
    self.company=company
    self.mobile_phone=mobile_phone
Karolina=BaseContact(name="Julie",surname="Lorenos",mobile_phone_private="564 879 786",email="kar.cho@o2.pl")
print(Karolina)