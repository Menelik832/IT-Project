print("Hello")
def tempchange():
  n=int(input("Give me a number."))
  u1=input("What do you want to convert?(Celsius or Fahrenheit)")
  if u1=="celsius":
    nf=((n-32)*5/9,"degrees fahrenheit")
    print(nf)
  elif u1=="fahrenheit":
    nf=(n*9/5+32,"degrees celsius")
    print(nf)
tempchange()  
