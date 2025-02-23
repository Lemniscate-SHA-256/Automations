# screenshot.py
from dash import Dash
import plotly.graph_objects as go
import kaleido

app = Dash(__name__)
fig = go.Figure([go.Box(x=["Conv2D", "Dense"], y=[[0.001], [0.005]])])
fig.write_image(f"box_plot_v{os.environ.get('VERSION', '0.1.1')}.png")