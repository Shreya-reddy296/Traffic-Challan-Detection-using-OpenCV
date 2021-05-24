import pandas as pd

def generate_receiver_email(reg_no):
    records=pd.read_csv("car_dataset.csv")
    email=""
    for row in records.iterrows():
        curr_reg_no=row[1][0]
        if curr_reg_no ==reg_no:
            email= row[1][1]
            break

    return email
#print(generate_receiver_email("MH 20 DV 2363"))