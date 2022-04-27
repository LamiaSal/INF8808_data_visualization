'''
    Contains the functions to set up the beeswarm visualization.
'''

import plotly.express as px
import hover_template as hover
from colors import COLORS

def beeswarm_trace_GDB(df):
    '''
        Description
        Args:
            df: dataframe
        Returns:
            fig: The figure with the beeswarm trace regarding GDP/capite data

    '''
    colors = COLORS
    # setting color of legend
    color_discrete_map = {'Taxe Carbone': colors[1], 'ETS': colors[0], 'ETS & Taxe Carbone':colors[2] ,'Aucune taxe':colors[9]}
    #{'Country Name': 'Pays','Country Code':'Code du Pays','CO2 emissions (metric tons per capita)':'Émission deCO2 (tonne par habitant)', 'GDP per capita (current US$)':'PIB/habitant (US$)'}
    #defining beeswarm
    fig = px.strip(df, \
        x='PIB/habitant (US$)',\
        log_x=True,\
        color='Type',\
        stripmode='overlay',\
        color_discrete_map=color_discrete_map,\
        category_orders={'Type': ['Aucune taxe','Taxe Carbone','ETS','ETS & Taxe Carbone']}, \
        hover_name = 'Pays',\
        hover_data=['Code du Pays'],
            ).update_traces(jitter = 0.2)
    for data in fig.data :
        data.hovertemplate = hover.hover_template_strip(data.x, 'PIB/habitant (US$)', data.name, data.hovertext)
    
    
    fig.update_layout(title_text="Les pays appliquant ces taxes sont des pays développés (données 2015)", title_x=0.5)
    
    # Legend
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor="whitesmoke",
        bordercolor="Black",
        borderwidth=1
    ))

    return fig

def beeswarm_trace_CO2(df):
    '''
        Description
        Args:
            df: dataframe
        Returns:
            fig: The figure with the beeswarm trace regarding CO2/capita data

    '''
    colors = COLORS
    # setting color of legend
    color_discrete_map = {'Taxe Carbone': colors[1], 'ETS': colors[0], 'ETS & Taxe Carbone':colors[2] ,'Aucune taxe':colors[9]}
    
    #defining beeswarm
    fig = px.strip(df, \
        x='Émission de CO2 (tonne par habitant)',\
        log_x=True,\
        color='Type',\
        stripmode='overlay',\
        color_discrete_map=color_discrete_map,\
        category_orders={'Type': ['Aucune taxe','Taxe Carbone','ETS','ETS & Taxe Carbone']}, \
        hover_name = 'Pays',\
        hover_data=['Code du Pays']\
            ).update_traces(jitter = 0.2)
    
    for data in fig.data :
        data.hovertemplate = hover.hover_template_strip(data.x,'Émission de CO2 (tonne par habitant)',  data.name, data.hovertext)
    
    #title
    fig.update_layout(title_text="Les pays appliquant ces taxes sont ceux qui émettent le plus de CO2/habitant (données 2018)", title_x=0.5)

    # Legend
    fig.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor="whitesmoke",
        bordercolor="Black",
        borderwidth=1
    ))

    return fig