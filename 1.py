print("для закінчення 0 в якості знака операціхї")

while True:
    s = input("Знак (+, -, *, /):")
    if s == '0':
        break
    if s not in ('+', '-', '*', '/'):
        continue
    a = float(input('a = '))
    b = float(input('b = '))

    if s == '+' :
       print(a + b)
    elif s == '-':
       print(a - b)
    elif s == '*':
       print(a * b)
    elif s == '/':
         if b !=0:
            print(a / b)
         else:
             print("ДІЛЕННЯ НА НУЛЬ!")
