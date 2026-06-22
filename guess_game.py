import random


guess_number=random.randint(1,10)
print("guess the number = ")
guess=int(input())
guess_limit=1
guess_count=0

while guess!=guess_number and guess_count<guess_limit:
  if guess<guess_number:
    print("guess higher")
  else:
    print("guess lower")
  guess=int(input())
  guess_count+=1
if guess==guess_number:
  print("you won")
else:
  print("you lost")
  print("the number was",guess_number)