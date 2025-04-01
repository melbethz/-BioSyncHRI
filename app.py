import streamlit as st

# Title for the app
st.title("VR Console View BioSyncHRI")

# Instructions for the user
st.write("Please choose your view:")

# Provide the options for selection
view_option = st.radio("Select a view", ("Surgeon's View", "Robot's View"))

# Display the corresponding video based on the user's choice
if view_option == "Surgeon's View":
    st.write("Playing Surgeon's View video...")
    st.video("video1.mp4")  # Ensure this file is in your repository
elif view_option == "Robot's View":
    st.write("Playing Robot's View video...")
    st.video("video2.mp4")  # Ensure this file is in your repository
