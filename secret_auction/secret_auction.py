import os

# Call clear() to clear the output in the console.
clear = lambda: os.system('clear')

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid:.2f}.')

print('Welcome to the secret auction program.')
while not bidding_finished:
    name = input('What is your name? ')
    bid = float(input('Whats is your bid? $'))
    bids[name] = bid
    other_bidders = input('Are there any other bidders? Type YES or NO. ')
    clear()
    if other_bidders == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
