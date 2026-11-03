"""Original unary-increment machine, with an explicit transition trace."""

def increment_unary(text):
    if any(symbol != "1" for symbol in text):
        raise ValueError("input must contain only ones; empty string represents zero")
    tape = list(text) + ["_"]
    head, state, trace = 0, "scan", []
    while state != "halt":
        read = tape[head]
        if read == "1":
            write, move, next_state = "1", 1, "scan"
        else:
            write, move, next_state = "1", -1, "halt"
        tape[head] = write
        trace.append({"step": len(trace) + 1, "state": state, "head": head, "read": read,
                      "write": write, "move": "R" if move == 1 else "L", "next": next_state,
                      "tape": "".join(tape)})
        head += move
        state = next_state
    return "".join(tape), trace


def self_check():
    for length in range(8):
        output, trace = increment_unary("1" * length)
        assert output == "1" * (length + 1)
        assert len(trace) == length + 1
        assert trace[-1]["next"] == "halt"
    try:
        increment_unary("101")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid tape accepted")


if __name__ == "__main__":
    self_check()
    output, trace = increment_unary("111")
    for row in trace:
        print(row)
    print("Result:", output)
