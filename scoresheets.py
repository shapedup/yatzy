from hands import YatzyHand

class YatzyScoresheet:
    # = Upper Section Scoring Methods =
    """Score all ones"""
    def score_ones(self, hand):
        return sum(hand.ones)
    
    """Score all twos"""
    def score_twos(self, hand):
        return sum(hand.twos)
    
    """Score all threes"""
    def score_threes(self, hand):
        return sum(hand.threes)
    
    """Score all fours"""
    def score_fours(self, hand):
        return sum(hand.fours)

    """Score all fives"""
    def score_fives(self, hand):
        return sum(hand.fives)
    
    """Score all sixes"""
    def score_sixes(self, hand):
        return sum(hand.sixes)
        
    """Total upper section score"""
    def total_upper_score(self):
        total_upper = sum(self.score_ones, self.score_twos, self.score_threes, self.score_fours, self.score_fives, self.score_sixes)
        if total_upper >= 63:
            return total_upper + 50
        return total_upper
    
    # = Lower Section Scoring Methods =
    """Method to score multiples of same dice"""
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count >= set_size:
                scores.append(worth*set_size)
        return max(scores)
    
    """Score a pair"""
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)
        
    """Score 2 pair"""
    def score_two_pair(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if count == 2:
                scores.append(worth*2)
        if len(scores) > 1:
            return sum(scores)
        return 0
    
    """Score 3 of a kind"""
    def score_three_kind(self, hand):
        return self._score_set(hand, 3)
	
    """Score 4 of a kind"""
    def score_four_kind(self, hand):
        return self._score_set(hand, 4)
	
    """Score small straight: 1,2,3,4,5"""
    def score_small_straight(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if count == 1:
                scores.append(worth)
            else:
                break
        if len(scores) == 5 and max(scores) == 5:
            return sum(scores)
        return 0
    
    """Score large straight: 2,3,4,5,6"""
    def score_large_straight(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if worth == 1 and count > 0:
                break
            if count == 1:
                scores.append(worth)
            else:
                continue
        if len(scores) == 5 and max(scores) == 6:
            return sum(scores)
        return 0
    
    """Score full house: 2,2,3,3,3"""
    def score_full_house(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if count == 3:
                scores.append(worth*3)
        for worth, count in hand._sets.items():
            if count == 2 and len(scores) == 1:
                scores.append(worth*2)
        if len(scores) == 2:
            return sum(scores)
        return 0
    
    """Score 'Chance': sum of all dice"""
    def score_chance(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if count > 0:
                scores.append(worth*count)
        return sum(scores)
    
    """YATZY! + 50"""
    def score_yatzy(self, hand):
        for worth, count in hand._sets.items():
            if count == 5:
                return 50
            return 0

    """Overall score"""
    def overall_score(self):
        return sum()

class Scoring:
    def __init__(self, hand = YatzyHand()):
        self.hand = hand

    def scores(self):
        return {
            "ones": YatzyScoresheet().score_ones(self.hand),
            "twos": YatzyScoresheet().score_twos(self.hand),
            "threes": YatzyScoresheet().score_threes(self.hand),
            "fours": YatzyScoresheet().score_fours(self.hand),
            "fives": YatzyScoresheet().score_fives(self.hand),
            "sixes": YatzyScoresheet().score_sixes(self.hand),
            "pair": YatzyScoresheet().score_one_pair(self.hand),
            "two pair": YatzyScoresheet().score_two_pair(self.hand),
            "three oak": YatzyScoresheet().score_three_kind(self.hand),
            "four oak": YatzyScoresheet().score_four_kind(self.hand),
            "Lstraight": YatzyScoresheet().score_small_straight(self.hand),
            "Hstraight": YatzyScoresheet().score_large_straight(self.hand),
            "full": YatzyScoresheet().score_full_house(self.hand),
            "chance": YatzyScoresheet().score_chance(self.hand),
            "YATZY!": YatzyScoresheet().score_yatzy(self.hand),
        }
    