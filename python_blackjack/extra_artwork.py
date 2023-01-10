
HEARTS = chr(9829) # Character 9829 is '♥'. 
DIAMONDS = chr(9830) # Character 9830 is '♦'. 
SPADES = chr(9824) # Character 9824 is '♠'. 
CLUBS = chr(9827) # Character 9827 is '♣'.

cards = ""

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', ''] # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card. 
        if card == BACKSIDE:
            # Print a card's back: 
            rows[1] += '|## | ' 
            rows[2] += '|###| ' 
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2)) 
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        for row in rows:
            print(row)


            
    # for
    # card in cards:
    # rank = card[0] # card is a tuple like (rank, suit) if rank == 'A':
    # numberOfAces += 1
    # elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points.
    # value += 10 else:
    # value += int(rank) # Numbered cards are worth their number.
    # 209. 210. 211. 212. 213. 214. 215. 216. 217. 218. 219. 220. 221. 222. 223. 224. 225. 226. 227. 228. 229. 230. 231. 232. 233. 234. 235. 236. 237. 238. 239. 240. 241.
    # # Print
    # for row

    # each row on the screen:
    # def
    # getMove(playerHand, money):