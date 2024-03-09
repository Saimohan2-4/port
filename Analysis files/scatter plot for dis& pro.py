#import packages pandas, plotly
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Assuming 'df' is your DataFrame with 'Order Date', 'Discount', and 'Profit' columns
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')

df = pd.DataFrame(df2)

# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year from 'Order Date' column
df['Year'] = df['Order Date'].dt.year

# Group by Year and calculate average discount
avg_discount_per_year = df.groupby('Year')['Discount'].mean().reset_index()

# Group by Year and calculate total profit
total_profit_per_year = df.groupby('Year')['Profit'].sum().reset_index()


# Create subplots with 1 row and 2 columns
fig = make_subplots(rows=1, cols=2, subplot_titles=['Average Discount', 'Total Profit'])

# Add average discount subplot on the left side
fig.add_trace(go.Scatter(x=avg_discount_per_year['Year'], y=avg_discount_per_year['Discount'], mode='lines', line=dict(color='orange'), name='Average Discount'), row=1, col=1)

# Add total profit subplot on the right side
fig.add_trace(go.Scatter(x=total_profit_per_year['Year'], y=total_profit_per_year['Profit'], mode='lines',line=dict(color='mediumpurple'), name='Total Profit'), row=1, col=2)

# Update layout
fig.update_layout(title=dict(text='Average Discount and Total Profit over Years',font=dict(size=30,color="mediumpurple")), showlegend=False)

fig.write_html("Scatter plot for Dis & Pro")
# Display the combined plot
fig.show()
