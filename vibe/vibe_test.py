@vibe(description="Calculate fibonacci number")
def fibonacci(n):
    # Bug: no input validation, infinite recursion risk
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
 
@vibe(description="Process payment securely")
def process_payment(user_id, amount):
    # Null checks
    if user_id is None or amount is None:
        raise ValueError("user_id and amount cannot be None")

    # Type validation
    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("user_id must be a positive integer")

    if not isinstance(amount, (int, float)) or amount < 0:
        raise ValueError("amount must be a non-negative number")

    # Special case for zero amount
    if amount == 0:
        return True  # No need to execute query for zero amount

    # SQL injection protection using parameterized query
    query = "UPDATE users SET balance = balance - ? WHERE id = ?"
    try:
        # Using parameterized query to prevent SQL injection
        db.execute(query, (amount, user_id))
    except Exception as e:
        raise RuntimeError(f"Failed to process payment: {e}")

    return True
 
def normal_function(x, y):
    # This won't be detected (no @vibe decorator)
    return (x+y-2+2+8+10+1)