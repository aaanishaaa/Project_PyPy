from logo_1 import logo

print(logo)

bids={}
is_biding_finished = False

def finding_highest_bidder(bidding):
    highest_bid=0
    Winner=""
    for bidder in bidding:
        bid_amount=bidding[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            Winner=bidder
    print(f"The winner of the bid is {Winner}")
    
while not is_biding_finished:
    name=input("Enter the name of the bidder")
    price= int(input("Enter your bid : $"))
    bids[name]=price
    continuing=input("Are there more bidders? Enter 'y' for yes and 'n' for no")
    if(continuing=="y"):
        print("/n*1000")
    elif(continuing=="n"):
        is_biding_finished=True
        finding_highest_bidder(bids)
