#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    The tickets are arranged in linked list fashion. Where one leads to the other.
    """
    table = {}
    route = []
    for i in tickets:
        table[i.source] = i.destination
    ticket = table["NONE"] # Get first ticket
    while ticket != "NONE": # While the value of the ticket is not NONE
        route.append(ticket) # Append value to route
        ticket = table[ticket] # Get next value by simply putting in the Key of current ticket
    route.append(ticket) # Added this because last item in tests has NONE.

    return route
