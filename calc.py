import math

def evaluate_expression(expression):
    """Evaluates a mathematical expression and returns the result"""
    try:
        return eval(expression, {"__builtins__": None}, {"sin": math.sin, "cos": math.cos, "tan": math.tan, "sqrt": math.sqrt, "log": math.log, "log10": math.log10, "exp": math.exp})
    except:
        return "Invalid expression"

if __name__ == "__main__":
    expression = input("Enter an expression: ")
    result = evaluate_expression(expression)
    print("Result:", result)
