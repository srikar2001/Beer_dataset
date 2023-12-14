# FINAL 
import streamlit as st
import pandas as pd
import altair as alt

# Load beer data from CSV
file_path = 'cleaned_beer.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# Streamlit app
st.set_page_config(
    page_title="Beer Data Visualization",
    page_icon="🍺",
    layout="wide"
)

# Introduction to the dataset
st.title("Beer Dataset Exploration")
st.markdown(
    "This Streamlit app allows you to explore and visualize the beer dataset. "
    "The dataset contains information about various beers, including their Alcohol By Volume (ABV), "
    "International Bitterness Unit (IBU), brewery details, and more. Select different charts from below and filter it from the ☰ Menu on the left."
)

# Sidebar menu
menu_options = ['Charts', 'Data Summary']
selected_option = st.sidebar.selectbox('☰ Menu', menu_options)

# Use st.session_state to keep track of the selected option
if 'selected_styles' not in st.session_state:
    st.session_state.selected_styles = []

# Display different options based on the selected menu
st.sidebar.markdown("---")

if selected_option == 'Charts':
    st.sidebar.subheader('Filter by Beer Style')
    selected_styles = st.sidebar.multiselect('Select Beer Styles', df['style'].unique())
    st.session_state.selected_styles = selected_styles

    # Filter data based on selected beer styles
    filtered_df = df[df['style'].isin(st.session_state.selected_styles)] if st.session_state.selected_styles else df

    # Create tabs for Charts
    chart_tab_titles = ['Scatter Plot', 'Bar Chart-1', 'Bar Chart-2']
    chart_tabs = st.tabs(chart_tab_titles)

    # Add content to the Scatter Plot tab
    with chart_tabs[0]:
        st.header('Scatter Plot (ABV vs IBU Scatter Plot) ')
        st.write('This scatter plot visualizes the relationship between Alcohol By Volume (ABV) and International Bitterness Unit (IBU) with bubble sizes representing ounces. Hover over bubbles to see details.')

        # Create a scatter plot using Altair with size variation
        scatter_chart = alt.Chart(filtered_df).mark_circle().encode(
            x='abv:Q',
            y='ibu:Q',
            size='ounces:Q',
            color='style:N',
            tooltip=['name:N', 'brewery_idbrewery_:N', 'city:N', 'state:N']
        ).properties(
            title=' ',
            width=500,  # Adjust the width as needed
            height=600  # Adjust the height as needed
        )

        # Display Altair chart using Streamlit
        st.altair_chart(scatter_chart, use_container_width=True)

    # Add content to the Bar Chart-1 tab
    with chart_tabs[1]:
        st.header('Bar Chart (Average ABV by Beer Style)')
        st.write('Displaying the average ABV for each beer style. This provides an overview of the alcohol content across different styles.')
        
        # Calculate average ABV by beer style
        avg_abv_by_style = filtered_df.groupby('style')['abv'].mean().reset_index()

        # Create a bar chart using Altair
        bar_chart = alt.Chart(avg_abv_by_style).mark_bar().encode(
            x=alt.X('style:N', title='Beer Style'),
            y=alt.Y('abv:Q', title='Average ABV'),
            tooltip=['style:N', 'abv:Q']
        ).properties(
            title=' ',
            width=500,  # Adjust the width as needed
            height=600  # Adjust the height as needed
        )

        # Display Altair chart using Streamlit
        st.altair_chart(bar_chart, use_container_width=True)

    # Add content to the Bar Chart-2 tab
    with chart_tabs[2]:
        st.header('Bar Chart (Total Ounces by Beer Style)')
        st.write('Displaying the total ounces for each beer style. This provides an overview of the size of different beer styles.')
        
        # Calculate total ounces by beer style
        total_ounces_by_style = filtered_df.groupby('style')['ounces'].sum().reset_index()

        # Create a bar chart using Altair
        total_ounces_chart = alt.Chart(total_ounces_by_style).mark_bar().encode(
            x=alt.X('style:N', title='Beer Style'),
            y=alt.Y('ounces:Q', title='Total Ounces'),
            tooltip=['style:N', 'ounces:Q']
        ).properties(
            title=' ',
            width=500,  # Adjust the width as needed
            height=600  # Adjust the height as needed
        )

        # Display Altair chart using Streamlit
        st.altair_chart(total_ounces_chart, use_container_width=True)

# Data Summary tab
elif selected_option == 'Data Summary':
    st.sidebar.subheader('Data Summary')

    # Total number of rows and columns
    st.sidebar.write(f"📊 Total Rows: {df.shape[0]}")
    st.sidebar.write(f"📊 Total Columns: {df.shape[1]}")

    # Top beer style
    top_beer_style = df['style'].value_counts().idxmax()
    st.sidebar.write(f"🏆 Top Beer Style: {top_beer_style}")

    # Highest ABV beer
    highest_abv_beer = df.loc[df['abv'].idxmax(), 'name']
    st.sidebar.write(f"⬆️ Highest ABV Beer: {highest_abv_beer}")

    # Lowest ABV beer
    lowest_abv_beer = df.loc[df['abv'].idxmin(), 'name']
    st.sidebar.write(f"⬇️ Lowest ABV Beer: {lowest_abv_beer}")

    # Highest IBU beer
    highest_ibu_beer = df.loc[df['ibu'].idxmax(), 'name']
    st.sidebar.write(f"⬆️ Highest IBU Beer: {highest_ibu_beer}")

    # Lowest IBU beer
    lowest_ibu_beer = df.loc[df['ibu'].idxmin(), 'name']
    st.sidebar.write(f"⬇️ Lowest IBU Beer: {lowest_ibu_beer}")

    # Display the dataset on the left side
    st.subheader('Raw Beer Data')
    st.dataframe(df)
