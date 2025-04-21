#research more about scopes and applications And try to solve problems
def myfunc():
  x = 300  # local variable
  print(x)

myfunc()
##
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#global
x=300
def myfunc():
  x = 200
  print(x)
myfunc()
