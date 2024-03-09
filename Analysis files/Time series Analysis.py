
#import nesscary libraries
import pandas as pd
import plotly.graph_objects as go

# reading the csv file
df2=pd.read_csv('Main Port/Retail sales analysis.csv')

# assigning that csv file variable to the pandas dataframe, we can do df= pd.DataFrame(Filepath.csv) also.
df = pd.DataFrame(df2)

# Convert 'Sales' column to float
sales = list(df['Sales'].astype(float))

# Convert 'Order Date' column to datetime, to access year, the column needs to be changed to datetime foramt.
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year,Month from 'Order Date'
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

# Calculate the sum of sales for each year
sales_sum_per_year = df.groupby('Year')['Sales'].sum().reset_index()

# Calculate the sum of sales for each year and month
sales_sum_per_month = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

# varibale called year as list
years = list(sales_sum_per_year['Year'])

# list for sales per year
sales_per_year = list(sales_sum_per_year['Sales'])

# Create a dictionary to store monthly sales for each year
monthly_sales_dict = {
    year: list(sales_sum_per_month.loc[sales_sum_per_month['Year'] == year, 'Sales'])
    for year in years
}

# Define the order of months, if data is in order , skip this part
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create a bar chart using Plotly Graph Objects (go)
fig = go.Figure(data=[go.Bar(x=years, y=sales_per_year)])
fig.update_layout(title=dict(text="Yearly Sales Analysis",font=dict(size=30,color="mediumpurple")))
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[dict(
                label="(All)",
                method="update",
                args=[{
                    "y": [sales_per_year],
                    "x": [years],
                    "title": "Yearly Sales",
                    "xaxis_title": "Year",
                    "yaxis_title": "Total Sales"
                }],
            ),
            *[
                dict(
                    args=[{
                        "y": [monthly_sales_dict[i]],
                        "x": [sales_sum_per_month.loc[sales_sum_per_month['Year'] == i, 'Month']],
                        "title": f"Monthly Sales for {i}",
                        "xaxis_title": "Month",
                        "yaxis_title": "Sales"
                    }],
                    label=str(i),
                    method="update"
                ) for i in years
            ]
        ],
        direction="down"
 ) ]
)

# Set the order of months for x-axis
fig.update_xaxes(categoryorder="array", categoryarray=month_order)
# Display the plot
fig.write_html("Time series analysis.html")
fig.show()

