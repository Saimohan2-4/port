import pandas as pd
import plotly.graph_objects as go

# reading the csv file
df2=pd.read_csv('Main Port/Retail sales analysis.csv')

# assigning that csv file variable to the pandas dataframe, we can do df= pd.DataFrame(Filepath.csv) also.
df = pd.DataFrame(df2)

# Convert 'Sales' to float
sales = list(df['Sales'].astype(float))

# Convert 'Order Date' column to datetime, to access year, the column needs to be changed to datetime format.
df['Order Date'] = pd.to_datetime(df['Order Date'])
year = list(df['Order Date'].dt.year)
selected_year = year[0]

# Extract Year from 'Order Date'
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

# Calculate the sum of sales for each year
sales_sum_per_year = df.groupby('Year')['Sales'].sum().reset_index()

# Calculate the sum of sales for each year and month
sales_sum_per_month = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

years = list(sales_sum_per_year['Year'])
sales_per_year = list(sales_sum_per_year['Sales'])

# Create a dictionary to store monthly sales for each year
monthly_sales_dict = {
    year: list(sales_sum_per_month.loc[sales_sum_per_month['Year'] == year, 'Sales'])
    for year in years
}

# Define the order of months
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create a line chart using Plotly Express
fig = go.Figure()

# Add a trace for each year
for i, year in enumerate(years):
    fig.add_trace(go.Line(x=month_order, y=monthly_sales_dict[year], name=f"Sales {year}"))

#update layout for titles fonts and colors
fig.update_layout(title=dict(text="Sales Analysis Per year",font=dict(size=30)), 
                  xaxis_title=dict(text="MONTHS",font=dict(size=20,family="Poppins",color="blue")),
                  yaxis_title=dict(text="SALES",font=dict(size=20,family="Poppins",color="blue")))
#Display the plot
fig.write_html("Time series analysis Line chart.html")
fig.show()

