# AI Code Review Assignment (Python)

## Candidate

- Name: GELASA JARSO
- Approximate time spent: ~70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- The denominator uses the total number of orders, including cancelled ones, while the numerator excludes cancelled orders, resulting in an incorrect average.

- The function can raise a division-by-zero error when the input list is empty.

### Edge cases & risks

- All orders may be cancelled, leading to an invalid average.

- Assumes all orders contain "status" and "amount" keys.

### Code quality / design issues

- Mismatch between business logic intent and implementation.

- No defensive handling for empty or degenerate inputs.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Track only non-cancelled orders when computing both total and count.

- Add a guard to safely handle cases with zero valid orders.

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

- Empty input list.

- All orders cancelled.

- Mixed cancelled and non-cancelled orders.

- Orders with zero or negative amounts.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- Incorrectly states that cancelled orders are excluded from the calculation when they are still included in the denominator.

### Rewritten explanation

- This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. Cancelled orders are excluded from both the total and the count. If no valid orders are present, the function returns 0.0 to avoid division by zero.

## 4) Final Judgment

- Decision: Reject
- Justification: The core logic produces incorrect results due to a denominator mismatch and unsafe handling of empty input.
- Confidence & unknowns: High confidence in the identified issues and proposed fix. Input schema assumptions remain minimal by design.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- Presence of "@" alone is not sufficient to classify an email as valid.

- Non-string inputs can raise runtime errors.

### Edge cases & risks

- Strings like "@", "user@", or "@domain" are incorrectly counted as valid.

- Mixed-type inputs are not handled safely.

### Code quality / design issues

- Validation logic is overly simplistic and misleading given the function name.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Ensure inputs are strings.

- Perform basic structural checks on local and domain parts without attempting full RFC validation.

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

- Empty list input.

- Mixed data types (None, integers, objects).

- Clearly invalid email formats.

- Typical valid email formats.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- Overstates correctness by claiming full validity checking.

- Fails to mention limitations of the validation approach.

### Rewritten explanation

- This function counts the number of email addresses that meet a basic validity heuristic. It verifies that each entry is a string, contains an “@” separator, has a non-empty local part, and includes a dot in the domain portion. This approach provides a safe and minimal check without attempting full RFC-level validation.

## 4) Final Judgment

- Decision: Reject
- Justification: The original implementation does not meet its stated goal and can misclassify invalid data.
- Confidence & unknowns: High confidence in findings. Full RFC compliance is intentionally out of scope.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- The denominator includes invalid and missing values, resulting in an incorrect average.

- Unsafe float conversion can raise runtime exceptions.

### Edge cases & risks

- Empty input list.

- All values being None or non-numeric.

- Mixed numeric and non-numeric inputs.

### Code quality / design issues

- Logical inconsistency between numerator and denominator.

- Overly optimistic assumptions about input types.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Count only successfully parsed numeric values.

- Safely ignore None and non-numeric inputs.

- Avoid division by zero.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

- Empty input.

- All values invalid.

- Mixed numeric strings and numeric types.

- Negative and zero values.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- Claims accurate averaging despite an incorrect denominator.

- Overstates safety of mixed-type handling.

### Rewritten explanation

- This function calculates the average of valid numeric measurements by converting each value to a float and ignoring None or non-numeric inputs. The average is computed using only successfully processed values. If no valid measurements are found, the function returns 0.0 to avoid division by zero.

## 4) Final Judgment

- Decision: Reject
- Justification: The original code produces incorrect results and is unsafe for mixed inputs.
- Confidence & unknowns: High confidence in the fix. Behavior for extreme numeric values follows standard Python float semantics.
