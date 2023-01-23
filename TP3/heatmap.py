'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import pandas as pd
import hover_template
import preprocess
import plotly.graph_objects as go
import hover_template

def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick.

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # Create the heatmap with dragmode=False in the layout. And, hover template included
    fig = px.imshow(data,labels=dict(color="Trees"),x=data.keys(), y=data.index, color_continuous_scale=px.colors.sequential.Bluyl)
    fig = fig.update_layout(dragmode=False)
    
    fig = fig.update_traces(
        hovertemplate = hover_template.get_heatmap_hover_template()
    )
    return fig
