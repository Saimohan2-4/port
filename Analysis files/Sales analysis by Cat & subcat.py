# import pandas, plotly packages
import pandas as pd
import plotly.graph_objects as go

# Read your csv file or use df = pd.DataFrame(filepath.csv)
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')
df = pd.DataFrame(df2)

# Convert 'Order Date' column to datetime, to access the year, the column needs to be changed to datetime format.
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year from 'Order Date'
df['Year'] = df['Order Date'].dt.year

# Group by 'Category' and 'Sub Category', then sum the 'Sales' for each group
sale_per_cat_subcate = df.groupby(['Category', 'Sub Category'])['Sales'].sum().reset_index()

# Sort the DataFrame by 'Sales' in descending order for both category and subcategory
sales_category = df.groupby('Category')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
sale_per_cat_subcate = sale_per_cat_subcate.sort_values(by='Sales', ascending=False)

# Lists for x, y for all categories and sales
Sales_cat = list(sales_category['Sales'])
list_cats = list(sales_category['Category'])

# Lists for x,y on click on dropdown button
list_s_cats = list(sale_per_cat_subcate['Sub Category'])
list_sales_sub_cat = list(sale_per_cat_subcate['Sales'])

# Create a dictionary to store sales by subcategory for each category
subcategory_sale_dict = {
    cat: list(sale_per_cat_subcate.loc[sale_per_cat_subcate['Category'] == cat, 'Sales'])
    for cat in list_cats
}

# Create a dictionary to store subcategories for each category
category_subcategory_dict = {
    cat: list(sale_per_cat_subcate.loc[sale_per_cat_subcate['Category'] == cat, 'Sub Category'])
    for cat in list_cats
}

# Create a Plotly figure
fig = go.Figure()

# Prepare text for hover labels
cat_text = [f"Category: {cat}<br> Sales: {sales}" for cat, sales in zip(list_cats, Sales_cat)]

# Create a bar chart with the initial data
fig = go.Figure(data=[go.Bar(x=list_cats, y=Sales_cat, marker_color="cornflowerblue", text=cat_text)])

# Update layout with buttons for interactive features
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label="(Total Sales by Category)",
                    args=[{
                        "x": [list_cats],
                        "y": [Sales_cat],
                        
                        "text": [cat_text]  
                    }],
                    method="update",
                ),
                *[
                    dict(
                        args=[{
                            "x": [category_subcategory_dict[j]],  # Use subcategories as x-axis labels
                            "y": [subcategory_sale_dict[j]],
                            "text": [
                                [f"Category: {j}<br>Subcategory: {sub}<br>Sales: {sale}"
                                 for sub, sale in zip(category_subcategory_dict[j], subcategory_sale_dict[j])]]
                        }],
                        label=str(j),
                        method="update"
                    ) for j in list_cats
                ]
            ],
            direction="down"
        )
    ],
    title=dict(text="Analysis of Sales by Category & Subcategory",font=dict(size=30,color="slateblue"))
)

fig.write_html("Sales Analysis by Cat and SUbcat.html")
# Display the figure
fig.show()
