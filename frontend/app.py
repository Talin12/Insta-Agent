import streamlit as st
import requests

st.title("Instagram Post Generator")

product_name = st.text_input("Product Name")
features = st.text_area("Product Features/Details")
style_example = st.text_area("Style Example (paste a caption you like)")

if st.button("Generate Post"):
    with st.spinner("Generating..."):
        response = requests.post(
            "http://localhost:8080/generate",
            json={
                "product_name": product_name,
                "features": features,
                "style_example": style_example
            }
        )
        if response.status_code == 200:
            st.success("Generated Caption:")
            st.write(response.json()["result"])
        else:
            st.error(f"Error: {response.text}")
