fru = input('Item :').title()
friuts_l = ['Apple','Banana','Strawberry','Grapefruit','Lemon','Lime','Avocado','Pear','Sweet Cherries','Kiwifruit']
calories = [130,110,50,60,15,20,50,100,100,90]
for i in range(len(friuts_l)):
    if fru in friuts_l[i]:
        f = friuts_l.index(fru)
        print(f'Calories:',calories[f])
        break
    else:
        continue
