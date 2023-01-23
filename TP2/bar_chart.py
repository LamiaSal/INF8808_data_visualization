'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

from turtle import pd, title, update
import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN
import pandas as pd


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'
        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # Update the template to include our new theme and set the title
    fig.update_layout(
        #we combine simple_white template with the draft one defined in template.py
        template=pio.templates['simple_white+draft'], 
        title='Lines per act',
        dragmode=False,
        barmode='relative'
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    try :
        custom_mode = MODE_TO_COLUMN[mode]

    except:
        raise ValueError('Please specify a correct value for mode')
    
    acts = pd.unique(data["Act"]).tolist()
    characters = pd.unique(data["Player"]).tolist()
    characters = sorted(characters)

    fig = go.Figure(fig)  # conversion back to Graph Object
    
    # Update the figure's data according to the selected mode
    # clear figure data
    fig.data = []

    # for each player we trace the count/percent of lines he speaks in each act
    for player in characters:
        res = list()
        for act in acts:
            player_data = data[data['Player'] == player]
            # if the player doesn't speak in the current act we add 0 to the res list
            if act not in pd.unique(player_data['Act']).tolist():
                res.append(0)
            else:
                tmp = player_data[player_data['Act'] == act]
                res.append(tmp[custom_mode].tolist()[0]) #depending on the mode we display the count or the percent
        
        # we draw the data from the current player
        fig = fig.add_trace(
            go.Bar(
                name = player, x = acts, y = res,
                hoverlabel = dict(bgcolor = 'white'),
                hovertemplate=get_hover_template(player,mode)
            )
        )
    
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count)' depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # Update the y axis title according to the current mode
    try :
        custom_mode = MODE_TO_COLUMN[mode]
    except:
        raise ValueError('Please specify a correct value for mode')
    if custom_mode == "LineCount":
        fig = fig.update_layout(
            yaxis_title='Lines (Count)')
    else:
        fig = fig.update_layout(
            yaxis_title='Lines (%)')
    return fig