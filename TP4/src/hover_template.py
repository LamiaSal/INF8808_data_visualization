'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    hovertemp= '        <b>Country: </b>%{customdata[0]}<br>'
    hovertemp+='        <b>Population: </b>%{marker.size:,}<br>'
    hovertemp+='        <b>GDP: </b> %{x:,k}$ (USD) </span><br>'
    hovertemp+='        <b>CO2 emissions: </b> %{y} metric tonnes<br>'
    hovertemp+='<extra></extra>'
    return hovertemp
