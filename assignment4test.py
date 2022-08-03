import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
import math
import  numpy as np
import io
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(page_title="Dashboard",
                   page_icon="chart_with_upwards_trend",
                   layout="wide")

st.markdown("<h6 style='text-align: center; color: black;'> Created By Alex Singh, Anthony Joseph, Tyrese Salandy, Turenne Wilson, Leah-Marie Leotaud </h6>", unsafe_allow_html=True)
st.markdown("""---""")
# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.write("<h5 style='text-align: center; color: black;'>From The Quick Menu Select Your Views </h5>", unsafe_allow_html=True)

    else:
        st.write("<h5 style='text-align: center; color: black;'>Please Upload File to Application </h5>", unsafe_allow_html=True)


def data_summary(df):
    st.markdown("<h2 style='text-align: center; color: black;'> Statistics of Dataframe </h2>", unsafe_allow_html=True)
    st.markdown("""---""")

    st.write(df.describe())

def data_variables(df):
    st.markdown("<h2 style='text-align: center; color: black;'>Listed Variables & Data Types </h2>",
                unsafe_allow_html=True)
    st.markdown("""---""")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)


def data_header(df):
    st.markdown("<h2 style='text-align: center; color: black;'> Header of Dataframe </h2>", unsafe_allow_html=True)
    st.markdown("""---""")
    st.write(df.head())



def displayplot():
    st.markdown("<h2 style='text-align: center; color: black;'> Graph Plots </h2>", unsafe_allow_html=True)
    st.markdown("""---""")
    if st.button("line Graph"):
        line_graph()
    st.button(" Graph")
    if st.button("Scatter Graph"):
        scatter_graph(df)


def Predictor():
    st.markdown("<h2 style='text-align: center; color: black;'> Goals Predictor </h2>", unsafe_allow_html=True)
    st.markdown("""---""")
    games_played = st.text_input("Games Played:")
    st.write('You Entered:', games_played)
    minutes_played = st.text_input("Minutes Played:")
    st.write('You Entered:', minutes_played)

    X = df[['MP', 'Min']]
    y = df['Gls']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    switch = st.radio(
        "Turn On to display the prediction results",
        ('Off', 'On'))

    if switch == 'Off':
        st.write('Currently Off.')
    else:
        st.write(regr.predict([[games_played, minutes_played]]))


#def line_graph(df):

    #line_chart = Chart(df).mark_line().encode(
       # y=df['Age'],
       # x=df['MP'],)


def scatter_graph(df):
    fig = plt.figure(figsize=(9, 5))
    sns.regplot(x="Age",
                y="Min",
                data=df)
    # show the plot
    st.pyplot(fig)

def show_count(df):
    st.markdown("<h2 style='text-align: center; color: black;'> Show Count & Total </h2>", unsafe_allow_html=True)
    st.markdown("""---""")
    user_select = st.selectbox('Select Team:',
                                ('Arsenal', 'Aston Villa', 'Brentford', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Leeds United',
                                 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United', 'Newcastle United', 'Norwich City', 'Southampton', 'Tottenham Hotspur',
                                 'Watford', 'West Ham United', 'Wolverhampton Wanderers'))
    st.write('You selected:', user_select)
    st.markdown("""---""")
    tab = df['Team'].value_counts().reindex(
        [user_select], fill_value=0)
    st.dataframe(tab)
    st.markdown("""---""")
    st.write("<h6 style='text-align: center; color: black;'> This shows the count & total of players",user_select, "had over the period 2021 -2022 </h6>", unsafe_allow_html=True)
    #st.write('This shows the amount of players',user_select, 'had over the period 2021 -2022')













# Add a title and intro text
st.markdown("<h2 style='text-align: center; color: black;'> Premier League Analytics </h2>", unsafe_allow_html=True)
st.markdown("""---""")
st.image("https://github.com/alexfrmhillview/assignment04/blob/main/PL.png?raw=true")
st.markdown("""---""")
# Sidebar setup
st.sidebar.title('Quick Menu')
upload_file = st.sidebar.file_uploader('Upload .CSV File')
# Sidebar navigation
st.sidebar.markdown("""---""")
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary','Data Variables', 'Data Header', 'Graph Plots','Predictor','Show Count (Categorical)'])
st.sidebar.markdown("""---""")
# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file, encoding='windows-1252')

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary(df)
elif options == 'Data Variables':
    data_variables(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Graph Plots':
    displayplot()
elif options == 'Predictor':
    Predictor()
elif options == 'Show Count (Categorical)':
    show_count(df)
