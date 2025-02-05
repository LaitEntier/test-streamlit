import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the dashboard
st.title("Basic Interactive Dashboard")

# Load some data
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'x': range(1, 101),
        'y': [i**2 for i in range(1, 101)]
    })
    return data

data = load_data()

# Display the data
st.write("Here's the dataset:")
st.write(data)

# Add a slider for interactive filtering
st.sidebar.header("Filter Data")
x_min = st.sidebar.slider("Minimum X value", min_value=int(data['x'].min()), max_value=int(data['x'].max()), value=int(data['x'].min()))
x_max = st.sidebar.slider("Maximum X value", min_value=int(data['x'].min()), max_value=int(data['x'].max()), value=int(data['x'].max()))

# Filter the data based on the slider values
filtered_data = data[(data['x'] >= x_min) & (data['x'] <= x_max)]

# Display the filtered data
st.write(f"Filtered Data (X between {x_min} and {x_max}):")
st.write(filtered_data)

# Plot the filtered data
st.write("Plot of Filtered Data:")
fig, ax = plt.subplots()
ax.plot(filtered_data['x'], filtered_data['y'], marker='o')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("X vs Y")
st.pyplot(fig)