'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    fig.add_trace(trace=go.Choropleth(geojson=montreal_data,featureidkey='properties.NOM',
    locations=locations,z=z_vals,colorscale=colorscale ,showscale=False,marker_line_color='white'))
    
    # scale to the montreal city
    fig.update_geos(
        fitbounds="locations",
        visible=False,
    )

    # change projection style to the mercator one
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type="mercator"
        )
    )
    fig.update_traces(
        hovertemplate = hover.map_base_hover_template()
    )

    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter traces
    '''
    
    # TODO : Add the scatter markers to the map base
    
    uniq_val_legend = street_df["properties.TYPE_SITE_INTERVENTION"].unique()
    colors = px.colors.qualitative.Plotly
    for (i,value) in enumerate(uniq_val_legend):
        
        street_df_i = street_df[street_df["properties.TYPE_SITE_INTERVENTION"]==value]
        fig.add_trace(trace = go.Scattergeo(
            lat=street_df_i["properties.LATITUDE"], 
            lon=street_df_i["properties.LONGITUDE"],
            marker=dict(size=9,color=colors[i]),
            mode='markers',
            opacity=0.5,
            name = value,
            hovertemplate = hover.map_marker_hover_template(value),
            customdata=street_df_i[['properties.NOM_PROJET', 'properties.MODE_IMPLANTATION', 'properties.OBJECTIF_THEMATIQUE']]))
        
        
    fig.update_layout(
    title="Explorez les rues pietonnes de Montréal <br><sup>Cliquez sur un marqueur pour plus d'informations</sup>",
    legend_title="Légende"
    )
    return fig
