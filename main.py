import streamlit as st
from datetime import datetime, timedelta
import pickle

st.title('Flight Price Prediction')

airline = st.sidebar.selectbox('Airline', [None, 'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'])
airline_dict = {'AirAsia': 0, 'Indigo': 1, 'GO_FIRST': 2, 'SpiceJet': 3, 'Air_India': 4, 'Vistara': 5}

source_city = st.sidebar.selectbox('Soruce City',
                                   [None, 'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])

departure_time = st.sidebar.selectbox('Departure Time',
                                      [None, 'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])
departure_time_dict = {'Late_Night': 0, 'Afternoon': 2, 'Early_Morning': 3, 'Evening': 4, 'Morning': 5, 'Night': 6}

stops = st.sidebar.selectbox('Stops', [None, 'zero', 'one', 'two_or_more'])
stops_dict = {'zero': 0, 'two_or_more': 1, 'one': 2}

arrival_time = st.sidebar.selectbox("Arrival Time",
                                    [None, 'Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night'])
arrival_time_dict = {'Late_Night': 0, 'Early_Morning': 1, 'Afternoon': 2, 'Night': 3, 'Morning': 4, 'Evening': 5}

destination_city = st.sidebar.selectbox('Destination City',
                                        [None, 'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'])

Class = st.sidebar.selectbox('Class', [None, 'Business', 'Economy'])
Class_dict = {'Economy': 0, 'Business': 1}

departure_date = st.sidebar.date_input('Date of travel', min_value=datetime.today(),
                                       max_value=datetime.today() + timedelta(50))
date_diff = datetime.strptime(str(departure_date), '%Y-%m-%d') - datetime.today()
Date_diff = int(date_diff.days + 1)

travel = source_city + ' - ' + destination_city
travel_dict = {'Bangalore - Delhi': 0, 'Delhi - Bangalore': 1, 'Hyderabad - Delhi': 2,
               'Delhi - Hyderabad': 3, 'Mumbai - Delhi': 4, 'Bangalore - Hyderabad': 5,
               'Delhi - Mumbai': 6, 'Kolkata - Delhi': 7, 'Delhi - Kolkata': 8,
               'Delhi - Chennai': 9, 'Chennai - Delhi': 10, 'Mumbai - Hyderabad': 11,
               'Hyderabad - Bangalore': 12, 'Mumbai - Bangalore': 13, 'Bangalore - Mumbai': 14,
               'Kolkata - Hyderabad': 15, 'Kolkata - Bangalore': 16, 'Hyderabad - Mumbai': 17,
               'Mumbai - Kolkata': 18, 'Bangalore - Kolkata': 19, 'Hyderabad - Kolkata': 20,
               'Bangalore - Chennai': 21, 'Hyderabad - Chennai': 22, 'Chennai - Hyderabad': 23,
               'Mumbai - Chennai': 24, 'Kolkata - Chennai': 25, 'Chennai - Mumbai': 26,
               'Chennai - Kolkata': 27, 'Kolkata - Mumbai': 28, 'Chennai - Bangalore': 29}

data = ['airline', 'source_city', 'departure_time', 'stops', 'arrival_time',
        'destination_city', 'Class', 'Date_diff']

if None not in data and st.button('PREDICT PRICE'):
    features = [[airline_dict[airline], departure_time_dict[departure_time], stops_dict[stops],
                arrival_time_dict[arrival_time], Class_dict[Class], Date_diff, travel_dict[travel]]]
    model = pickle.load(open('rf.pkl', 'rb'))
    predict = model.predict(features)[0]
    st.write(f'Your Flight Price Rs {predict:.2f}')