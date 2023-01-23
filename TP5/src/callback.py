'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html
import preprocess as preproc

def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    style['visibility'] = 'hidden'
    
    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    style['visibility'] = 'visible'
    style['white-space'] = 'pre-wrap'

    panel = figure['data'][curve]['customdata'][point]
    color = figure['data'][curve]['marker']['color']

    title = html.Div(panel[0], style={'color': color}) #'properties.NOM_PROJET'
    mode = panel[1] #'properties.MODE_IMPLANTATION'

    if panel[2] is not None:
        theme_list = str(panel[2]).split('\n')
        for i in range(len(theme_list)):
            theme_list[i] = ('\t\u2022 ' + theme_list[i]) #'properties.OBJECTIF_THEMATIQUE'
        theme_list = ['Thématique:\n'] + theme_list 
        theme = '\n'.join(theme_list) + '\n\n'
    else:
        theme = ''

    return title, mode, theme, style
