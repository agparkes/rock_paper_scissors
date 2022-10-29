# Rock Paper Scissor Game: Version 1
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# player1 = input("Player 1, make your move: ")
# player2 = input("Player 2, make your move: ")

# if player1 == "rock" and player2 == "scissors":
#     print("player1 wins!!!")
# elif player1 == "rock" and player2 == "paper":
#     print("player2 wins!!!")
# elif player1 == "paper" and player2 == "rock":
#     print("player1 wins!!!")
# elif player1 == "paper" and player2 == "scissors":
#     print("player2 wins!!!")
# elif player1 == "scissors" and player2 == "rock":
#     print("player2 wins!!!")
# elif player1 == "scissors" and player2 == "paper":
#     print("player1 wins!!!")
# elif player1 == player2:
#     print("It's a tie!!!")
# else:
#     print("something went wrong. Try again. Please!!!")

# Refactor Rock Paper Scissor Game: Version 2
# print("Rock...")
# print("Paper...")
# print("Scissors...")

# player1 = input("Player 1, it's your move: ")
# print("****NO CHEATING\n" * 10)
# player2 = input("Player 2, it's your move: ")

# if player1 == player2:
#     print("We have a tie game!!!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("player1 wins!!!")
#     elif player2 == "paper":
#         print("player2 wins!!!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("player1 wins!!!")
#     elif player2 == "scissors":
#         print("player2 wins!!!")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("player1 wins!!!")
#     elif player2 == "rock":
#         print("player2 wins!!!")
# else:
#     print("something went wrong. Try again...Please!!!")

# Version 3: Much cleaner and shorter code (NO ERROR HANDLING)
p1 = input("Player 1: rock, paper, or scissors ")
p2 = input("Player 2: rock, paper, or scissors ")
 
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("player1 wins")
elif p1 == "paper" and p2 == "rock":
    print("player1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("player1 wins")
else:
    print("p2 wins")