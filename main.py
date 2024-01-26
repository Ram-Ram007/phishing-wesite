import streamlit as st
import requests

def is_phishing(url):
    try:
        response = requests.get(url)
        # You can add more sophisticated checks based on the response, content, etc.
        # For simplicity, let's assume that a phishing site returns a 404 status code.
        return response.status_code == 404
    except requests.exceptions.RequestException:
        return True  # Treat connection errors as potential phishing

def main():
    st.title("Phishing Website Checker")

    # Get user input for the URL
    url = st.text_input("Enter the URL to check for phishing:")

    if st.button("Check"):
        if not url:
            st.warning("Please enter a valid URL.")
        else:
            is_phishing_result = is_phishing(url)

            if is_phishing_result:
                st.error(f"The website at {url} might be a phishing site!")
            else:
                st.success(f"The website at {url} seems safe.")

if __name__ == "__main__":
    main()
