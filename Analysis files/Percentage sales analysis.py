# import pandas, plotly packages
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read your csv file or use df = pd.DataFrame(filepath.csv)
df2 = pd.read_csv('Main Port/Retail sales analysis.csv')
df = pd.DataFrame(df2)

# Group by category and sales 
Category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Group by  Category, Sub Cateogry and Sales
Subcategory_sales = df.groupby(['Category', 'Sub Category'])['Sales'].sum().reset_index()

# Lists for sales, Category and converting sales datatype to Float
sales = list(df['Sales'].astype(float))
catergory_s = list(Category_sales['Category'])

# Creating a dictionary to store category and their respective subcategories
dicts_of_cats_subs_cats={} 
for j in catergory_s:
    subcatse_cats=df[df.Category.isin([j])]
    subcatse_cats=subcatse_cats["Sub Category"]
    list_Sub_cats_in_dict=list(set(subcatse_cats))
    dicts_of_cats_subs_cats[j] = list_Sub_cats_in_dict 

# sum of category
total_sales_cat=sum(Category_sales["Sales"])

# Dictionary for having all the categories total sales
category_total_sales = {category: sum(df[df["Category"] == category]["Sales"]) for category in set(df["Category"])}

# Recalculate subcategory percentages based on category totals
subcategory_percentages_within_category = {}
for category, subcategories in dicts_of_cats_subs_cats.items():
    total_sales_for_category = category_total_sales[category] 
    print(total_sales_for_category) # Get total sales for this category
    for subcategory in subcategories:
        subcategory_sales = sum(df[df["Sub Category"] == subcategory]["Sales"])
        percentage = (subcategory_sales / total_sales_for_category) * 100
        subcategory_percentages_within_category[subcategory] = percentage

# Generate a list of distinct colors for subcategories
subcategory_colors = px.colors.qualitative.Set2  # Or choose a different color palette
fig = go.Figure()

# Iterate through categories and their subcategories
for i, (category, subcategories) in enumerate(dicts_of_cats_subs_cats.items()):
    start_value = 0  # Track starting position for each category
    for j, subcategory in enumerate(subcategories):
        subcategory_percentage = subcategory_percentages_within_category[subcategory]
        fig.add_trace(go.Bar(
            y=[category],
            x=[subcategory_percentage],
            name=subcategory,
            orientation='h',
            marker=dict(
                color=subcategory_colors[j % len(subcategory_colors)],
                 # Adjust bar width
            )
        ))

        # Add text annotations using subcategory_percentages
        fig.add_annotation(
            x=start_value + subcategory_percentage / 2,
            y=category,
            text=f"{subcategory}\n({subcategory_percentage:.1f}%)",
            xref="x",
            yref="y",
            showarrow=False,
            font=dict(size=10)  # Adjust font size if needed
        )
        start_value += subcategory_percentage

# Adjust layout for stacked bars and visibility
fig.update_layout(
    xaxis_range=[0,100],
    xaxis_tickvals=[0, 25, 50, 75, 100],
    xaxis_ticktext=['0%', '25%', '50%', '75%', '100%'],
    barmode='stack',
      title=dict(text="Category and Sub Category Profit Percentage",font=dict(size=30,color="darkblue")))  # Stack the bars)

fig.write_html("Sales percentage Analysis.html")

fig.show()