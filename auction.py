# pylint: disable=missing-docstring

from itertools import count

# CLI = Command Line Interface
from utils import Cli


class Auction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()


    # Input bidders
    def bidder():
        bidders = []
        for index in count(1):
            bidder = self.cli.prompt(
                f"Enter name for bidder {index} (enter nothing to move on):"
            )
            if not bidder:
                break
            bidders.append(bidder)
        self.cli.display(f"\nBidders are: {', '.join(bidders)}\n")
    

    # Display winner
    def display_winner(winner, standing_bid)
        self.cli.display("\n~~~~~~~~\n")
        self.cli.display(f"Winner is {winner}. Winning bid is {standing_bid}.")

