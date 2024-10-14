import streamlit as st
import math

# Function to handle the scientific calculator
def scientific_calculator():
    st.title("Scientific Calculator")
    
    # Display available operations
    operation = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root", 
                                                   "Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Exponential (e^x)"])
    
    # Input for basic arithmetic operations
    if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
        num1 = st.number_input("Enter first number:", value=0.0)
        num2 = st.number_input("Enter second number:", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Addition":
                st.write(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operation == "Subtraction":
                st.write(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operation == "Multiplication":
                st.write(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operation == "Division":
                if num2 != 0:
                    st.write(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    st.write("Error: Division by zero!")
            elif operation == "Power":
                st.write(f"Result: {num1} ^ {num2} = {num1 ** num2}")
    
    # Input for square root
    elif operation == "Square Root":
        num = st.number_input("Enter a number:", value=0.0)
        
        if st.button("Calculate"):
            if num >= 0:
                st.write(f"Result: √{num} = {math.sqrt(num)}")
            else:
                st.write("Error: Cannot take square root of a negative number!")
    
    # Input for trigonometric functions
    elif operation in ["Sine", "Cosine", "Tangent"]:
        angle = st.number_input("Enter angle in degrees:", value=0.0)
        radian = math.radians(angle)
        
        if st.button("Calculate"):
            if operation == "Sine":
                st.write(f"Result: sin({angle}) = {math.sin(radian)}")
            elif operation == "Cosine":
                st.write(f"Result: cos({angle}) = {math.cos(radian)}")
            elif operation == "Tangent":
                st.write(f"Result: tan({angle}) = {math.tan(radian)}")
    
    # Input for logarithm
    elif operation == "Logarithm (base 10)":
        num = st.number_input("Enter a number:", value=1.0)
        
        if st.button("Calculate"):
            if num > 0:
                st.write(f"Result: log10({num}) = {math.log10(num)}")
            else:
                st.write("Error: Logarithm undefined for non-positive numbers!")
    
    # Input for exponential function
    elif operation == "Exponential (e^x)":
        num = st.number_input("Enter a number:", value=0.0)
        
        if st.button("Calculate"):
            st.write(f"Result: e^{num} = {math.exp(num)}")

# Main function to run the app
if __name__ == '__main__':
    scientific_calculator()

