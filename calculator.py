
# Importing Streamlit
import streamlit as st

# Defining the basic calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit UI for the calculator
def calculator():
    st.title("Simple Calculator")
    
    # Selection of the operation
    operation = st.selectbox("Choose an operation:", ['Add', 'Subtract', 'Multiply', 'Divide'])
    
    # Inputs for numbers
    num1 = st.number_input("Enter the first number", step=1.0, format="%.2f")
    num2 = st.number_input("Enter the second number", step=1.0, format="%.2f")
    
    # Result based on the selected operation
    if st.button("Calculate"):
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        st.success(f"The result is: {result}")

# Running the calculator function in Streamlit
if __name__ == '__main__':
    calculator()

