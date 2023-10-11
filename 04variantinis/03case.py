#supgrogramuoti skaiciuotuva:veiksmai(+,-,*,/,^ - kelimas laipsniu,sqrt-saknies traukimas)
import math;

def sudetis(x, y):
    return x+y

def atimtis(x, y):
    return x-y

def daugyba(x, y):
    return x*y

def dalyba(x, y):
    return x/y

def laipsnis(x,y):
    return x^y

def saknis(x):
    return math.sqrt(x)

num1=int(input('Pirmas skaicius:'))
veiksmas=(input('Iveskite veiksma:'))
match veiksmas:
    case '+' | '-' | '*' | '/' | '^' | '&':
        txt='Iveskite veiksma:'
        if  veiksmas !='%':
            num2=int(input('Antras skaicius:'))

if veiksmas == '+':
    print(num1, "+", num2, "=", sudetis(num1, num2))
elif veiksmas == '-':
    print(num1, "-", num2, "=", atimtis(num1, num2))
elif veiksmas == '*':
        print(num1, "*", num2, "=", daugyba(num1, num2))
elif veiksmas == '/':
        print(num1, "/", num2, "=", dalyba(num1, num2))
elif veiksmas == '^':
        print(num1, "^", num2, "=", laipsnis(num1, num2))
elif veiksmas == '&':
    if  veiksmas !='%':
        print(num1,'&','=',saknis(num1))