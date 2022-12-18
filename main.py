from datetime import date #core python module
import pandas as pd #pip install pandas
from send_mails import send_email #local python module


#loading google sheet 
SHEET_ID = "1XR35IyrnAT8mmSSn6uFU3GqMHyzOGcBPbzWXcyPMRFU" #Replace me 
SHEET_NAME  = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["due_date","reminder_date"]
    df = pd.read_csv(url,parse_dates = parse_dates, dayfirst=True)
    return df   

def query_data_and_send_emails(df):
    present= date.today()
    email_count = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject= f'[coding is Fun] Invoice: {row["invoice_no"]}',
                receiver_email= row["email"],
                name = row["name"],
                due_date = row["due_date"].strftime("%d, %b %Y"),
                invoice_no = row["invoice_no"],
                amount = row["amount"],
            )
            email_count += 1
    return f"Total email sent: {email_count}"


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)