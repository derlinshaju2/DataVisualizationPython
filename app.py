import streamlit as st
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Weather Data Visualization")
st.title("Weekly Temperature Analysis")

# Your Data
days = [1, 2, 3, 4, 5, 6, 7]
max_t = [50, 51, 52, 48, 47, 49, 46]
min_t = [43, 42, 40, 44, 33, 35, 37]
avg_t = [45, 48, 48, 46, 40, 42, 41]

# --- Chart 1: Maximum Temperature ---
st.subheader("Maximum Temperature per Day")
fig1, ax1 = plt.subplots()
ax1.plot(days, max_t, color='red', marker='*', linestyle='--')
ax1.set_xlabel("Days")
ax1.set_ylabel("Temperature")
ax1.grid(True, linestyle=':', alpha=0.6)
st.pyplot(fig1)

# --- Chart 2: Multi-line Comparison ---
st.subheader("Full Temperature Comparison")
fig2, ax2 = plt.subplots()
ax2.plot(days, max_t, label="Max", color="red", marker='o')
ax2.plot(days, min_t, label="Min", color="blue", marker='o')
ax2.plot(days, avg_t, label="Avg", color="green", marker='o')

ax2.set_xlabel("Days")
ax2.set_ylabel("Temperature")
ax2.legend()
ax2.grid(True, linestyle=':', alpha=0.6)
st.pyplot(fig2)
