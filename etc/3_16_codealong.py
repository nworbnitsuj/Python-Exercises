#This is a Python program that says hello and asks for your assigned

print('Hey!  What\'s up?')
print('What is your name?')
myName = input()
print('It\'s dope to meet you, ' + myName + '!')
print('The length of your name is: ')
print(len(myName))
print('How old are you?')
myAge = input()
if(int(myAge) < 21):
    print('You\'re only ' + myAge + '!? You can\'t party with us!')
else:
    print('Let\'s party!')
