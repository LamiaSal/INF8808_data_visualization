'''
    Contains the functions to set up the map visualization.
'''

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

import hover_template as hover

def draw_map(df):
    '''
        Description
        Args:
            fig: The figure to add the map
        Returns:
            fig: The updated figure with the map

    '''
    # Draw the map
    fig = px.choropleth(df, locations='Country', locationmode='country names', scope='world',
        color='Status', color_discrete_map={'Implemented':'green', 'Scheduled':'orange'})
    
    fig.update_geos(
        projection_type="natural earth",
        resolution=50,
        showland=True, landcolor="LightYellow",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="Blue"
        )
    
    # hover
    for data in fig.data :
        data.hovertemplate = hover.hover_template_map(data.locations, data.name)
    return fig
    


