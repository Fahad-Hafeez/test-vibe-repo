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
    # Security vulnerability: SQL injection
    query = f"UPDATE users SET balance = balance - {amount} WHERE id = {user_id}"
    db.execute(query)
    return True
 
def normal_function(x, y):
    # This won't be detected (no @vibe decorator)
    return x + y + 4 *2