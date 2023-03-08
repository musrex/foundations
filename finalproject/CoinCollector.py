
class CoinCollector:

    
    def parseChange(coins):
        purse = {
        "P":0,
        "N":0,
        "D":0,
        "Q":0,
        "H":0,
        "W":0, 
        }

        for x in coins:
            if x == purse["P"]:
                purse["P"] = purse["P"] + 1
        # implement parseChange here
        #◦ ‘P’ represents a penny (1 cent)
        #◦ ‘N’ represents a nickel (5 cents)
        #◦ ‘D’ represents a dime (10 cents)
        #◦ ‘Q’ represents a quarter (25 cents)
        #◦ ‘H’ represents a half-dollar (50 cents)
        #◦ ‘W’ represents a whole dollar (100 cents)
        return 0
