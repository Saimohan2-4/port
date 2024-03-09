import plotly.graph_objects as go
import pandas as pd

# Example DataFrame
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')
df = pd.DataFrame(df2)

# Group by on states postal codes and sales
states_s = df.groupby(['States', 'Postal Code'])['Sales'].sum().reset_index()

# Lists for postal codes and states and sales
Post_cds = list(states_s['Postal Code'])
States = list(states_s['States'])
sum_of_sales_states = list(states_s['Sales'].astype(int))

# Create a fig called choropleth, and sc
fig = go.Figure(data=go.Choropleth(locations=Post_cds,  # Spatial coordinates
    z=sum_of_sales_states,  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Portland',
    colorbar_title="Sum of sales across USA",hovertext=States

))

fig.update_geos(
    scope='usa',  # Set the map scope to USA
     # Adjust the projection scale as needed
)
fig.update_layout(title=dict(text="Sales Analysis on USA-States",
                             font=dict(size=30,color="maroon")))

fig.write_html("Geospatial Analysis Of Sales.html")

fig.show()
