# goal is to reconstruct a trip by figuring out the correct order of tickets.  The first ticket will have a source of None, and the last ticket will have a destination of None.

# find the ticket with a source of None, set it as the first entry in the list.
# find the ticket with a destination of None, set it as the last entry in the list.
# Find the ticket with the source that is the same as the previous ticket's destination, from the example, the second ticket would have the source as LAX and the destination as the next airport, which would be the source of the next ticket, and so on.
# see readme for more details.

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    return route
