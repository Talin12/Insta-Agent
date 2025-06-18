import streamlit as st
import requests
from streamlit_lottie import st_lottie  # Make sure this is installed: pip install streamlit-lottie
from components.input_form import input_form

# Function to load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    # Lottie animation at the top
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"  # Example: social media animation
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=180, key="header_anim")

    # Simple header using standard Streamlit
    st.markdown("## AI Instagram Post Generator")
    st.markdown("Generate catchy captions, hashtags, and CTAs for your clothing brand!")

    # Tabs for organization
    tab1, tab2 = st.tabs(["Generate Post", "About / Help"])

    with tab1:
        product_name, features, style_example, generate = input_form()

        if generate:
            if not product_name or not features or not style_example:
                st.error("Please fill in all fields before generating.")
            else:
                with st.spinner("Generating..."):
                    try:
                        response = requests.post(
                            "http://localhost:8081/generate",
                            json={
                                "product_name": product_name,
                                "features": features,
                                "style_example": style_example
                            }
                        )
                        if response.status_code == 200:
                            result = response.json().get("result", "No result found")
                            st.success("Generated Caption:")
                            st.write(result)
                            st.balloons()  # Celebrate after successful generation!
                        else:
                            st.error(f"Error: {response.text}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Request failed: {e}")

        # Collapsible section for future advanced options
        with st.expander("Advanced Options (coming soon)"):
            st.write("Here you can add more customization options in the future.")

    with tab2:
        st.markdown("""
        **About this tool:**  
        This AI-powered agent generates Instagram captions, hashtags, and calls to action for your clothing products.  
        Enter your product details and style preferences, and get a ready-to-use caption instantly!

        **Tips:**  
        - Use clear, descriptive product features for best results.
        - Paste a real Instagram caption you like as a style example for more personalized output.
        """)

if __name__ == "__main__":
    main()
