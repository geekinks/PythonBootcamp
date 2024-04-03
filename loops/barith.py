birthdays = {'Ali': 'Apr 1', 'fatima': 'Dec 12', 'khadija': 'Mar 4'}
while True:
print('Enter a name: (blank to quit)')
name = input()
if name == '':
break
if name in birthdays:
print(birthdays[name] + ' is the birthday of ' + name)
else:
print('I do not have birthday information for ' + name)
print('What is their birthday?')
bday = input()
birthdays[name] = bday
print('Birthday database updated.')

#  create a dictionary with key as name and # value as birthday
 
barith = {'Ali': 'Apr 1', 'fatima': 'Dec 12', 'khadija': 'Mar 4'}

#  loop through the dictionary

for name in barith:
    print(name + ' birthday is ' + barith[name])

    