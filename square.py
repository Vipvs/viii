x=int(input("enter a value"))
def is_power_of_two(x):
   return x>0 and (x&(x-1))==0
print("yes")
