#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    lookup = {}
    routes = [None] * length
    for x in tickets:
        lookup[x.source] = x.destination
    
    routes[0] = lookup['NONE']
    for i in range(1, len(routes)):
        routes[i] = lookup[routes[i - 1]]

    return routes

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
