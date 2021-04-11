import string
import random
def generate_id():
    tokens=list(string.ascii_letters + string.digits)
    uid=" "
    for i in range(6):
        uid+=random.choice(tokens)
    return uid    
#print(generate_id())
class Amazon:
    def __init__(self):
      self.id=None
      self.name=None
      self.email=None
      self.order_cart=None
      self.isprime=1

    def get_details(self):
       self.id=generate_id()
       self.name=input("Enter Name: ")
       self.email=input("Enter Email id: ")   

    def buy_prime(self):
      self.isprime=0

    def buy_items(self):
      self.order_cart=[i for i in input("Enter the item names: ").split(", ") ]

user_list=[]

def find_user_pos(new_user):
    user_count=len(user_list)
    pos=0
    for i in range(user_count):
        if user_list[i].isprime<= new_user.isprime:
            pos+=1
    return pos

ch="y"
while ch=="y":
    new_user=Amazon()
    new_user.get_details()

    op = input("Want to order? y/n: ")
    if op=="y":
        new_user.buy_items()
    op=input("Do you want to buy Prime? y/n: ")
    if op=="y":
        new_user.buy_prime()
    pos=find_user_pos(new_user)    
    user_list.insert(pos,new_user)
    ch=input("Want to add more? y/n: ")

#print(user_list)
#user_list=sorted(user_list, key=lambda user: user.isprime)

for i in user_list:
    if i.isprime==0:
        print(f"Hi {i.name},unique id{i.id} your oder{i.order_cart} has been shipped under Prime delivery")
    else:
        print(f"Hi {i.name},unique id{i.id} your oder{i.order_cart} has been shipped")
