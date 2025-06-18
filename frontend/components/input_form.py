import streamlit as st

def input_form():
    st.markdown("### Enter Product Details")
    product_name = st.text_input("Product Name", help="E.g., Summer Floral Dress")
    features = st.text_area("Product Features/Details", help="List key features or details")

    style_options = ["Funky", "Professional", "Eye-catching", "Trendy", "Minimalist", "Playful"]

    # Arrange options in two columns
    col1, col2 = st.columns(2)
    selected_style = st.session_state.get("selected_style", style_options[0])

    # Helper function to render a bubble button
    def bubble_button(label, col):
        if col.button(label, key=label):
            st.session_state["selected_style"] = label

    # Place buttons in two columns
    for i, style in enumerate(style_options):
        if i % 2 == 0:
            bubble_button(style, col1)
        else:
            bubble_button(style, col2)

    # Show which style is selected
    selected_style = st.session_state.get("selected_style", style_options[0])
    st.markdown(f"**Selected Style:** `{selected_style}`")

    generate = st.button("Generate Post")
    return product_name, features, selected_style, generate
