import pandas as pd
import pytest
from io import StringIO
from orders import *

def test_calculate_sales():
    csv_data = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n" \
               "1,C1,2023-01-01,P1,Product 1,10.00,2\n" \
               "2,C2,2023-01-15,P2,Product 2,15.00,1\n" \
               "3,C1,2023-02-10,P3,Product 3,20.00,3\n" \
               "4,C3,2023-02-20,P1,Product 1,10.00,1\n" \
               "5,C2,2023-03-05,P1,Product 1,10.00,2\n"

    data = pd.read_csv(StringIO(csv_data))
    # add new sales column by calculating product_price * quantity. 
    # This new column will be used for revenue calcualtion
    #data['sales'] = data['product_price'] * data['quantity']
    sales = calculate_sales(data)

    assert sales[0] == 20.00
    assert sales[1] == 15.00
    assert sales[2] == 60.00
    assert sales[3] == 10.00
    assert sales[4] == 20.00
    
def test_calculate_monthly_revenue():
    csv_data = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n" \
               "1,C1,2023-01-01,P1,Product 1,10.00,2\n" \
               "2,C2,2023-01-15,P2,Product 2,15.00,1\n" \
               "3,C1,2023-02-10,P3,Product 3,20.00,3\n" \
               "4,C3,2023-02-20,P1,Product 1,10.00,1\n" \
               "5,C2,2023-03-05,P1,Product 1,10.00,2\n"

    data = pd.read_csv(StringIO(csv_data))
    # add new sales column by calculating product_price * quantity. 
    # This new column will be used for revenue calcualtion
    data['sales'] = calculate_sales(data)
    monthly_revenue = calculate_monthly_revenue(data)

    assert len(monthly_revenue) == 3
    assert monthly_revenue[0] == 35.00
    assert monthly_revenue[1] == 70.00
    assert monthly_revenue[2] == 20.00

def test_calculate_product_revenue():
    csv_data = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n" \
               "1,C1,2023-01-01,P1,Product 1,10.00,2\n" \
               "2,C2,2023-01-15,P2,Product 2,15.00,1\n" \
               "3,C1,2023-02-10,P3,Product 3,20.00,3\n" \
               "4,C3,2023-02-20,P1,Product 1,10.00,1\n" \
               "5,C2,2023-03-05,P1,Product 1,10.00,2\n"

    data = pd.read_csv(StringIO(csv_data))
    # add new sales column by calculating product_price * quantity. 
    # This new column will be used for revenue calcualtion
    data['sales'] = calculate_sales(data)
    product_revenue = calculate_product_revenue(data)

    assert len(product_revenue) == 3
    assert product_revenue['Product 1'] == 50.00
    assert product_revenue['Product 2'] == 15.00
    assert product_revenue['Product 3'] == 60.00

def test_calculate_customer_revenue():
    csv_data = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n" \
               "1,C1,2023-01-01,P1,Product 1,10.00,2\n" \
               "2,C2,2023-01-15,P2,Product 2,15.00,1\n" \
               "3,C1,2023-02-10,P3,Product 3,20.00,3\n" \
               "4,C3,2023-02-20,P1,Product 1,10.00,1\n" \
               "5,C2,2023-03-05,P1,Product 1,10.00,2\n"

    data = pd.read_csv(StringIO(csv_data))
    # add new sales column by calculating product_price * quantity. 
    # This new column will be used for revenue calcualtion
    data['sales'] = calculate_sales(data)
    customer_revenue = calculate_customer_revenue(data)

    assert len(customer_revenue) == 3
    assert customer_revenue['C1'] == 80.00
    assert customer_revenue['C2'] == 35.00
    assert customer_revenue['C3'] == 10.00

def test_identify_top_customers():
    csv_data = "order_id,customer_id,order_date,product_id,product_name,product_price,quantity\n" \
               "1,C1,2023-01-01,P1,Product 1,10.00,2\n" \
               "2,C2,2023-01-15,P2,Product 2,15.00,1\n" \
               "3,C1,2023-02-10,P3,Product 3,20.00,3\n" \
               "4,C3,2023-02-20,P1,Product 1,14.00,1\n" \
               "5,C4,2023-02-20,P1,Product 1,01.00,1\n" \
               "6,C5,2023-02-20,P1,Product 1,02.00,1\n" \
               "7,C6,2023-02-20,P1,Product 1,03.00,1\n" \
               "8,C7,2023-02-20,P1,Product 1,04.00,1\n" \
               "9,C8,2023-02-20,P1,Product 1,05.00,1\n" \
               "10,C9,2023-02-20,P1,Product 1,06.00,1\n" \
               "11,C10,2023-02-20,P1,Product 1,07.00,1\n" \
               "12,C11,2023-02-20,P1,Product 1,08.00,1\n" \
               "13,C12,2023-03-05,P1,Product 1,10.00,2\n"

    data = pd.read_csv(StringIO(csv_data))
    # add new sales column by calculating product_price * quantity. 
    # This new column will be used for revenue calcualtion
    data['sales'] = calculate_sales(data)
    top_customers = identify_top_customers(data)

    assert len(top_customers) == 10
    assert top_customers.index[0] == 'C1'
    assert top_customers.iloc[0] == 80.00
    assert top_customers.index[1] == 'C12'
    assert top_customers.iloc[1] == 20.00
    assert top_customers.index[2] == 'C2'
    assert top_customers.iloc[2] == 15.00
    assert top_customers.index[3] == 'C3'
    assert top_customers.iloc[3] == 14.00
    assert top_customers.index[4] == 'C11'
    assert top_customers.iloc[4] == 08.00
    assert top_customers.index[5] == 'C10'
    assert top_customers.iloc[5] == 07.00