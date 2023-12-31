import plotly.express as px
import streamlit as st
from components.streamlit_plotly_events.src import st_plotly_events

st.set_page_config(
    page_title="React Plotly events component",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def get_plotly_events(fig):
    return st_plotly_events(
        fig, click_event=True, select_event=True, key="selected_points"
    )


def main():
    st.title("React Plotly events component")

    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        title="Sample Figure",
        template="seaborn",
    )
    fig["layout"]["uirevision"] = True

    value = get_plotly_events(fig)
    plot_value_holder = st.empty()
    plot_value_holder.write(value)


main()
