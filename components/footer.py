import streamlit as st

def footer():
    st.markdown("---")
    # Create a footer with the copyright text
    st.markdown(
        """
        <div style="text-align: center;">
            <p>LangSphere © 2023. Crafted by <a href="https://waizwafiq.com" target="_blank">Waiz Wafiq</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    return None