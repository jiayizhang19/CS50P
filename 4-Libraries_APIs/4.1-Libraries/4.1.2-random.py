'''
1. random.choice(list) --> randomly choose one items from the list.
2. random.choices(list, k=n, weights=[]) --> randomly choose n items from the list following the weights, while the items could be duplicate
3. random.sample(list, k=n) --> similar as the above, but the items choosed are obsolutely unique. 
'''

import random

cards = ['jack', 'queen', 'king']

def main():
    print(random.choice(cards))
    print(random.choices(cards, k=2, weights=[60,20,20]))
    print(random.sample(cards,k=2))

main()