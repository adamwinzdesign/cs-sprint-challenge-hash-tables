# goal is to reconstruct a trip by figuring out the correct order of tickets.  The first ticket will have a source of None, and the last ticket will have a destination of None.

# Find the ticket with the source that is the same as the previous ticket's destination, from the example, the second ticket would have the source as LAX and the destination as the next airport, which would be the source of the next ticket, and so on.

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    flights = {}
    route = []
    for ticket in tickets:
        flights[ticket.source] = ticket.destination
    current_flight = flights['NONE']
    while current_flight != 'NONE':
        route.append(current_flight)
        current_flight = flights[current_flight]
    route.append(current_flight)

    return route
