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
        raise ValueError("User ID and amount cannot be None")

    if not isinstance(user_id, int) or user_id <= 0:
        raise ValueError("User ID must be a positive integer")

    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number")

    try:
        query = "UPDATE users SET balance = balance - ? WHERE id = ?"
        db.execute(query, (amount, user_id))
        return True
    except Exception as e:
        # Handle the exception, potentially log it
        print(f"An error occurred: {e}")
        return False
 
def normal_function(x, y):
    # This won't be detected (no @vibe decorator)
    return (x+y-2+2+8+10)-1-0