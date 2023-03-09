
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
            if x == purse["N"]:
                purse["N"] = purse["N"] + 1
            if x == purse["P"]:
                purse["D"] = purse["D"] + 1
            if x == purse["Q"]:
                purse["Q"] = purse["Q"] + 1
            if x == purse["H"]:
                purse["H"] = purse["H"] + 1
            if x == purse["W"]:
                purse["W"] = purse["W"] + 1            

        return 0
