"""
Week 0 diagnostic — coding warm-up.

Function: most_frequent(items)
Returns the element that appears most often in a list.
On a tie, returns the one that appeared first.
"""


def most_frequent(items):
    if not items:
        raise ValueError("items must not be empty")
    seen_order = []
    counts = {}
    for item in items:
        if item not in counts:
            seen_order.append(item)
            counts[item] = 0
        counts[item] += 1
    return max(seen_order, key=lambda k: counts[k])


# --- tests ---

assert most_frequent([1, 2, 2, 3]) == 2
assert most_frequent(["a", "b", "a", "c", "b", "a"]) == "a"
assert most_frequent([7]) == 7
assert most_frequent([1, 2, 3, 1, 2, 3, 1]) == 1
# tie: "x" appears first, both appear twice
assert most_frequent(["x", "y", "x", "y"]) == "x"

try:
    most_frequent([])
    assert False, "expected ValueError"
except ValueError:
    pass

print("All tests passed.")
