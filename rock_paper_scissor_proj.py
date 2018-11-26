print("...Rock...")
print("...Scissors...")
print("...Paper...")
user1 = input("Enter Player 1's choice: ")
user2 = input("Enter Player 2's choice: ")

if user1 == 'scissors' and user2 == 'paper':
    print('Player1 wins')
elif user1 == 'rock' and user2 == 'scissors':
    print('Player1 wins')
elif user1 == 'paper' and user2 == 'rock':
    print('Player1 wins')
elif user1 == user2:
    print('It\'s a tie')
else:
    print('Player2 wins')
