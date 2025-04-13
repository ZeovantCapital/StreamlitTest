
import streamlit as st

def main():
    st.set_page_config(page_title="My Awesome  ", layout="centered")
    st.title("Welcome to My Pet Gallery! :cat:")

    # Fun intro text
    # Create columns for side-by-side images
    col1, col2 = st.columns(2)
    with col1:
        st.image("pet1.jpg", use_column_width=True)
    with col2:
        st.image("pet2.jpg", use_column_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image("pet3.jpg", use_column_width=True)
    with col4:
        st.image("pet4.jpg", use_column_width=True)


if __name__ == "__main__":
    main()

