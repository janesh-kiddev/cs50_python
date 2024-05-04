def inter(x,y,z):
    if y=='+':
        return x+z
    elif y=='-':
        return x-z
    elif y=='*':
        return x*z
    elif y=='/':
        return x/z

get = input("Expression : ").split()
x = float(get[0]),get[1],float(get[2])
print(inter(*x))
