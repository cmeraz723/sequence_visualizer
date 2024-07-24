import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the variable
n = sp.symbols('n')

# Function to calculate the nth term of the sequence based on user's choice
def sequence_term(n, formula):
    try:
        expr = sp.sympify(formula)
        result = expr.subs(sp.symbols('n'), n)
        return float(result)
    except (sp.SympifyError, TypeError):
        return 0

st.title("Sequence Visualizer")

# User input for choosing predefined sequences or custom formula
sequence_option = st.radio(
    "Choose a sequence type or input a custom formula",
    ("Predefined sequence", "Custom formula")
)

# Predefined sequences
predefined_sequences = {
    "1/n": "1/n",
    "1/n^2": "1/n^2",
    "(-1)^n / n": "(-1)^n / n",
    "2^n": "2^n",
    "n^2": "n^2",
    "sqrt(n)": "sqrt(n)"
}

if sequence_option == "Predefined sequence":
    sequence_type = st.selectbox("Choose a sequence type", list(predefined_sequences.keys()))
    formula = predefined_sequences[sequence_type]
else:
    formula = st.text_input("Enter the formula for the nth term (use 'n' as the variable)", "1/n^2")

# Range of n values
n_start = st.number_input("Start of range", min_value=1, value=1)
n_end = st.number_input("End of range", min_value=2, value=20)
n_step = st.number_input("Step size", min_value=1, value=1)

# Generate sequence terms
n_values = np.arange(n_start, n_end + 1, n_step)
terms = [sequence_term(i, formula) for i in n_values]

# Plotting
fig, ax = plt.subplots()
ax.plot(n_values, terms, marker='o', linestyle='-', color='b')
ax.set_title(f'Sequence: {formula}')
ax.set_xlabel('n')
ax.set_ylabel('a_n')
ax.grid(True)

# Display the plot
st.pyplot(fig)
