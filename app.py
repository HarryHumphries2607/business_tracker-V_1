import pandas as pd
import plotly.express as px
import streamlit as st

#--------TITLE----------

st.set_page_config(page_title="business_tracker(V_1)", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title(" :chart_with_upwards_trend: business_tracker(V_1)")

#-----------------------
#----------file_uploading----------

upload_file = st.file_uploader("Upload your CSV file", type=["CSV"])
#----------------------------------

#--------------checks_if_file_was_uploaded------------
if upload_file is not None:

    df = pd.read_csv(upload_file)       #reads the csv file

    date = df.columns[0]       #gets the date from the first column
    price = df.columns[1]      #gets the price from the second column

#-----------Sorts_by_date--------------
    df[date] = pd.to_datetime(df[date], format='mix', errors='coerce')
    df = df.sort_values(by=date).reset_index(drop=True)
    df[date] = df[date].dt.strftime('%d/%m/%Y')
#--------------------------------------

#-----------creates_line_graph------------
    fig = px.line(df, x=date, y=price )
#-----------------------------------------

#----------graph_fits_page----------------
    st.plotly_chart(fig, use_container_width=True)
#-----------------------------------------
else:
    st.info("Please upload a CSV")
#----------------------------------------------------------
