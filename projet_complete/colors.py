import plotly.express as px

# colors for the whole website
COLORS = px.colors.qualitative.Plotly
COLORS[0], COLORS[3], COLORS[1], COLORS[4] = COLORS[3], COLORS[0], COLORS[4], COLORS[1]
COLORS[9] = "#BAB0AC"