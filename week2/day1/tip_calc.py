totalb = float(input('Total bill amount? '))
service = input('Level of service? ')

if service == 'good':
    tip = totalb * .2
elif service == 'fair':
    tip = totalb * .15
elif service == 'bad':
    tip = totalb * .1

totala = totalb + tip

print('Tip amount: $' + '%.2f' % tip)
print('Total amount: $' + '%.2f' %totala)