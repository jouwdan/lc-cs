"""Original queue model: arrivals, service, then record remaining queue."""
from random import Random
from statistics import mean


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


def simulate(minutes, arrival_probability, service_probability, seed):
    if type(minutes) is not int or minutes < 0:
        raise ValueError("minutes must be a non-negative integer")
    if not (0 <= arrival_probability <= 1 and 0 <= service_probability <= 1):
        raise ValueError("probabilities must lie in [0, 1]")
    rng = Random(seed)
    arrivals, services = [], []
    for _ in range(minutes):
        arrivals.append(int(rng.random() < arrival_probability))
        services.append(int(rng.random() < service_probability))
    return queue_trace(arrivals, services)


def summarise(result):
    history = result["history"]
    return {"final": history[-1] if history else 0,
            "maximum": max(history, default=0),
            "mean_queue": mean(history) if history else None}


def self_check():
    result = queue_trace([1, 0, 1, 1, 0], [0, 1, 0, 1, 1])
    assert result["history"] == [1, 0, 1, 1, 0]
    assert simulate(5, 0, 1, 8)["history"] == [0] * 5
    assert simulate(5, 1, 0, 8)["history"] == [1, 2, 3, 4, 5]
    assert summarise(simulate(0, .5, .5, 8))["mean_queue"] is None
    assert simulate(30, .6, .5, 7) == simulate(30, .6, .5, 7)
    for args in [(-1, .5, .5, 1), (5, 1.2, .5, 1)]:
        try:
            simulate(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input accepted")
    for seed in range(20):
        result = simulate(120, .6, .5, seed)
        assert min(result["history"]) >= 0
        assert result["history"][-1] == result["arrivals"] - result["served"]


if __name__ == "__main__":
    self_check()
    print("Checks passed.")
    print("Remaining queue:", simulate(10, 0.6, 0.5, 7)["history"])
    for service in (0.5, 0.8):
        means = [summarise(simulate(120, 0.6, service, seed))["mean_queue"] for seed in range(20)]
        print(f"Service {service:.1f}: mean of run means={mean(means):.3f} people; "
              f"range={min(means):.3f} to {max(means):.3f}")
