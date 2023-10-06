import streamlit as st

import plotly.express as px
import pandas as pd

import warnings
from components import footer

warnings.filterwarnings("ignore")

def main():

    st.set_page_config(page_title="VizTrackr", page_icon="📈", layout="wide")
    st.title(" 📈 VizTrackr (In Progress)")
    st.header(" 🔬")
    st.write("""---""")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    df = pd.read_csv("./files/covid-data.csv", encoding="ISO-8859-1")

    col1, col2 = st.columns((2))
    df["date"] = pd.to_datetime(df["date"])

    # Getting the min and max date
    startDate = pd.to_datetime(df["date"]).min()
    endDate = pd.to_datetime(df["date"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    df = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()

    df = df[df["location"] != "World"].copy()
    df = df[df['continent'].notnull()].copy()

    st.sidebar.header("Choose your filter: ")
    continent = st.sidebar.multiselect("Pick Your Continent", df["continent"].unique())
    if not continent:
        df2 = df.copy()
    else:
        df2 = df[df["continent"].isin(continent)].copy()

    location = st.sidebar.multiselect("Pick Your Location", df2["location"].unique())
    if not location:
        df3 = df2.copy()
    else:
        df3 = df2[df2["location"].isin(location)].copy()

    if not continent and not location:
        filtered_df = df
    elif not continent:
        filtered_df = df[df["location"].isin(location)]
    elif not location:
        filtered_df = df[df["continent"].isin(continent)]
    else:
        filtered_df = df3[df3["continent"].isin(continent) & df3['location'].isin(location)]

    # Filter out null continents
    filtered_df = filtered_df[filtered_df['continent'].notnull()]

    filtered_df['month_year'] = filtered_df['date'].dt.to_period('M')

    end_location_df = filtered_df.groupby('location').apply(lambda group: group[group['date'] == group['date'].max()])
    start_location_df = filtered_df.groupby('location').apply(lambda group: group[group['date'] == group['date'].min()])

    end_location_df['total_cases'] = end_location_df['total_cases'].fillna(0)
    start_location_df['total_cases'] = start_location_df['total_cases'].fillna(0)

    end_location_df['total_deaths'] = end_location_df['total_deaths'].fillna(0)
    start_location_df['total_deaths'] = start_location_df['total_deaths'].fillna(0)

    end_location_df = end_location_df.reset_index(drop=True)
    start_location_df = start_location_df.reset_index(drop=True)

    location_df = pd.merge(end_location_df, start_location_df, on='location')

    location_df['total_cases_end'] = location_df['total_cases_x']
    location_df['total_cases_start'] = location_df['total_cases_y']
    location_df['total_cases_change'] = location_df['total_cases_end'] - location_df['total_cases_start']

    location_df['total_deaths_end'] = location_df['total_deaths_x']
    location_df['total_deaths_start'] = location_df['total_deaths_y']
    location_df['total_deaths_change'] = location_df['total_deaths_end'] - location_df['total_deaths_start']

    st.subheader("Analyzing COVID-19 Cases by Location")
    fig = px.bar(location_df, x="location", y="total_cases_change", color="location", template="seaborn")
    # Update the y-axis label
    fig.update_yaxes(title_text="Total Cases")
    fig.update_xaxes(title_text="Country")
    st.plotly_chart(fig, use_container_width=True, height=200)

    # Group by continent and date to sum up the total cases for each country
    continent_total_cases = filtered_df.groupby(['continent', 'date'])['total_cases'].sum().reset_index()

    # Find the latest date for each continent
    end_continent_df = continent_total_cases.groupby('continent').apply(lambda group: group[group['date'] == group['date'].max()])

    # Find the earliest date for each continent
    start_continent_df = continent_total_cases.groupby('continent').apply(lambda group: group[group['date'] == group['date'].min()])

    end_continent_df['total_cases'] = end_continent_df['total_cases'].fillna(0)
    start_continent_df['total_cases'] = start_continent_df['total_cases'].fillna(0)

    end_continent_df = end_continent_df.reset_index(drop=True)
    start_continent_df = start_continent_df.reset_index(drop=True)

    continent_df = pd.merge(end_continent_df, start_continent_df, on='continent')

    continent_df['total_cases_end'] = continent_df['total_cases_x']
    continent_df['total_cases_start'] = continent_df['total_cases_y']
    continent_df['total_cases_change'] = continent_df['total_cases_end'] - continent_df['total_cases_start']

    st.subheader("Analyzing COVID-19 Cases by Continent")
    fig = px.pie(continent_df, values="total_cases_change", names="continent", hole=0.5)
    fig.update_traces(text=continent_df["continent"], textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Exploring the COVID-19 Pandemic through Time Series Analysis')
    monthly_cases = filtered_df.groupby(['month_year', 'location'])['total_cases'].last().reset_index()
    linechart = pd.DataFrame(monthly_cases.groupby(monthly_cases["month_year"].dt.strftime("%Y : %b"))["total_cases"].sum()).reset_index()
    linechart = linechart.sort_values(by="total_cases")
    fig2 = px.line(linechart, x="month_year", y="total_cases", labels={"total_cases": "Cases"}, height=500, width=1000, template="gridon")
    # Update the x-axis label
    fig2.update_xaxes(title_text="Month:Year")

    # Update the y-axis label
    fig2.update_yaxes(title_text="Total Cases")
    st.plotly_chart(fig2, use_container_width=True)

    end_location_df = filtered_df.groupby(['continent', 'location']).apply(lambda group: group[group['date'] == group['date'].max()])
    start_location_df = filtered_df.groupby(['continent', 'location']).apply(lambda group: group[group['date'] == group['date'].min()])

    end_location_df['total_cases'] = end_location_df['total_cases'].fillna(0)
    start_location_df['total_cases'] = start_location_df['total_cases'].fillna(0)

    end_location_df['total_deaths'] = end_location_df['total_deaths'].fillna(0)
    start_location_df['total_deaths'] = start_location_df['total_deaths'].fillna(0)

    end_location_df = end_location_df.reset_index(drop=True)
    start_location_df = start_location_df.reset_index(drop=True)

    location_df = pd.merge(end_location_df, start_location_df, on=['continent', 'location'])

    location_df['total_cases_end'] = location_df['total_cases_x']
    location_df['total_cases_start'] = location_df['total_cases_y']
    location_df['total_cases_change'] = abs(location_df['total_cases_end'] - location_df['total_cases_start'])

    location_df['total_deaths_end'] = location_df['total_deaths_x']
    location_df['total_deaths_start'] = location_df['total_deaths_y']
    location_df['total_deaths_change'] = abs(location_df['total_deaths_end'] - location_df['total_deaths_start'])

    st.subheader("Visualizing Hierarchical Total Deaths with TreeMap: A Global Perspective")

    # Group by continent and location to sum up the total deaths and total cases for each location
    location_total_cases = location_df.groupby(['continent', 'location'])[['total_deaths_change', 'total_cases_change']].sum().reset_index()

    # Filter out rows with zero values
    location_total_cases = location_total_cases[(location_total_cases['total_deaths_change'] != 0) & (location_total_cases['total_cases_change'] != 0)]
    location_total_cases['total_deaths_change'] = location_total_cases['total_deaths_change'].astype(int)

    fig3 = px.treemap(location_total_cases, path=["continent", "location"], values="total_deaths_change",
                    hover_data=["total_deaths_change", "total_cases_change"], color="total_deaths_change")

    # Define a custom hover template with integer formatting
    fig3.update_traces(hovertemplate='Total Deaths: %{customdata[0]:.0f}<br>Total Cases: %{customdata[1]:.0f}')

    fig3.update_layout(width=800, height=650)

    st.plotly_chart(fig3, use_container_width=True)


    footer.footer()

if __name__ == '__main__':  # define code that should only run when the script is executed directly
    main()
