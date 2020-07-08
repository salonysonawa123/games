import random
print("what about today's result ")
print("click on OK or ENTER button")
text = input()
if text=="":
    messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

#print(messages[random.randint(0, len(messages) - 1)]
    print(messages[random.randint(0,8)])