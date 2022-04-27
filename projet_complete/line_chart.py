'''
    Contains some functions related to the creation of the six line charts
    The line charts will display the CO2 emission of a country since 1960
    It will also display the date of implementation of a taxe on Carbon to visualize the impact of these initiatives 
'''
import pandas as pd
from hover_template import hover_template_line_chart, hover_template_scatter
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

def get_figure(country_name):
    dataframe = pd.read_csv('https://raw.githubusercontent.com/LamiaSal/data_project_INF8808/main/assets/CO2%20emission%206%20countries.csv')
    df = dataframe.loc[dataframe["country"] == country_name]
    fig = px.line(df, x="year", y="emission", title=country_name+' CO2 Emission')
    
    # Legend
    fig.update_layout(legend=dict(
        #orientation = "h",
        yanchor="top",
        y=0.9999,
        xanchor="left",
        x=0.01
    ))
    # Title & Axis
    fig.update_layout(title_x=0.5,
                   xaxis_title='Année')
                   #yaxis_title='Émission de CO2 (tonne par habitant)')
    
    # Line color & Hover
    fig.update_traces(line_color='green', hovertemplate=hover_template_line_chart())
    
    # fig.update_traces(mode='markers+lines')
    #Adding the information about the implementation of the iniatives 
    if(country_name =='Finland'):
        fig.update_layout(title = "En Finlande")
        fig.add_trace(go.Scatter(x=[1990], y=[10.9416936], name='Taxe Carbone 1990', hovertemplate = hover_template_scatter(country_name, "Carbon Tax")))
        fig.add_shape(type='line',x0=1990, y0=0, x1=1990, y1=15.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_layout(yaxis_title='Émission de CO2 (tonne par habitant)')
    if(country_name =='France'):
        fig.update_layout(title = "En France")
        fig.add_trace(go.Scatter(x=[2014], y=[4.59237683], name='Taxe Carbone 2014', hovertemplate = hover_template_scatter(country_name, "Carbon Tax")))
        fig.add_shape(type='line',x0=2014, y0=0, x1=2014, y1=15.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_yaxes(visible=False)
    if(country_name =='Ireland'):
        fig.update_layout(title = "En Irelande")
        fig.add_trace(go.Scatter(x=[2010], y=[8.90978486],  name='Taxe Carbone 2010', hovertemplate = hover_template_scatter(country_name, "Carbon Tax")))
        fig.add_shape(type='line',x0=2010, y0=0, x1=2010, y1=15.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_yaxes(visible=False)
    if(country_name =='New Zealand'):
        fig.update_layout(title = "En Nouvelle Zéalande")
        fig.add_trace(go.Scatter(x=[2008], y=[8.06845392], name='ETS 2008', hovertemplate = hover_template_scatter(country_name, "ETS")))
        fig.add_shape(type='line',x0=2008, y0=0, x1=2008, y1=9.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_layout(yaxis_title='Émission de CO2 (tonne par habitant)')
    if(country_name =='Mexico'):
        fig.update_layout(title = "Au Mexique")
        fig.add_trace(go.Scatter(x=[2014], y=[3.80806346],  name='ETS 2014', hovertemplate = hover_template_scatter(country_name, "ETS")))
        fig.add_shape(type='line',x0=2014, y0=0, x1=2014, y1=9.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_yaxes(visible=False)
    if(country_name =='Switzerland'):
        fig.update_layout(title = "En Suisse")
        fig.add_trace(go.Scatter(x=[2008], y=[5.87891091], name='ETS 2008', hovertemplate = hover_template_scatter(country_name, "ETS")))
        fig.add_shape(type='line',x0=2008, y0=0, x1=2008, y1=9.0, line=dict(color='orangered',), xref='x', yref='y')
        fig.update_yaxes(visible=False)
        
    return fig


def get_figure_html(country_name):
    return html.Div(className='four columns', children=[
                dcc.Graph(
                    id=country_name,
                    figure=get_figure(country_name)
                )
            ])
