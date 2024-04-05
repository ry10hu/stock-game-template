import stocktable, nametoid, os, platform, math, random, colours
from colorama import Fore, Back, Style

def userInput():
    while True:
        stocktable.money = int(math.floor(float(stocktable.money)))
        user_input = input(colours.questioncolour + "\nWhat would you like to do? " + colours.inputcolour).lower()
        user_input = user_input.split()
        print(user_input)
        # print('\n')
        if user_input[0] == 'changestock':
            for x in range(0, len(stocktable.table)):
                number = random.randint(-20, 20)
                if stocktable.table[x][1] + number > 0:
                    stocktable.table[x][1] += number    
        stocktable.money=int(stocktable.money)

        if user_input[0] == "buy" or user_input[0] == 'b':
            if len(user_input) == 3:
                buying = user_input[1]
                amount = user_input[2]
            else:
                print(colours.answercolour + f'\nERROR: WRONG SYNTAX. The Correct Syntax Is: buy \{stock\} amount' + colours.inputcolour)
                continue
            try:
                if amount == 'max':
                    amount = int(stocktable.money/stocktable.table[nametoid.toID(buying)][1])
                else:
                    amount = int(amount)
                if stocktable.money >= amount * stocktable.table[nametoid.toID(buying)][1]:
                    stocktable.money -= amount * stocktable.table[nametoid.toID(buying)][1]
                    stocktable.table[nametoid.toID(buying)][2] += amount
                else:
                    req = amount * stocktable.table[nametoid.toID(buying)][1] - stocktable.money
                    print(colours.answercolour + f'You need {req} more money' + colours.inputcolour)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input[0] == 'sell' or user_input[0] == 's':
            if len(user_input) == 3:
                selling = user_input[1]
                amount = user_input[2]
            else:
                print(colours.answercolour + f'\nERROR: WRONG SYNTAX. The Correct Syntax Is: sell \{stock\} \{amount\}' + colours.inputcolour)

            try:
                if amount == 'max':
                    amount = stocktable.table[nametoid.toID(selling)][2]
                else:
                    amount = int(amount)
                if stocktable.table[nametoid.toID(selling)][2] >= amount:
                    stocktable.money += amount * stocktable.table[nametoid.toID(selling)][1]
                    stocktable.table[nametoid.toID(selling)][2]-= amount
                else:
                    print(colours.answercolour + '\nYou can\'t sell what you don\'t have, idiot.' + colours.inputcolour)
            except ValueError:
                print('\nEnter a numeric value or a shorthand (max). \n')
                continue

        if user_input[0] == 'inventory' or user_input[0] == 'i':
            
            for x in range(0, len(stocktable.table)):
                print(colours.answercolour + f'\n{stocktable.table[x][3]} Owned:  {stocktable.table[x][2]}      Current Price: {stocktable.table[x][1]}' + colours.inputcolour)
            

        if user_input[0] == 'balance' or user_input[0] == 'bal':
            print(colours.answercolour + f'\nYou have {stocktable.money} money.' + Style.RESET_ALL)
        if user_input[0] == 'price':
            price = user_input[1]
            print(colours.answercolour + f'\nThe price of {price} is {stocktable.table[nametoid.toID(price)][1]} money.' + Style.RESET_ALL)
        if user_input[0] == 'cls' or user_input[0] == 'clear':
            if platform.system() == "Windows":
               os.system('cls')
            elif platform.system() in ["Linux", "Darwin"]:  
                os.system('clear')
