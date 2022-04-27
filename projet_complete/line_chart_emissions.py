'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''


import plotly.express as px
from colors import COLORS

def draw(data):
    '''
        Draws the bar chart.

        Arg:
            data: The data to be displayed
        Returns:
            fig: The figure comprising the drawn bar chart
    '''

    

    colors = COLORS
    color_discrete_map = {'Avec taxe carbone': colors[1], 'Avec ETS': colors[0], 'Sans aucune taxe':colors[9] ,'Émissions actuelles':colors[2]}

    hovertemp= '        <b>Année: </b>%{x}<br>'
    hovertemp+='        <b>CO2 émis: </b> %{y} tonnes<br>'
    hovertemp+='<extra></extra>'

    texte = list()
    for col in ['Sans aucune taxe','Avec taxe carbone', 'Avec ETS','Émissions actuelles']:
        tmp = data[col].tolist()
        for i in range(len(tmp)-1):
            tmp[i] = " "
        tmp[-1] = str("{:3.1f}".format(tmp[-1])) + " milliards de tonnes de CO2 rejeté"
        texte.append(tmp)

    fig = px.line(data, x="Year", y=['Émissions actuelles','Sans aucune taxe','Avec taxe carbone', 'Avec ETS'], labels={
                     "Year": "Année",
                     "value": " ",
                     "variable": "Avec quelles taxes ?"
                 },color_discrete_map=color_discrete_map, line_dash='variable')
    fig = fig.update_traces(hovertemplate=hovertemp)

    
    return fig
