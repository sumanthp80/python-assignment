import pandas as pd

'''
This program expects CSV file in below format to give the desired results.
order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,A001,2023-05-21,A,Socks,020.00,2

'sales' column needs to be added to working sheet by calling calculate_sales() function before calling any other functions in this program 
'sales'  = product_price * quantity  
'''

def calculate_sales(data):
    try:
        sales = data['product_price'] * data['quantity']
        return sales
    except Exception as e:
        print("Error occurred while calculating sales:", str(e))
        return None
    
def calculate_monthly_revenue(data):
    try:
        data['order_date'] = pd.to_datetime(data['order_date'])
        data['month'] = data['order_date'].dt.to_period('M')
        monthly_revenue = data.groupby('month')['sales'].sum()
        return monthly_revenue
    except Exception as e:
        print("Error occurred while calculating monthly revenue:", str(e))
        return None

def calculate_product_revenue(data):
    try:
        product_revenue = data.groupby('product_name')['sales'].sum()
        return product_revenue
    except Exception as e:
        print("Error occurred while calculating product revenue:", str(e))
        return None

def calculate_customer_revenue(data):
    try:
        customer_revenue = data.groupby('customer_id')['sales'].sum()
        return customer_revenue
    except Exception as e:
        print("Error occurred while calculating customer revenue:", str(e))
        return None

def identify_top_customers(data):
    try:
        top_customers = data.groupby('customer_id')['sales'].sum().nlargest(10)
        return top_customers
    except Exception as e:
        print("Error occurred while identifying top customers:", str(e))
        return None

if __name__ == '__main__':
    try:
        # Read the CSV file
        data = pd.read_csv('orders.csv')

        # add new sales column by calculating product_price * quantity. 
        # This new column will be used for revenue calcualtion
        data['sales'] = calculate_sales(data)

        #monthly_revenue 
        monthly_revenue = calculate_monthly_revenue(data)

        # Compute total revenue generated by each product
        product_revenue = calculate_product_revenue(data)

        # Compute total revenue generated by each customer
        customer_revenue = calculate_customer_revenue(data)

        # Identify the top 10 customers by revenue generated
        top_customers = identify_top_customers(data)

        # Print the results
        print("Total revenue generated by the online store for each month:")
        print(monthly_revenue)
        print("\nTotal revenue generated by each product:")
        print(product_revenue)
        print("\nTotal revenue generated by each customer:")
        print(customer_revenue)
        print("\nTop 10 customers by revenue generated:")
        print(top_customers)
    except Exception as e:
        print("An error occurred:", str(e))