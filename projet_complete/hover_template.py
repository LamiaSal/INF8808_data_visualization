def hover_template_map(countries, status):
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hovertemplate = '<b> Pays : </b><span>' + countries + ' </span><br>'
    hovertemplate += '<b> Status : </b><span>' + status +'</span><br>'
    hovertemplate += '<extra></extra>'
    return hovertemplate

def hover_template_strip(x, x_name, type,  hovertext):
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hovertemplate = '<b>%{hovertext}</b><br><br>'
    hovertemplate += 'Code du Pays : %{customdata[0]}<br>'
    hovertemplate += 'Type : ' + type +'<br>'
    hovertemplate += x_name + ' : %{x}<br>'
    hovertemplate += '<extra></extra>'
    return hovertemplate

def hover_template_line_chart():
    hovertemplate = "Année: %{x}<br>" 
    hovertemplate += "Emission de CO2: %{y:.2f}<br>"
    hovertemplate += "<extra></extra>"
    return hovertemplate

def hover_template_scatter(country_name, initiative_name):
    hovertemplate = "<b>" + country_name + " " + initiative_name +  "<br>Implémenté en " + "%{x}</b>"
    return hovertemplate