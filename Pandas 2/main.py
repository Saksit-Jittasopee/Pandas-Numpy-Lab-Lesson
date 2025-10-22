# YOUR CODE HERE
import pandas as pd

passenger_data = pd.read_csv('data.csv')
passenger_data.head()

def process_passenger_data(data):
    embarked = data['Embarked'].unique()
    
    for port in embarked:
        filtered_data = data[data['Embarked'] == port]
        sorted_data = filtered_data.sort_values(by=['Pclass', 'Fare'], ascending=[True, False])
        
        selected_data = sorted_data[['Pclass', 'Fare', 'Embarked']]
        top_5 = selected_data.head(5)
        bottom_5 = selected_data.tail(5)
        
        print(f"Embarked: {port}")
        print(top_5)
        print(bottom_5)
process_passenger_data(passenger_data)
