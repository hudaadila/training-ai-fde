# Week 00 — Setup and Diagnostic

## Diagnostic

### Function: `most_frequent`

`most_frequent(items)` returns the element that appears most often in a list. On a tie, it returns whichever element appeared first in the list. It raises a `ValueError` if the list is empty.

**What would break it:**
- Passing a list with unhashable types (e.g. a `dict` or a `list` as an element) raises a `TypeError` because the function uses items as dictionary keys.
- Passing a non-list iterable like a plain string iterates over individual characters instead of words, which is likely not the intended behaviour.

### Command-line task

```
# Navigate to the week folder
cd week-00

# Run the script
python diagnostic.py
# Output: All tests passed.

# Read an environment variable
echo $env:USERNAME
```

### GitHub operation

Created branch `week-00/diagnostic`, committed `diagnostic.py`, and pushed to remote. Pull request opened from `week-00/diagnostic` → `main`.
