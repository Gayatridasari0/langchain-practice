from fastmcp import FastMCP

app = FastMCP("math-server")

@app.tool()
def calculator(a: float, b: float, operation: str) -> dict:
    """Perform basic math: add, sub, mul, div"""

    if operation == "add":
        return {"result": a + b}
    elif operation == "sub":
        return {"result": a - b}
    elif operation == "mul":
        return {"result": a * b}
    elif operation == "div":
        if b == 0:
            return {"error": "Division by zero"}
        return {"result": a / b}
    else:
        return {"error": "Invalid operation"}

if __name__ == '__main__':
    app.run()