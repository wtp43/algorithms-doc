# Sequences



## Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

- Store counter of available numbers
- Always start building sequence at smallest possible number


```python
def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # we want to start at smallest card possible in the current sequence
            while card_count[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1

        return True
```