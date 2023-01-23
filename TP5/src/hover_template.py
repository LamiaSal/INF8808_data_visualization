'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    hovertemp='    <span style="font-family:Oswald"> %{properties.NOM} </span><br>'
    hovertemp+='<extra></extra>'
    return hovertemp



def map_marker_hover_template(name):
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    hovertemp='    <span style="font-family:Oswald"> '+name+'</span><br>'
    hovertemp+='<extra></extra>'
    return hovertemp