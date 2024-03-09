import pandas as pd
import plotly.graph_objects as go
df2=pd.read_csv('Main Port/Retail sales analysis.csv')

df = pd.DataFrame(df2)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year']=df['Order Date'].dt.year

profit_per_cat_subcate=df.groupby(['Category','Sub Category'])['Profit'].sum().reset_index()

# for the first bar to show all the profits year per regions
Profit_category=df.groupby('Category')['Profit'].sum().reset_index()
#finding profit if the product is sold 20% more than the Cost Of the Goods Sold to Business(COGS)

list_sub_cat=list(profit_per_cat_subcate["Sub Category"])


#lists for x,y
cat_pro=list(Profit_category['Profit'])
list_cats=list(set(Profit_category['Category']))
list_s_cats=list(profit_per_cat_subcate['Sub Category'])
list_su_Pro_cat=list(profit_per_cat_subcate['Profit'])

dicts_of_cats_subs_cats={}
for j in list_cats:
    subcatse_cats=df[df.Category.isin([j])]
    subcatse_cats=subcatse_cats["Sub Category"]
    list_Sub_cats_in_dict=list(set(subcatse_cats))
    dicts_of_cats_subs_cats[j] = list_Sub_cats_in_dict 
# Create a dictionary to store monthly sales for each year
category_profit_dict = {
    cat: list(profit_per_cat_subcate.loc[profit_per_cat_subcate['Category'] == cat, 'Profit'])
    for cat in list_cats
}

# Create a dictionary to store profits by subcategory for each category
subcategory_profit_dict = {
    cat: list(profit_per_cat_subcate.loc[profit_per_cat_subcate['Category'] == cat, 'Profit'])
    for cat in list_cats
}

# Create a dictionary to store subcategories for each category
category_subcategory_dict = {
    cat: list(profit_per_cat_subcate.loc[profit_per_cat_subcate['Category'] == cat, 'Sub Category'])
    for cat in list_cats
}

subcategory_colors = ['rgb(0, 0, 255)', 'rgb(255, 0, 0)', 'rgb(255, 255, 0)', 'rgb(0, 128, 0)', 'rgb(128, 0, 128)', 'rgb(255, 0, 255)', 'rgb(200, 200, 200)']


cat_text= [f"Category:{cat}<br> Profit:{pro}" for cat,pro in zip(list_cats,cat_pro)]

fig = go.Figure(data=[go.Bar(x=list_cats, y=cat_pro,marker_color="dodgerblue",text=cat_text)])
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label="(Total Profits by Category)",
                    args=[{
                        "x": [list_cats],
                        "y": [cat_pro],
                        "marker_color": ['rgb(0, 0, 80)'] * len(list_cats),  
                        "text":[cat_text] #Blue
                    }],
                    method="update",
                ),
                *[
                    dict(
                        args=[{
                            "x": [category_subcategory_dict[j]],  # Use subcategories as x-axis labels
                            "y": [subcategory_profit_dict[j]],
                            "text":[[f"Category: {j}<br>Subcategory: {sub}<br>Profit: {profit}"
                         for sub, profit in zip(category_subcategory_dict[j], subcategory_profit_dict[j])]]
                         }],
                            
                        label=str(j),
                        method="update"
                    ) for j in list_cats
                ]
            ],
            direction="down"
        )
    ],
    title=dict(text="Analysis of Profit by Category & Sub category",font=dict(size=30,color="indigo"))
)
fig.write_html("Analysis Of profit by Cat and Subcat.html")
fig.show()