"""Change the two event lists, predict, then run in Python 3."""
def queue_trace(arrivals, services):
    if len(arrivals) != len(services) or any(x not in (0, 1) for x in arrivals + services):
        raise ValueError("equal-length lists of binary events required")
    queue, served, history = 0, 0, []
    for arrival, service in zip(arrivals, services):
        queue += arrival
        if queue and service:
            queue -= 1
            served += 1
        history.append(queue)
    return {"history": history, "arrivals": sum(arrivals), "served": served}



arrivals = [1, 0, 1, 1, 0]
services = [0, 1, 0, 1, 1]
result = queue_trace(arrivals, services)
history = result["history"]
print("Remaining queue:", history)
print("Arrivals:", result["arrivals"])
print("Served:", result["served"])
