# birth=input('birth:')
# birth=int(birth)
# if birth>2000:
#     print('00后')
# else:
#     print('00前')

#if else 练习
height=1.75
weigiht=80.5
BMI=weigiht/(height*height)
print(BMI)
#BMI=float(BMI)
#print(BMI)
if BMI>32:
    print('严重肥胖')
elif BMI>28:
    print('肥胖')
elif BMI>25:
    print('过重')
elif BMI>18.5:
    print('正常')
else:
    print('过轻')
