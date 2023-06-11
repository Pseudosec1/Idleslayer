from random import randint

# modify these values for number of rounds to run, target coins you're aiming for, and a 0 or 1 for whether or not you have the extra coin bonus activated
rounds = 1000
target = 200
BONUS = 1

#########################################
# don't modify anything below this line #
#########################################
total_coins = 0
highest = 0
round_met = 0

def get_coins():

	lose = False
	current_wins = 0
	coins = 0
	roll = 0
	
	while not lose:
		num = randint(0, 15)
		roll += 1
		
		if num == 0:
			lose = True
		elif num%2 == roll%2:
			lose = True
		else:
			current_wins += 1
			coins = coins + current_wins + BONUS
			
	return coins, current_wins

for i in range(0,rounds):

	coins = 0
	
	if total_coins >= target:
		coins, current_wins = get_coins()
	else:
		coins, current_wins = get_coins()
		if (total_coins + coins) >= target:
			round_met = i+1

			
	if coins > highest:
		highest = coins
	total_coins += coins
	
	print(f'wins for round {i+1}: {current_wins} wins yielding {coins} coins')
	
print(f'received {total_coins} in {rounds} rounds for an average of {total_coins/rounds} per round with the most coins won in a round being: {highest}')

if total_coins >= target:
	print(f'target of {target} met on round {round_met}')
else:
	 print(f'target of {target} missed by {target-total_coins} after {rounds} rounds')
