print('Welcome to my computer Quiz !')
playing = str(input('Do you want to play?(yes/no) '))

if (playing.lower() != 'yes'):
  quit()

print("Okay let's play :)")

count = 0
answer = str(input('What does CPU stand for? '))
answerOne = 'central processing unit'
if(answer.lower() == answerOne):
  print("Yeah that's correct ✅")
  count += 1
else:
  print("Noo!, it's wrong 🤯")

answer = str(input('What does GPU stand for? '))
answerTwo = 'graphics processing unit'
if(answer.lower() == answerTwo):
  print("Yeah that's correct ✅")
  count += 1
else:
  print("Noo!, it's wrong 🤯")

answer = str(input('What does CPU stand for? '))
answerOne = 'central processing unit'
if(answer.lower() == answerOne):
  print("Yeah that's correct ✅")
  count += 1
else:
  print("Noo!, it's wrong 🤯")

answer = str(input('What does YT stand for? '))
answerThree = 'youtube'
if(answer.lower() == answerThree):
  print("Yeah that's correct ✅")
  count += 1
else:
  print("Noo!, it's wrong 🤯")

answer = str(input('What does MVC stand for? '))
answerFour = 'model view controller'
if(answer.lower() == answerFour):
  print("Yeah that's correct ✅")
  count += 1
else:
  print("Noo!, it's wrong 🤯")

percentage = count/5 * 100
if(count > 0 and count <= 5):
  print('You got ' + str(count) + " queestions correct!")
  print("congrats you answered {0} passed 🎊🎉 with {1}%".format(count, percentage))
else:
  print("You failed")

