import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plots
import plotly.express as px
import streamlit as st
from PIL import Image


happy = pd.read_csv('/Users/iiiii/Desktop/world-happiness-report-2021.csv')
happy = happy.drop(['Standard error of ladder score', 'Ladder score in Dystopia'], axis = 1)

st.sidebar.title('Sidebar')
selected_box = st.sidebar.selectbox(
    'Select one of the following:',
    ('Start', 'Table Preview', 'Column Explaination', 'Region Distribution', 'How to Use 3D Scatter Plot?', 'Analysis 1', 'Analysis 2', 'Analysis 3', 'Analysis 4', 'Some More Fast Facts', 'Bibliography')
    )


if selected_box == 'Start':
    st.title('World Happiness Report 2021')
    st.markdown('This is the dataset of world happiness report in 2021.')
    st.markdown('I am going to perform a series of data analysis on this dataset, to let you see what data science can really do.')


if selected_box == 'Table Preview':
    st.title('Table Preview')
    happy


if selected_box == 'Column Explaination':
    st.title('Column Explaination')
    head5 = happy.head(5)
    head5
    st.markdown('This is the first 5 lines of the dataset. As you can see, there are many columns, just ignore the column at the end that say "Explained by:".')
    st.markdown('Lets first define all of the columns')
    st.markdown('Ladder score just means the happiness score, ranging from 0 to 10')
    st.markdown('upperwhisker is the maximum amount of happiness in that country')
    st.markdown('lowerwhisker is the least amount of happiness in that country')
    st.markdown("Logged GDP per capita is the amount of money the country makes divided by the country's population")
    st.markdown('I think these columns needs the most explaining')
 
    if st.checkbox('I get it'):
        st.balloons()
        st.markdown('please uncheck this after the balloons, it will bring unimaginable problems')


if selected_box == 'Region Distribution':
    st.title('Region Distribution')
    st.subheader('Lets see how the regions are distributed.')
    st.plotly_chart(px.pie(happy, happy['Regional indicator'], color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name'))
    st.markdown('The region with the most countries is Sub-Saharan Africa, there are actually 26 countries within this region.')
    st.markdown('The region with the least countries is North America, Australia, and New Zealand. This is not correct, because of the lack of the amount of happiness data found there.')


if selected_box == 'How to Use 3D Scatter Plot?':
    st.title('How to Use 3D Scatter Plot?')
    st.markdown('Drag the plot around to see different 2D scatter plots. How many different scatter plots can you see?')
    st.markdown('You can also enter the full screen mode for better visual effects')


if selected_box == 'Analysis 1':
    st.title('Analysis 1')
    plot1 = px.scatter_3d(happy, x = 'Ladder score', y = 'Logged GDP per capita' , z = 'Social support', color = 'Regional indicator', hover_name = 'Country')
    st.plotly_chart(plot1)
    st.markdown('Sub-Saharan Africa is very poor so it is in the corners of this plot.')
    st.markdown('When the GDP goes up, the happiness gets ')
    st.markdown('Social support up, Ladder score up')
    st.markdown('Social support up, GDP up')
    st.markdown('These factors support each other')


if selected_box == 'Analysis 2':
    st.title('Analysis 2')
    plot2 = px.scatter_3d(happy, x='Ladder score', y='Logged GDP per capita', z='Generosity', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name')
    st.plotly_chart(plot2)
    st.markdown('This is the 3D scatter chart with the following factors: Ladder score, GDP per person and Generosity.')

    if st.button('Show analysis'):
        st.markdown('The ladder score goes up as the GDP goes up, because the more richer you are, the happier you are.')
        st.markdown('GDP up, Ladder score up')
        st.markdown('Interesting! Ladder: 7~3.5')
        st.markdown('Generosity: 0.1~-0.3')
        st.markdown('May think that GDP up, generosity up. BUT NO')


if selected_box == 'Analysis 3':
    st.title('Analysis 3')
    st.plotly_chart(px.scatter_3d(happy, x='Regional indicator', y='Ladder score', z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name'))
    st.markdown('Fast way of looking at data')


if selected_box == 'Analysis 4':
    st.title('Analysis 4')
    st.plotly_chart(px.scatter_3d(happy, x='Freedom to make life choices', y='Social support',z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name'))


if selected_box == 'Some More Fast Facts':
    st.title('Fast Facts')
    st.markdown('I have made another more smaller table with the most needed columns.')
    st.markdown('Happiest:')
    noob = happy['Country name', 'Regional indicator', 'Ladder score', 'Logged GDP per capita', 'Social support', 'Generosity']
    happiest = noob[happy['Ladder score'] == max(happy['Ladder score'])]
    happiest
    st.image('download.jpg', use_column_width=True)
    st.markdown('Wealthiest:')
    wealthiest = noob[happy['Logged GDP per capita'] == max(happy['Logged GDP per capita'])]
    wealthiest
    
    
if selected_box == 'Bibliography':
    st.title('Bibliography')
# ### The point here 
# ### ![Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png](attachment:Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png)
# ### is Afghanistan, a very poor country, with a bunch of terrorists