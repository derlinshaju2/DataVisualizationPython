import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Visualization Dashboard")

# Navigation Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Temperature Analysis", "Home Rent Analysis", "Customer Demographics"])

# --- PAGE 1: TEMPERATURE ANALYSIS ---
if page == "Temperature Analysis":
    st.title("Weather Data Visualization")
    
    days = [1, 2, 3, 4, 5, 6, 7]
    max_t = [50, 51, 52, 48, 47, 49, 46]
    min_t = [43, 42, 40, 44, 33, 35, 37]
    avg_t = [45, 48, 48, 46, 40, 42, 41]

    st.subheader("Temperature Trends (Max, Min, Avg)")
    fig, ax = plt.subplots()
    ax.plot(days, max_t, 'b*--', label='Max Temp')
    ax.plot(days, min_t, 'k*--', label='Min Temp')
    ax.plot(days, avg_t, 'yd--', label='Avg Temp')
    ax.set_xlabel("Days")
    ax.set_ylabel("Temperature")
    ax.legend()
    st.pyplot(fig)

# --- PAGE 2: HOME RENT ANALYSIS ---
elif page == "Home Rent Analysis":
    st.title("Home Rent vs Area")
    
    # Manually creating data since the CSV won't be on the server initially
    data = {
        'area': [2600, 3000, 3200, 3600, 4000],
        'price': [550000, 565000, 610000, 680000, 725000]
    }
    df = pd.DataFrame(data)
    
    st.write("Current Dataset:", df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Line Plot")
        fig1, ax1 = plt.subplots()
        ax1.plot(df['area'], df['price'], 'bd--')
        st.pyplot(fig1)
        
    with col2:
        st.subheader("Scatter Plot")
        fig2, ax2 = plt.subplots()
        ax2.scatter(df['area'], df['price'])
        st.pyplot(fig2)

# --- PAGE 3: CUSTOMER DEMOGRAPHICS ---
elif page == "Customer Demographics":
    st.title("Customer Data Analysis")
    
    # Uploading file option for Streamlit
    uploaded_file = st.file_uploader("Choose the Customers CSV file", type="csv")
    
    if uploaded_file is not None:
        c = pd.read_csv(uploaded_file)
        
        tab1, tab2, tab3 = st.tabs(["Gender Distribution", "Profession Split", "Activity Pie"])
        
        with tab1:
            st.subheader("Gender Distribution")
            p = c['Gender'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(p.values, labels=p.index, autopct='%0.2f%%')
            st.pyplot(fig)
            
        with tab2:
            st.subheader("Profession Analysis")
            d = c['Profession'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(d.values, labels=d.index, autopct='%0.2f%%')
            st.pyplot(fig)
            
        with tab3:
            st.subheader("Daily Activities")
            hour = [6, 7, 2, 5, 4]
            activity = ['study', 'sleep', 'exercise', 'cook', 'run']
            fig, ax = plt.subplots()
            ax.pie(hour, labels=activity, autopct='%0.2f%%')
            st.pyplot(fig)
    else:
        st.info("Please upload the 'Customers.csv' file to see visualizations.")
