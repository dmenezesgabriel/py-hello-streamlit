import random
from datetime import datetime, time

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import streamlit as st
from bokeh.plotting import figure
from plotly import express as px
from vega_datasets import data


def render_text_ui():
    st.title("Hello, World!")

    st.header("This is a header", help="This is a tooltip", divider="rainbow")

    st.markdown(
        """
        This is a :rainbow[Markdown]
        """
    )

    st.subheader(
        "This is a subheader", help="This is a tooltip", divider="gray"
    )

    st.code(
        """
        import streamlit as st

        st.write("Hello, World!")
        """,
        language="python",
        line_numbers=True,
    )

    st.text("This is a text", help="This is a tooltip")

    st.latex(
        r"""
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        """
    )

    st.caption("This is a caption", help="This is a tooltip")

    st.divider()


@st.cache_data
def get_random_stars():
    return [random.randint(0, 1000) for _ in range(3)]


@st.cache_data
def get_random_views_history():
    return [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)]


def render_dataframe_ui():
    st.header("Table", help="This is a tooltip", divider="rainbow")

    st.info("Edit Me!")

    df = pd.DataFrame(
        {
            "name": ["Roadmap", "Extras", "Issues"],
            "url": [
                "https://roadmap.streamlit.app",
                "https://extras.streamlit.app",
                "https://issues.streamlit.app",
            ],
            "stars": get_random_stars(),
            "views_history": get_random_views_history(),
            "isActive": [True, False, True],
            "widgets": ["🗺", "🎁", "🐞"],
            "category": [
                "📊 Data Exploration",
                "📈 Data Visualization",
                "📊 Data Exploration",
            ],
            "appointment": [
                datetime(2024, 2, 5, 12, 30),
                datetime(2023, 11, 10, 18, 0),
                datetime(2024, 3, 11, 20, 10),
            ],
            "time": [
                time(12, 30),
                time(18, 0),
                time(9, 10),
            ],
            "images": [
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            ],
            "sales": [200, 550, 1000],
        }
    )

    edited_df = st.data_editor(
        df,
        column_config={
            "name": st.column_config.TextColumn(
                "App name",
                validate="^[a-z]",
                help="Only String characters are allowed",
            ),
            "stars": st.column_config.NumberColumn(
                "Github stars",
                help="This is a tooltip",
                format="%d ⭐",
            ),
            "url": st.column_config.LinkColumn(
                "App URL", help="This is a tooltip"
            ),
            "views_history": st.column_config.LineChartColumn(
                "Views history (past 30 days)",
                y_min=0,
                y_max=5000,
                help="This is a tooltip",
            ),
            "widgets": st.column_config.Column(
                "Icons",
                help="Help 🎈",
                width="medium",
            ),
            "category": st.column_config.SelectboxColumn(
                "select option",
                options=[
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "📊 Data Exploration",
                ],
                help="This is a tooltip",
            ),
            "appointment": st.column_config.DatetimeColumn(
                "datetime",
                min_value=datetime(2021, 1, 1),
                max_value=datetime(2025, 1, 1),
                format="YYYY/MM/DD - hh:mm",
                help="This is a tooltip",
            ),
            "time": st.column_config.TimeColumn(
                "time",
                min_value=time(0, 0),
                max_value=time(23, 59),
                format="hh:mm a",
                help="This is a tooltip",
            ),
            "images": st.column_config.ImageColumn(
                "images",
                help="This is a tooltip",
            ),
            "sales": st.column_config.ProgressColumn(
                "sales",
                min_value=0,
                max_value=1000,
                format="$%f",
                help="This is a tooltip",
            ),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic",
        key="editor",
    )

    st.text("output (dataframe):")
    st.dataframe(edited_df)
    st.text("output (static table):")
    st.table(edited_df)


def render_json_ui():
    st.header("JSON", help="This is a tooltip", divider="gray")
    st.json(
        {
            "foo": "bar",
            "baz": "boz",
            "stuff": [
                "stuff 1",
                "stuff 2",
                "stuff 3",
                "stuff 5",
            ],
        }
    )


def render_metric_ui():
    st.header("Metrics", help="This is a tooltip", divider="blue")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Temperature", value="70 °F", delta="2 °F")
    with col2:
        st.metric(label="Humidity", value="50 %", delta="5 %")
    with col3:
        st.metric(label="Pressure", value="1000 hPa", delta="10 hPa")
    with col4:
        st.metric(label="Wind", value="10 km/h", delta="2 km/h")


@st.cache_data
def get_random_chart_data():
    return pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"],
    )


def render_chart_ui():
    st.header("Native Charts", help="This is a tooltip", divider="violet")
    chart_data = get_random_chart_data()

    with st.expander("data"):
        st.dataframe(chart_data)

    st.subheader("Line Chart")
    st.line_chart(chart_data)
    st.subheader("Area Chart")
    st.area_chart(chart_data)
    st.subheader("Bar Chart")
    st.bar_chart(chart_data)


def render_matplotlib_ui():
    st.header("Matplotlib", help="This is a tooltip", divider="green")

    col1, col2, col3 = st.columns(3)

    arr = np.random.normal(1, 1, size=100)
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20)

    with col1:
        st.pyplot(fig, clear_figure=True, use_container_width=True)


def render_altair_basic_ui():
    st.header("Altair", help="This is a tooltip", divider="red")

    chart_data = get_random_chart_data()

    chart = (
        alt.Chart(chart_data)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )

    st.altair_chart(chart, use_container_width=True)

    # Theme

    source = data.cars()

    with st.expander("data"):
        st.dataframe(source)

    chart = (
        alt.Chart(source)
        .mark_circle()
        .encode(x="Horsepower", y="Miles_per_Gallon", color="Origin")
    ).interactive()

    tab1, tab2 = st.tabs(["Streamlit native theme", "Altair native theme"])

    with tab1:
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        st.altair_chart(chart, theme=None, use_container_width=True)


def render_altair_advanced_ui():
    st.header("Altair advanced", help="This is a tooltip", divider="red")

    source = data.seattle_weather()

    with st.expander("data"):
        st.dataframe(source)

    scale = alt.Scale(
        domain=["sun", "fog", "drizzle", "rain", "snow"],
        range=["#e7ba52", "#c7c7c7", "#aec7e8", "#1f77b4", "#9467bd"],
    )

    color = alt.Color("weather:N", scale=scale)
    brush = alt.selection_interval(encodings=["x"])
    click = alt.selection_multi(encodings=["color"])

    points = (
        alt.Chart()
        .mark_point()
        .encode(
            alt.X("monthdate(date):T", title="Date"),
            alt.Y(
                "temp_max:Q",
                title="Maximum Daily Temperature(C)",
                scale=alt.Scale(domain=[-5, 40]),
            ),
            color=alt.condition(brush, color, alt.value("lightgray")),
            size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
        )
        .properties(width=600, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )

    bars = (
        alt.Chart()
        .mark_bar()
        .encode(
            x="count()",
            y="weather:N",
            color=alt.condition(click, color, alt.value("lightgray")),
        )
        .transform_filter(brush)
        .properties(width=600)
        .add_selection(click)
    )

    chart = alt.vconcat(
        points, bars, data=source, title="Seattle Weather: 2012-2015"
    )

    st.altair_chart(chart, theme="streamlit", use_container_width=True)


def render_vega_lite_ui():
    st.header("Vega Lite", help="This is a tooltip", divider="gray")

    st.write(
        "Vega-Lite is a high-level grammar of interactive graphics. It comes bundled with the Python API of Altair."
    )

    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

    st.vega_lite_chart(
        chart_data,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "a", "type": "quantitative"},
                "y": {"field": "b", "type": "quantitative"},
                "size": {"field": "c", "type": "quantitative"},
                "color": {"field": "c", "type": "quantitative"},
            },
        },
    )

    # Theme
    source = data.cars()

    chart = {
        "mark": "point",
        "encoding": {
            "x": {
                "field": "Horsepower",
                "type": "quantitative",
            },
            "y": {
                "field": "Miles_per_Gallon",
                "type": "quantitative",
            },
            "color": {"field": "Origin", "type": "nominal"},
            "shape": {"field": "Origin", "type": "nominal"},
        },
    }

    tab1, tab2 = st.tabs(
        ["Streamlit theme (default)", "Vega-Lite native theme"]
    )

    with tab1:
        # Use the Streamlit theme.
        # This is the default. So you can also omit the theme argument.
        st.vega_lite_chart(
            source, chart, theme="streamlit", use_container_width=True
        )
    with tab2:
        st.vega_lite_chart(source, chart, theme=None, use_container_width=True)


def render_plotly_ui():
    st.header("Plotly", help="This is a tooltip", divider="gray")

    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]

    group_labels = ["Group 1", "Group 2", "Group 3"]

    fig = ff.create_distplot(
        hist_data,
        group_labels,
        bin_size=[0.1, 0.25, 0.5],
    )

    st.plotly_chart(fig, use_container_width=True)

    #  Theme
    df = px.data.gapminder()

    fig = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )

    tab1, tab2 = st.tabs(["Streamlit theme", "Plotly native theme"])

    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)

    df = px.data.iris()

    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale="reds",
    )

    tab1, tab2 = st.tabs(["Streamlit theme", "Plotly native theme"])

    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)


def render_bokeh_ui():
    st.header("Bokeh", help="This is a tooltip", divider="gray")

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]

    p = figure(
        title="simple line example",
        x_axis_label="x",
        y_axis_label="y",
    )

    p.line(x, y, legend_label="Temp.", line_width=2)

    st.bokeh_chart(p, use_container_width=True)


def render_input_widgets_ui():
    st.header("Input Widgets", help="This is a tooltip", divider="gray")

    st.subheader("Button")

    tab1, tab2, tab3, tab4, tab5 = st.columns(5)

    with tab1:
        st.button(
            "Click me",
            type="primary",
            help="This is a tooltip",
            key="btn-pimary",
        )
    with tab2:
        st.button(
            "Click me",
            type="secondary",
            help="This is a tooltip",
            key="btn-secondary",
        )
    with tab3:
        st.button(
            "Click me",
            disabled=True,
            help="This is a tooltip",
            key="btn-disabled",
        )

    st.subheader("Checkbox")
    st.checkbox("Check me out")

    st.subheader("Radio")
    st.radio("Radio", ["foo", "bar", "baz"])

    st.subheader("Selectbox")
    st.selectbox("Selectbox", ["foo", "bar", "baz"])

    st.subheader("Multiselect")
    st.multiselect("Multiselect", ["foo", "bar", "baz"])

    st.subheader("Slider")
    st.slider("Slider")

    st.subheader("Text Input")
    st.text_input("Text Input")

    st.subheader("Number Input")
    st.number_input("Number Input")

    st.subheader("Text Area")
    st.text_area("Text Area")

    st.subheader("Date Input")
    st.date_input("Date Input")

    st.subheader("Time Input")
    st.time_input("Time Input")

    st.subheader("File Uploader")
    st.file_uploader("File Uploader")

    st.subheader("Color Picker")
    st.color_picker("Color Picker")