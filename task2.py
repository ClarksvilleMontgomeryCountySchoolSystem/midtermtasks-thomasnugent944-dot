

# Allowance & Chore Tracker

# Given variables
allowance = 15
dishes, room, trash, lawn, laundry, vacuum = 3, 5, 2, 8, 4, 6
candy, soda, game, movie, toy, snack = 4, 2, 15, 10, 7, 3

"""
CHORE MENU - Earn Money:        PURCHASE MENU - Spend Money:
dishes = $3                      candy = $4
room = $5                        soda = $2
trash = $2                       game = $15
lawn = $8                        movie = $10
laundry = $4                     toy = $7
vacuum = $6                      snack = $3
"""


# Week 1: You took out the trash and cleaned your room
allowance += trash
allowance += room

# You bought soda
allowance -= soda

# Week 2: Parents gave you a bonus! They doubled your allowance for working hard
allowance *= 2

# You did the laundry
allowance += laundry

# You bought a new movie
allowance -= movie

# Week 3: You decided to put a fourth of your money in savings
allowance /= 4

# Print final allowance
print(f"Allowance: ${allowance}")#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!
