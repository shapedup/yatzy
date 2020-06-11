# This file has mainly been used to test the class methods of YatzyScoresheet()
from dice import D6
from hands import YatzyHand
from scoresheets import YatzyScoresheet
hand = YatzyHand()
six = D6(value=6)
five = D6(value=5)
four= D6(value=4)
three = D6(value=3)
two = D6(value=2)
one = D6(value=1)

# hand[:] = [one, three, three, four, four]
# print('Hand: {} Pair score: {}'.format(hand, YatzyScoresheet().score_one_pair(hand))) # PAIR 4+4 = 8

# print('Hand:', hand, 'Two pair:', YatzyScoresheet().score_two_pair(hand)) # TWO PAIR 4+4+3+3 = 14

# hand[:] = [one, three, three, three, four]
# print('Hand:', hand, '3 OAK:', YatzyScoresheet().score_three_kind(hand)) # 3 OAK 3+3+3 = 9

# hand[:] = [one, four, four, four, four]
# print('Hand:', hand, '4 OAK:', YatzyScoresheet().score_four_kind(hand)) # 4 OAK 4+4+4+4 = 16

# hand[:] = [three, three, six, six, six]
# print('Hand:', hand, 'Full House:', YatzyScoresheet().score_full_house(hand)) # FULL HOUSE 3+3+6+6+6 = 24

# hand[:] = [one, two, three, four, five]
# print('Hand:', hand, 'Small straight:', YatzyScoresheet().score_small_straight(hand)) # S STRAIGHT 1+2+3+4+5 = 15

# hand[:] = [two, three, four, five, six]
# print('Hand:', hand, 'Large straight:', YatzyScoresheet().score_large_straight(hand)) # L STRAIGHT 2+3+4+5+6 = 20

# hand[:] = [one, one, one, one, one]
# print('Hand:', hand, 'YATZY!:', YatzyScoresheet().score_yatzy(hand)) # 50

# hand[:] = [three, four, two, three, five]
# print('Hand:', hand, 'Chance:', YatzyScoresheet().score_chance(hand)) # Chance 3+4+2+3+5 = 17

# hand[:] = [one, four, six, five, three]
# print('Hand:', hand, 'not Yatzy:', YatzyScoresheet().score_yatzy(hand)) # 0

hand[:] = [four, four, four, five, three]
print('Hand:', hand, 'Pair with 3oak:', YatzyScoresheet().score_one_pair(hand)) # 8

hand[:] = [five, five, five, five, five]
print('Hand:', hand, 'Pair with Yatzy:', YatzyScoresheet().score_one_pair(hand)) # 10
print('Hand:', hand, '3oak with Yatzy:', YatzyScoresheet().score_three_kind(hand)) # 15
print('Hand:', hand, '4oak with Yatzy:', YatzyScoresheet().score_four_kind(hand)) # 20
