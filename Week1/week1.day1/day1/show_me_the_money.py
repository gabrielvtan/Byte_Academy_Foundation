# Input an amount of money as a floating point number
change_need = float(input("How much change do you need?\n"))

penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
one_dollar = 1.00
five_dollar = 5.00
ten_dollar = 10.00
twenty_dollar = 20.00
fifty_dollar = 50.00
hundred_dollar = 100.00

hundred_need = float(change_need//100)
fifty_need = float((change_need%100)//50)
twenty_need = float(((change_need%100)%50)//20)
ten_need = float((((change_need%100)%50)%20)//10)
five_need = float(((((change_need%100)%50)%20)%10)//5)
one_need = float((((((change_need%100)%50)%20)%10)%5)//1)
quarter_need = float(((((((change_need%100)%50)%20)%10)%5)%1)//0.25)
dime_need = float((((((((change_need%100)%50)%20)%10)%5)%1)%0.25)//0.10)
nickel_need = float(((((((((change_need%100)%50)%20)%10)%5)%1)%0.25)%0.10)//0.05)
penny_need = float((((((((((change_need%100)%50)%20)%10)%5)%1)%0.25)%0.10)%0.05)//0.01)

print('hundreds needed: {}'.format(hundred_need))
print('fifty needed: {}'.format(fifty_need))
print('twenty needed: {}'.format(twenty_need))
print('ten needed: {}'.format(ten_need))
print('five needed: {}'.format(five_need))
print('one needed: {}'.format(one_need))
print('quarter needed: {}'.format(quarter_need))
print('dime needed: {}'.format(dime_need))
print('nickel needed: {}'.format(nickel_need))
print('penny needed: {}'.format(penny_need))