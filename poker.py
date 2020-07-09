#Given various poker hands as arguments, print what type of hand each argument is.

#The list of hands in ranking order are as follows:

#Hand	Cards	Description
#Royal Flush	🃁🃎🃍🃋🃊	Ten to Ace of the same suit
#Straight Flush	🃛🃚🃙🃘🃗	Five consecutive cards of the same suit
#Four of a Kind	🃕🃅🂵🂥🃂	Four cards of the same rank
#Full House	🂦🂶🃆🃞🂾	Three of a Kind combined with a Pair
#Flush	🃋🃉🃈🃄🃃	Five cards of the same suit
#Straight	🃊🂩🂸🃇🃖	Five consecutive cards
#Three of a Kind	🃝🂭🂽🂹🂢	Three cards of the same rank
#Two Pair	🂻🂫🃓🂣🂲	Two separate pairs
#Pair	🂪🂺🂨🂷🃔	Two cards of the same rank
#High Card	🃎🃍🂧🂤🂳	No other hand applies

#code starts

Hands = {"Royal Flush":"Ten to Ace of the same suit", "Straight Flush":"Five consectutive card of same suit",
"Four of a Kind":"Four cards of the same rank", "Full House":"Three of a Kind combined with a pair",
"Flush":"Five cards of the same suit", "Straight":"Five consecutive cards",
"Three of a Kind":"Three cards of the same rank", "Two pair":"Two separate Pairs", "Pair":"Two cards of the same rank",
"High Card":"No other hand applies"}

for hand, definition in Hands.items():
    print("{:<15} | {}".format(hand, definition))
