answers = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

from random import random , randint
text = input( "Please enter a number(1 to 8): " )
if int(text) > 0 and int(text) < 9:
    print (answers[randint(0,len(answers)-1)])
else:
  print('wrong number')