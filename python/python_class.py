""" 
problem: 
1) Create a class named "Cooking", where four functions named "wash", "cut", "spice" and "oven" will be there.
2) Run the function to show the output.
"""

class Cooking:
  def __init__(self, name):
    self.name = name

  #defining function to wash the item
  def func_wash(abc):
    print(abc.name + " is washed.")

  #defining function to cut the item
  def func_cut(abc):
    print(abc.name + " is cut.")

  #defining function to add spice to the item
  def func_spice(abc):
    print(abc.name + " is mixed with spice.")

  #defining function to put the item in the oven
  def func_oven(abc):
    print(abc.name + " is in the oven.")

p1 = Cooking("Meat")
p2 = Cooking("Fish")
p3 = Cooking("Vegetable")

p1.func_wash()
p1.func_cut()
p1.func_spice()
p1.func_oven()

p2.func_wash()
p2.func_cut()
p2.func_spice()
p2.func_oven()

p3.func_wash()
p3.func_cut()
p3.func_spice()
p3.func_oven()