import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


def run():
    # Membuat Title
    st.title('Credit Card ')

    # Membuat Sub Header
    st.subheader('Membuat EDA untuk analisa dataset Credit Card')

    #Menambahkan Gambar
    image = Image.open('cc.jpg')
    st.image(image, caption='Black Card')

    #Menambahkan Deskripsi
    st.write('Page ini dibuat oleh **Syechrifanka Yoffi Adrian**')

    #Show Data Frame
    data = pd.read_csv('P1G5_Set_1_Syechrifanka-Yoffi.csv')
    st.dataframe(data)

    #Membuat Barplot
    st.write('#### Plot Cardinality Categorical Columns')
    # Specify the list of categorical columns you want to visualize
    categorical_columns = ['education_level', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6', 'sex', 'marital_status']
    # Create a DataFrame to store the cardinality of each categorical column
    cardinality_data = pd.DataFrame({'Column': categorical_columns, 'Cardinality': [data[col].nunique() for col in categorical_columns]})
    # Create a bar plot to visualize the cardinality of each column
    fig = plt.figure(figsize=(12, 6))
    sns.barplot(data=cardinality_data, x='Column', y='Cardinality', palette='viridis')
    plt.title('Cardinality of Categorical Columns')
    plt.xlabel('Categorical Columns')
    plt.ylabel('Cardinality (Number of Unique Values)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    #Membuat Barplot Berdasarkan Inputan User untuk column categorical
    st.write('#### Histogram Berdasarkan Input ')
    pilihan = st.selectbox('Pilih Column:', ('education_level', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6', 'sex', 'marital_status'))
    fig = plt.figure(figsize = (5,5))
    sns.countplot(data=data, x=data[pilihan], palette="Set3")  # Membuat bar plot
    st.pyplot(fig)

    #Membuat Boxplot Berdasarkan Inputan User
    st.write('#### Boxplot Berdasarkan Input User')
    pilihan = st.selectbox('Pilih Column:', ('limit_balance','age','bill_amt_1','bill_amt_2','bill_amt_3','bill_amt_4','bill_amt_5','bill_amt_6','pay_amt_1','pay_amt_2','pay_amt_3','pay_amt_4','pay_amt_5','pay_amt_6'))
    fig = plt.figure(figsize = (15,5))
    sns.boxplot(data=data, x=data[pilihan], palette="Set3")
    st.pyplot(fig)

    #Membuat Pie Chart default payment next month
    default_counts = data['default_payment_next_month'].value_counts()
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(6, 6))
    sns.set(style="whitegrid")
    plt.pie(default_counts, labels=default_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral'])
    plt.title('Distribution of Default Payment')
    st.pyplot(fig)
    st.markdown('Berdasarkan Pie Chart Diatas, dapat disimpulkan bahwa terdapat 21,4% pengguna kartu kredit yang gagal dalam pembayaran kartu kredit serta 78,6% pengguna kartu kredit yang pembayarannya lancar')

    

    # #Membuat Plotly Plot
    # st.write('#### Plotly Plot - ValueEUR dengan Overall')
    # fig = px.scatter(data, x='ValueEUR', y='Overall', hover_data=['Name','Age'])
    # st.plotly_chart(fig)

if __name__ == '__main__':
    run()