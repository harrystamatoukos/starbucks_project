import streamlit as st
import altair as alt
from clean_data_2 import *
import pandas as pd


st.image('logo.jpg', width=150, format='JPEG')
st.title('Top offers by demographic')

st.sidebar.title('Parameters')

income = st.sidebar.slider('Income level', 0, 140_000, 40_000)
gender = st.sidebar.selectbox(
    "Select Gender",
    ("F", "M", "O"))
age = st.sidebar.slider('Age', 10, 100, 25)


@st.cache
def load_data():
    df = pd.read_csv('df.csv')
    df.drop(columns='Unnamed: 0', inplace=True)
    profile = pd.read_csv('profile.csv')
    profile.drop(columns='Unnamed: 0', inplace=True)
    customers = per_customer_data(df, profile)
    return customers


customers = load_data()

offers = get_most_popular_offers_filtered(
    customers, n_top=10, income=income, gender=gender, age=age)

df_offer = pd.DataFrame(offers[0])
df_offer = df_offer[0].str.split(expand=True)
df_offer.columns = ('Offer Name', 'Reward', 'Difficulty', 'Duration')


st.write('Most effective offers for the selected demographic')

st.write('To view the most succesful offers for the different demographics select different sliders on the left side of the app')

st.table(df_offer)

offers_net_expense = offers[1]
df_expense = pd.DataFrame.from_records(offers_net_expense, index=[0])
df_expense = df_expense.melt()
df_expense.columns = ('Offer', 'Net Expense')

st.write('Net expense chart by offer type')

chart2 = alt.Chart(df_expense).mark_bar(size=40).encode(
    y='Net Expense',
    x='Offer',
).properties(width=700, height=600
             ).configure_axis(grid=False
                              ).configure_view(strokeWidth=0

                                               )


st.altair_chart(chart2)
