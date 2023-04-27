import streamlit as st
import pandas as pd
import numpy as np


st.text("hello world")

st.text("hello world 2")

st.text("hello world 3")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)


x = st.slider("Beta", max_value=50, min_value=20)
st.write(x, "squared is ", x*x)


df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})
option = st.selectbox(
    "Which number do you like best?",
    df["first column"]
)
"Your selected: ", option
