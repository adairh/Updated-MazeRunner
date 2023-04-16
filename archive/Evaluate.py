from Bot import Bot
from Coin import Coin
from Location import Location


def evaluation_function(my_bot: Bot, coin: Coin, opp_bot: Bot):
    my_bot_loc: Location = my_bot.loc
    coin_loc: Location = coin.loc
    opp_bot: Location = opp_bot.loc
    dA = my_bot_loc.distance(coin_loc)
    dB = opp_bot.distance(coin_loc)
    pA = []
    pB = []
    chooseLoc = None
    if dA < dB:
        # finding path for A and B without considering opponent bot
        if len(pA) < len(pB):
            if dA < 2 and len(pA) <= 2:
                for nearCoin in coin_loc.getNearby():
                    if 2 > nearCoin.distance(my_bot_loc) >= 1:
                        if nearCoin not in pB:
                            if nearCoin in pB[-2].getNearby():
                                chooseLoc = nearCoin
                        break
                        # move to 'nearCoin'

        lB = len(pB)
        # if lB % 2 == 0:
        #
        # else:
