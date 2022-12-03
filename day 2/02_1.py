winning_hands = {"ROCK":"SCISSORS","PAPER":"ROCK","SCISSORS":"PAPER"}
opponent_hand = {"A":"ROCK","B":"PAPER","C":"SCISSORS"}
user_hand = {"X":"ROCK","Y":"PAPER","Z":"SCISSORS"}

points_per_hand = {"X":1,"Y":2,"Z":3}

score = 0
with open("02-input.txt") as f:
   for line in f:
      play = list("".join(line.split()))
      score += points_per_hand[play[1]]
      opponent_draw = opponent_hand[play[0]]
      user_draw = user_hand[play[1]]
      if opponent_draw == user_draw:
         score += 3
      if (user_draw,opponent_draw)in winning_hands.items():
         score += 6
print(score)