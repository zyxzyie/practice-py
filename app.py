# ## 將 Ploty 繪製完成的互動式圖表部署至 Dash
# ---
# * Dash HTML Components: 使用 python 產生 HTML 需要的標籤與元素
# * Dash Core Components: 創建互動式UI，包含 figure, filter, 以及 menu

# In[15]:


import dash

# import dash_html_components as html
# import dash_core_components as dcc

from dash import html
from dash import dcc

import plotly_express as px  # require installation
import pandas as pd
import plotly

# In[17]:

df = px.data.gapminder()

# Figure 1
fig1 = px.bar(
    df[df["country"].isin(["Taiwan", "Japan"])],
    x="year", y="gdpPercap", color="country", barmode="overlay",
    height=600
)

# Figure 2
fig2 = px.scatter_matrix(
    df[df["country"].isin(["Taiwan", "Japan"])],
    dimensions=["year", "gdpPercap", "pop"], color="country",
    height=600
)


# * 開一個 app 裡面開一個 html.div 放入 `fig1` & `fig2`

# In[18]:


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(
            figure=fig1
        ),
        dcc.Graph(
            figure=fig2
        )
    ]
)


# In[19]:


if __name__ == "__main__":
    app.run_server(debug=True)
    