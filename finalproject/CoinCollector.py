
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
            if x == "P":
                purse["P"] = purse["P"] + 1
            if x == "N":
                purse["N"] = purse["N"] + 1
            if x == "D":
                purse["D"] = purse["D"] + 1
            if x == "Q":
                purse["Q"] = purse["Q"] + 1
            if x == "H":
                purse["H"] = purse["H"] + 1
            if x == "W":
                purse["W"] = purse["W"] + 1            

        return purse
