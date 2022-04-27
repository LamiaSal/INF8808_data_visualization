'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''
from unicodedata import name
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from colors import COLORS
from modes import FRENCH_MODE_TO_COLUMN, MODE_TO_COLUMN
import pandas as pd


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # Update the template to include our new theme and set the title
    fig.update_layout(
        
        title='GHG emissions covered [MtCO2e]',
        dragmode=False,
        barmode='relative'
    )

    return fig


def draw(data, mode):
    '''
        Draws the bar chart.

        Arg:
            data: The data to be displayed
            mode: country selected
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    try :
        custom_mode = MODE_TO_COLUMN[mode]
        fr_custom_mode = FRENCH_MODE_TO_COLUMN[mode]

    except:
        raise ValueError('Please specify a correct value for mode')
    
      # conversion back to Graph Object
    # Update the figure's data according to the selected mode
    # clear figure data
    # fig.data = []
    # for each player we trace the count/percent of lines he speaks in each act
    colors = COLORS
    color_discrete_map = {'Carbon tax': colors[1], 'ETS': colors[0]}
    res = data[data["Country"] == custom_mode]


    hovertemp= '<b>Taxe: </b>%{x}<br>'
    hovertemp+='<b>CO2 couvert: </b> %{y} millions de tonnes<br>'
    hovertemp+='<extra></extra>'


    #updatemenus = [{"type": "dropdown", "buttons": [dict(label="FK",method="animate",args=[None])]}]
    # fig = px.bar(data, x='Type', y='GHG emissions covered [MtCO2e]', animation_frame="Country", animation_group="Type")
    fig = px.bar(res, x='Type', y='GHG emissions covered [MtCO2e]', color="Type", color_discrete_map=color_discrete_map, title='...'+fr_custom_mode+' depuis '+ str(data[data["Country"]==custom_mode]['Year of implementation'].tolist()[0]))
    #fig = fig.update_layout(updatemenus=updatemenus)
    fig = fig.update_layout(showlegend=False,yaxis_title=None, xaxis_title = None)
    fig = fig.update_traces(hovertemplate=hovertemp)
    fig = fig.update_yaxes(autorange=True)


    
    return fig


def get_figure_html(data,country_name):
    return html.Div(className='four columns', children=[
                dcc.Graph(
                    id=country_name,
                    figure=draw(data, country_name)
                )
            ])