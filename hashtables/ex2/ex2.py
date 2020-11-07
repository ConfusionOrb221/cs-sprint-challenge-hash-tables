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
    destinations = {}
    route = []

    for i in range(length):
        destinations[tickets[i].source] = tickets[i].destination

    for i in range(length):
        if i == 0:
            route.append(destinations["NONE"])
        else:
            route.append(destinations[route[i-1]])

    print(destinations)

    return route
