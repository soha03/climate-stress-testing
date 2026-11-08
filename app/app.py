import streamlit as st

st.set_page_config(
    page_title="Climate Stress Testing",
    page_icon="📊",
    layout="wide",
)

st.title("Climate Stress Testing")

st.markdown(
    """
    ### Quantifying the impact of climate and energy shocks
    on corporate financial performance and credit losses.
    """
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Companies", "5")

with col2:
    st.metric("Region", "Europe")

with col3:
    st.metric("Status", "Development")

st.divider()

st.subheader("Model transmission")

st.markdown(
    """
    **Climate / energy shock**

    ↓

    **Revenue and operating costs**

    ↓

    **EBITDA / EBIT**

    ↓

    **Leverage and interest coverage**

    ↓

    **Probability of Default**

    ↓

    **Expected Credit Loss**
    """
)

st.info(
    "The model and data pipeline are currently under development."
)
