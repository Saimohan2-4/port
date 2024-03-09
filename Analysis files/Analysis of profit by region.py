import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')
df = pd.DataFrame(df2)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year
df['Profit'] = df['Profit'].astype(float)

# Group by Region and calculate total profit
profit_by_region = df.groupby('Region')['Profit'].sum().reset_index()

# Group by Region and Year and calculate total profit
profit_by_region_year = df.groupby(['Region', 'Year'])['Profit'].sum().reset_index()

# Create a list of unique years
years = df['Year'].unique()
years.sort()

# Create a bar chart using plotly.graph_objects
fig = go.Figure()

# Initial trace with the first year
initial_year = years[0]
initial_data = profit_by_region_year[profit_by_region_year['Year'] == initial_year]

# Create BAR Graph
fig.add_trace(go.Bar(
    x=profit_by_region['Region'].tolist(),
    y=profit_by_region['Profit'].tolist(),
))

# Set layout details
fig.update_layout(
    xaxis=dict(title='Region'),
    yaxis=dict(title='Profit'),
    updatemenus=[
        dict(
            type='buttons',
            x=-0.15,
            y=1,
            buttons=[
                dict(label='All Years',
                     method='update',
                     args=[{'x': [profit_by_region['Region'].tolist()],
                            'y': [profit_by_region['Profit'].tolist()],
                            'text': 'All Years'}]
                     ),
            ],
            direction='down'
        ),
        dict(
            type='dropdown',
            buttons=[
                dict(label=str(year),
                     method='update',
                     args=[{'x': [profit_by_region_year.loc[profit_by_region_year['Year'] == year]['Region'].tolist()],
                            'y': [profit_by_region_year.loc[profit_by_region_year['Year'] == year]['Profit'].tolist()],
                            'text': f'{year}'}])
                for year in years
            ],
            direction='down'
        ),
    ]
)

fig.update_layout(
    title=dict(
    text=f"Analysis of Profits by Region ",
    font=dict(size=30,color="navy")
    )
    )
# Display the plot
fig.write_html("Analysis Of profit by Region.html")
fig.show()

