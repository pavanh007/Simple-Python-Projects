name = input("Type you name: ")
print("Welocome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you would like to go.?(left/right) ").lower()
if answer == 'left':
  answer = input('You come to a river, you can walk around it oe swiss accross? Type walk to "walk"/"swim" ').lower()
  if answer == 'swim':
    print('You swim accross and were eaten by an alligator !!')
  elif answer == 'walk':
    print('you walked for many miles, ran out of water and you lost the game. ')
  else:
    print('Not a valid option, You lose!')
elif answer == 'right':
  answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back ? (cross/back) :')
  if answer == 'back':
    print("You go back ad lose.")
  elif answer == 'cross':
    answer = input('You cross the bridge and meet a strange. Do you talk to them ? (yes/no) :').lower()
    if answer == 'yes':
      print('You talk to the stranger and they give you gold. YOU WIN!🎊')
    elif answer == 'no':
      print('You ignored the stranger and they are offended and you lose.')
    else:
      print('Not a valid option, You lose!')
  else:
    print('Not a valid option, You lose!')
else: 
  print('Not a valid option, You lose!')

print("Thank you for trying...!", name)