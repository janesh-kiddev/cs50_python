def main(s):
    list_d=['a','o','e','i','u','A','E','I','O','U']
    emp=""
    for i in s:
        if i in list_d:
            li=list(i)
            li.remove(i)
        else:
            emp+=i
    return emp

s=input('Input :')
print(f'Output:{main(s)}')
