import plotly.express as px
import pandas as pd


df = pd.read_csv("scores.csv")
df["Colors"] = "blue"

colors = ["blue",] * 69
colors[62] = "red"
colors[40] = "orange"

fig = px.bar(df, 
    x="Portal",
    y="Score", 
    color = "Portal", 
    color_discrete_sequence=["LightSkyBlue"],
    color_discrete_map= {
    "San Rafael": "red",
    "Marin": "green",
    "Petaluma": "orange",
    },
    title="Data Portal Scores")

fig.update_yaxes(
    range=(60, 130),
    constrain='domain'
)

fig.add_annotation(
    x=60, 
    y=83,
    text="S.R.",
    font=dict(
        color='black',
        size=18),
    showarrow=True)

fig.add_annotation(
    x=40, 
    y=94,
    text="Marin",
    font=dict(
        color='black',
        size=18),
    showarrow=False)

fig.add_annotation(
    x=63, 
    y=81,
    text="Petaluma",
    font=dict(
        color='black',
        size=18),
    showarrow=False)

fig.update_layout(showlegend=False)

fig.show()
