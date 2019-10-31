total_bill = float(input('Total bill amount? '))
service = input('Level of service? ')
split = int(input('SPlit how many ways? '))

if service == 'good':
    tip = total_bill * .2
elif service == 'fair':
    tip = total_bill * .15
elif service == 'bad':
    tip = total_bill * .1

total_amount = total_bill + tip
per_person = total_amount / split
print('Tip amount: $' + '%.2f' % tip)
print('Total amount: $' + '%.2f' %total_amount)
print('Amount per person: $' + '%.2f' %per_person)