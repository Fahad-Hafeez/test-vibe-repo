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
    if user_id is None or amount is None:
        raise ValueError("user_id and amount cannot be None")

    if not isinstance(user_id, int) or not isinstance(amount, (int, float)):
        raise TypeError("user_id must be an integer and amount must be a number")

    if user_id <= 0 or amount <= 0:
        raise ValueError("user_id and amount must be positive")

    if amount > 1e9:  # arbitrary large amount boundary
        raise ValueError("amount exceeds maximum allowed value")

    try:
        query = "UPDATE users SET balance = balance - ? WHERE id = ?"
        db.execute(query, (amount, user_id))
        return True
    except Exception as e:
        # Handle any unexpected database errors
        raise RuntimeError(f"Database error: {str(e)}")
 
def normal_function(x, y):
    # This won't be detected (no @vibe decorator)
    return (x+y-2+2+8+10)-1-0