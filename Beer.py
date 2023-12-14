# import streamlit as st
# import pandas as pd
# import altair as alt

# # Load beer data from CSV
# file_path = 'cleaned_beer.csv'  # Update with your actual file path
# df = pd.read_csv(file_path)

# # Streamlit app
# st.set_page_config(
#     page_title="Beer Data Visualization",
#     page_icon="🍺",
#     layout="wide"
# )

# # Introduction to the dataset
# st.title("Beer Dataset Exploration")
# st.markdown(
#     "This Streamlit app allows you to explore and visualize the beer dataset. "
#     "The dataset contains information about various beers, including their Alcohol By Volume (ABV), "
#     "International Bitterness Unit (IBU), brewery details, and more. Select different charts from the menu on the left."
# )

# # Sidebar menu
# menu_options = ['Select Chart', 'Raw Data', 'Summary Statistics', 'Data Insights']
# selected_option = st.sidebar.selectbox('☰ Menu', menu_options)

# # Use st.session_state to keep track of the selected option
# if 'selected_option' not in st.session_state:
#     st.session_state.selected_option = 'Select Chart'

# # Slider for the number of rows in summary statistics
# if st.session_state.selected_option == 'Summary Statistics':
#     num_rows = st.sidebar.slider('Number of Rows for Summary Statistics', min_value=1, max_value=len(df), value=10)

# # Display different options based on the selected menu
# st.sidebar.markdown("---")

# if selected_option == 'Select Chart':
#     st.sidebar.subheader('Select Chart Type')
#     selected_chart = st.sidebar.radio('Chart Type', ['Scatter Plot', 'Bar Chart'])
    
#     # Main content on the right
#     st.subheader('ABV vs IBU Scatter Plot')
#     st.markdown(
#         "This scatter plot visualizes the relationship between Alcohol By Volume (ABV) and "
#         "International Bitterness Unit (IBU) with bubble sizes representing ounces. "
#         "Hover over bubbles to see details."
#     )
    
#     # Create a scatter plot using Altair with size variation
#     if selected_chart == 'Scatter Plot':
#         scatter_chart = alt.Chart(df).mark_circle().encode(
#             x='abv:Q',
#             y='ibu:Q',
#             size='ounces:Q',
#             color='style:N',  # Add color encoding back
#             tooltip=['name:N', 'brewery_idbrewery_:N', 'city:N', 'state:N']
#         ).properties(
#             title='ABV vs IBU with Size Representing Ounces',
#             width=600,  # Adjust the width as needed
#             height=400  # Adjust the height as needed
#         )
#         # Display Altair chart using Streamlit
#         st.altair_chart(scatter_chart, use_container_width=True)
    
#     # Create a bar chart using Altair
#     elif selected_chart == 'Bar Chart':
#         st.subheader('Average ABV by Beer Style')
        
#         # Calculate average ABV by beer style
#         avg_abv_by_style = df.groupby('style')['abv'].mean().reset_index()
        
#         # Create a bar chart using Altair
#         bar_chart = alt.Chart(avg_abv_by_style).mark_bar().encode(
#             x=alt.X('style:N', title='Beer Style'),
#             y=alt.Y('abv:Q', title='Average ABV'),
#             tooltip=['style:N', 'abv:Q']
#         ).properties(
#             title='Average ABV by Beer Style',
#             width=600,  # Adjust the width as needed
#             height=400  # Adjust the height as needed
#         )
        
#         # Display Altair chart using Streamlit
#         st.altair_chart(bar_chart, use_container_width=True)

# # Save the selected option to session state
# st.session_state.selected_option = selected_option

# # Add a footer with additional information
# st.sidebar.markdown("---")
# st.sidebar.subheader("About")
# st.sidebar.markdown(
#     "This Streamlit app is designed to visualize and explore beer data. "
#     "It provides various charts and insights to analyze the dataset."
# )

# # Display additional charts based on selected tab
# selected_chart_type = st.sidebar.selectbox("Explore", ["Scatter Plot", "Bar Chart", "Other Tab 1", "Other Tab 2"])
# if selected_chart_type == "Scatter Plot":
#     scatter_chart = alt.Chart(df).mark_circle().encode(
#         x='abv:Q',
#         y='ibu:Q',
#         size='ounces:Q',
#         color='style:N',
#         tooltip=['name:N', 'brewery_idbrewery_:N', 'city:N', 'state:N']
#     ).properties(
#         title='ABV vs IBU with Size Representing Ounces',
#         width=600,
#         height=400
#     )
#     st.altair_chart(scatter_chart, use_container_width=True)

# elif selected_chart_type == "Bar Chart":
#     avg_abv_by_style = df.groupby('style')['abv'].mean().reset_index()
#     bar_chart = alt.Chart(avg_abv_by_style).mark_bar().encode(
#         x=alt.X('style:N', title='Beer Style'),
#         y=alt.Y('abv:Q', title='Average ABV'),
#         tooltip=['style:N', 'abv:Q']
#     ).properties(
#         title='Average ABV by Beer Style',
#         width=600,
#         height=400
#     )
#     st.altair_chart(bar_chart, use_container_width=True)

# elif selected_chart_type == "Other Tab 1":
#     # Add code for other tab 1 here
#     st.write("This is Other Tab 1")

# elif selected_chart_type == "Other Tab 2":
#     # Add code for other tab 2 here
#     st.write("This is Other Tab 2")








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
    "International Bitterness Unit (IBU), brewery details, and more. Select different charts from below and filter it from the ☰ Menu. on to the left"
)

# Create tabs
tab_titles = ['Scatter Plot', 'Bar Chart', 'Line Graph']
scatter_tab, bar_chart_tab, line_graph_tab = st.tabs(tab_titles)

# Add content to each tab
with scatter_tab:
    st.header('Scatter Plot (ABV vs IBU Scatter Plot) ')
    st.write('This scatter plot visualizes the relationship between Alcohol By Volume (ABV) and International Bitterness Unit (IBU) with bubble sizes representing ounces. Hover over bubbles to see details.')

with bar_chart_tab:
    st.header('Bar Chart(Average ABV by Beer Style)')
    st.write('Displaying the average ABV for each beer style. This provides an overview of the alcohol content across different styles.')

    # Bar Chart (Average ABV by Beer Style)
    st.subheader('')
    
    # Calculate average ABV by beer style
    avg_abv_by_style = df.groupby('style')['abv'].mean().reset_index()
    
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

with line_graph_tab:
    st.header('Line Graph')
    st.write('Line Graph content goes here')

# Sidebar menu
menu_options = ['Select Chart', 'Data Summary']
selected_option = st.sidebar.selectbox('☰ Menu', menu_options)

# Use st.session_state to keep track of the selected option
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = 'Select Chart'

# Display different options based on the selected menu
st.sidebar.markdown("---")

if selected_option == 'Select Chart':
    st.sidebar.subheader('Filter by Beer Style')
    selected_styles = st.sidebar.multiselect('Select Beer Styles', df['style'].unique())
    
    # Main content on the right
    st.subheader('')
    st.markdown(
        " "
    )
    
    # Filter data based on selected beer styles
    filtered_df = df[df['style'].isin(selected_styles)] if selected_styles else df
    
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

