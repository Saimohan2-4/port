# import packages
import pandas as pd
import plotly.express as px

# Read the CSV file
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')
df = pd.DataFrame(df2)

# Convert 'Sales', 'Profit', and 'Discount' to appropriate data types
df['Sales'] = df['Sales'].astype(float)
df['Profit'] = df['Profit'].astype(float)
df['Discount'] = df['Discount'].astype(float)

# Aggregate Sales and Profit by Sub Category
subcat_agg = df.groupby(['Sub Category','Category']).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Create a bubble chart using Plotly Express
fig = px.scatter(subcat_agg, x='Sales', y='Category', size='Sales', color='Profit',
                 size_max=50, template='plotly_dark',hover_name='Sub Category',
                 labels={'Sub Category': 'Sub-Category', 'Sales': 'Total Sales', 'Profit': 'Total Profit'})

# Set layout details
fig.update_layout(title=dict(text='Bubble Chart: Total Sales and Profit by Sub-Category'
                             ,font=dict(size=30,color="darkseagreen")),
                  xaxis_title='Sub-Category', yaxis_title='Total Profit')

# Set background color to black
fig.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)

fig.write_html("Bubble chart Analysis on profit.html")
# Display the plot
fig.show()
