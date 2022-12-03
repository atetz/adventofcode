winning_hands = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}
losing_hands = {v: k for k, v in winning_hands.items()}

opponent_hand = {"A":"ROCK","B":"PAPER","C":"SCISSORS"}
user_hand = {"X":"ROCK","Y":"PAPER","Z":"SCISSORS"}

points_per_hand = {"ROCK":1,"PAPER":2,"SCISSORS":3}

score = 0
with open("02-input.txt") as f:
   for line in f:
      play = list("".join(line.split()))
      if play[1] == "X":
         losing_hand = winning_hands[opponent_hand[play[0]]]
         score+= points_per_hand[losing_hand]       
      if play[1] == "Y":
         draw_hand = opponent_hand[play[0]]
         score+= points_per_hand[draw_hand]
         score += 3
      if play[1] == "Z":
         score += 6
         winning_hand = losing_hands[opponent_hand[play[0]]]
         score += points_per_hand[winning_hand]
         
print(score)