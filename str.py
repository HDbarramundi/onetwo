import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def expression(TAN, Salinity, Temp, pH):
    return TAN / (1 + 10**(9.242 + 0.0025*Salinity + 0.034*(24.85 - Temp) - pH))

# Generate sample data
TAN_values = np.arange(0.00, 15.95, 0.05)
Salinity_values = np.arange(0, 63.80, 0.2)
Temp_values = np.arange(0, 63.8, 0.2)
pH_values = np.arange(0, 14, 0.045)

# Streamlit app
st.title('Ammonia vs Variables')

# Select variables
selected_variable = st.selectbox('Select Variable', ['Salinity', 'Temperature', 'TAN', 'pH'])

# Plot the selected variable against Ammonia
fig, ax = plt.subplots()
if selected_variable == 'Salinity':
    ax.plot(Salinity_values, expression(TAN_values[2], Salinity_values, Temp_values[29], pH_values[7]), label='Salinity')
    ax.set_xlabel('Salinity')
elif selected_variable == 'Temperature':
    ax.plot(Temp_values, expression(TAN_values[2], Salinity_values[10], Temp_values, pH_values[7]), label='Temperature')
    ax.set_xlabel('Temperature')
elif selected_variable == 'TAN':
    ax.plot(TAN_values, expression(TAN_values, Salinity_values[10], Temp_values[29], pH_values[7]), label='TAN')
    ax.set_xlabel('TAN')
elif selected_variable == 'pH':
    ax.plot(pH_values, expression(TAN_values[2], Salinity_values[10], Temp_values[29], pH_values), label='pH')
    ax.set_xlabel('pH')

# Set labels and title
ax.set_ylabel('Ammonia')
ax.set_title('Ammonia vs ' + selected_variable)
ax.legend()
ax.grid(True)

# Show the plot in Streamlit
st.pyplot(fig)
