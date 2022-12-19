import plotly.express as px
import pandas as pd

df = pd.read_csv('score_breakdown.csv')

fig = px.bar(df, 
    x="Score", 
    y="Category", 
    color="Score",
    color_continuous_scale=["#ed4411", "#faf205", "#4ef048"],
    title="Average Score per Category"
)

#fig.update_xaxes(tickangle=90)
fig.update_layout(coloraxis_showscale=False)
fig.update_layout(yaxis={'categoryorder':'total descending'})

fig.show()