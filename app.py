import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


def standard_units(x):
	return (x - np.average(x))/np.std(x)
def correlation(x,y):
	x_su = standard_units(x)
	y_su = standard_units(y)
	return np.average(x_su * y_su)


happy = pd.read_csv('world-happiness-report-2021.csv')
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
    st.image('OIP-1.jpg')


if selected_box == 'Table Preview':
    st.title('Table Preview')
    happy
    st.markdown('For better effects, enter fullscreen mode!')


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
    plot1 = px.scatter_3d(happy, x = 'Ladder score', y = 'Logged GDP per capita' , z = 'Social support', color = 'Regional indicator', hover_name = 'Country name')
    st.plotly_chart(plot1)
    st.markdown('This is the 3D scatter chart with the following factors: Ladder score, GDP per person and Social support.')
    
    if st.checkbox('Show analysis', key='1'):
        st.markdown('Sub-Saharan Africa is very poor so it is in the corners of this plot.')
        st.markdown('When the GDP goes up, the happiness grows, because the wealthier you are, the more happy you are.')
        st.markdown('When other people care more about you, you become happier.')
        st.markdown('When other people care more about you, you become happier, and that causes you to be more wealthier.')
        st.markdown('These factors support each other')


if selected_box == 'Analysis 2':
    st.title('Analysis 2')
    plot2 = px.scatter_3d(happy, x='Ladder score', y='Logged GDP per capita', z='Generosity', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name')
    st.plotly_chart(plot2)
    st.markdown('This is the 3D scatter chart with the following factors: Ladder score, GDP per person and Generosity.')

    if st.checkbox('Show analysis', key='2'):
        #r_of_thing = correlation(happy['Logged GDP per capita'], happy['Generosity'])
        st.markdown('The ladder score goes up as the GDP goes up, because the more richer you are, the happier you are.')
        st.markdown('Interesting! There is a Ladder score blob ranging from 7 to 3.5')
        st.markdown('Interesting! There is a Generosity blob ranging from 0.1 to -0.3')
        st.markdown('We may think that the wealthier you get the more generous you get, but no.')

if selected_box == 'Analysis 3':
    st.title('Analysis 3')
    st.plotly_chart(px.scatter_3d(happy, x='Regional indicator', y='Ladder score', z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name'))
    st.markdown('This is the 3D scatter chart with the following factors: Ladder score, GDP per person and Regional indicator.')
    
    if st.checkbox('Show analysis', key='3'):
        st.markdown('This way is a very fast way of looking at data')
        st.markdown('As we can see Western Europe is both happy and wealthy, why?')
        
        if st.checkbox('Why?'):
            st.markdown('This is a very complicated question.')
            st.markdown('There are about 2 reasons:')
            st.markdown("1. Western Europe conquered about half the Earth's area in the Middle Ages, so that forced the other countries not to progress.")
            st.markdown('2. Western Europe, when having half the Earth, saw the other culture that it conquered, so then became industrialized more quickly.')


if selected_box == 'Analysis 4':
    st.title('Analysis 4')
    st.plotly_chart(px.scatter_3d(happy, x='Freedom to make life choices', y='Social support',z='Logged GDP per capita', color = 'Regional indicator', color_discrete_sequence = px.colors.qualitative.Safe, hover_name = 'Country name'))
    st.markdown('This is the 3D scatter chart with the following factors: Freedom, GDP per person and Social support.')
    
    if st.checkbox('Show analysis', key='4'):
        st.markdown('The more support you have, the freer you are.')


if selected_box == 'Some More Fast Facts':
    st.title('Fast Facts')
    st.markdown('Happiest:')
    happiest = happy[happy['Ladder score'] == max(happy['Ladder score'])]
    happiest
    st.image('download.jpg')
    st.markdown('Wealthiest:')
    wealthiest = happy[happy['Logged GDP per capita'] == max(happy['Logged GDP per capita'])]
    wealthiest
    st.image('OIP.jpg')
    st.markdown('Most generous:')
    generous = happy[happy['Generosity'] == max(happy['Generosity'])]
    generous
    st.image('download-1.jpg')
    
    
if selected_box == 'Bibliography':
    st.title('Bibliography')
    st.markdown('https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021')
    st.markdown('Github repository:')
    st.markdown('https://github.com/StanleyData/World-Happiness-Report-2021')
# ### The point here 
# ### ![Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png](attachment:Screen%20Shot%202021-07-24%20at%2012.07.09%20PM.png)
# ### is Afghanistan, a very poor country, with a bunch of terrorists
