'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import pandas as pd
import hover_template
import preprocess
import plotly.graph_objects as go
import hover_template
from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    fig = px.line()
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.update_layout(dragmode=False)
    
    # Update axes properties
    fig.update_xaxes(
        range = [0, 1],
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    fig.update_yaxes(
        range = [0, 1],
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    )

    
    #add the rectangle
    fig.add_shape(
        type="rect",
        x0=0, 
        y0=0.25, 
        x1=1, 
        y1=0.75,
        line=dict(color=THEME['pale_color']),fillcolor=THEME['pale_color'],
        )
    
    #add the error message
    fig.add_annotation(
        text="No data to display. Select a cell in the heatmap for more information",
        x=0.5, y=0.5, 
        showarrow=False,
        xref = "paper",
        yref = "paper"
    )
    

    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    #  Construct the required figure. Don't forget to include the hover template
    line_data.columns=[year, arrond]

    #if there is only one data, we display a single point
    if line_data.shape[0] == 1:
        fig = px.scatter(line_data, x=year, y=arrond,title="Trees planted in " + arrond + " in " + str(year))

        # update tickmarks for daily information
        fig.update_xaxes(
            title=None,
            tickformat='%d %b'
            )
        
    else:
        fig = px.line(line_data, x=year, y=arrond,title="Trees planted in " + arrond + " in " + str(year))

        # update tickmarks for monthly information
        fig.update_xaxes(
            title=None,
            dtick='M1',
            tickformat='%d %b'
            )

    # update the y label
    fig.update_yaxes(title="Trees")
        
    fig.update_layout(dragmode=False)

    # defining the line chart
    fig = fig.update_traces(
        hovertemplate = hover_template.get_linechart_hover_template()
    )
    return fig