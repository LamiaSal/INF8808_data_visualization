
import plotly.express as px
from colors import COLORS


def draw(data):
    '''
        Draws the bar chart.

        Arg:
            data: The data to be displayed
        Returns:
            figs: The figures comprising the drawn chart
    '''

    colors = COLORS

    hovertemp1= '        <b>Année: </b>%{x}<br>'
    hovertemp1+="        <b>Revenu généré par l'ETS: </b> %{y} millions de US$<br>"
    hovertemp1+='<extra></extra>'

    hovertemp2= '        <b>Année: </b>%{x}<br>'
    hovertemp2+="        <b>Revenu généré par la taxe carbone: </b> %{y} millions de US$<br>"
    hovertemp2+='<extra></extra>'


    fig1_text = data["ETS"].tolist()
    mf1t = max(fig1_text[:-1])
    for i,v in enumerate(fig1_text[:-1]):
        if v<mf1t:
            fig1_text[i] = " "
        else:
            fig1_text[i] = str("{:3.1f}".format(v))
    fig1_text[-1] = str("{:3.1f}".format(fig1_text[-1])) + " millions US$"
    fig1 = px.line(data_frame = data, x='Year', y='ETS',text=fig1_text,range_x=[2005, 2019], range_y=[0,10], title="...par l'ETS")


    fig2_text = data["Carbon tax"].tolist()
    mf2t = max(fig2_text[:-1])
    for i,v in enumerate(fig2_text[:-1]):

        fig2_text[i] = " "

    fig2_text[-1] = str("{:3.1f}".format(fig2_text[-1])) + " millions US$"

    fig2 = px.line(data_frame = data, x='Year', y='Carbon tax', text=fig2_text, range_x=[2005, 2019], range_y=[0,1300], title="...par la taxe carbone")

    fig1 = fig1.update_layout(showlegend=False,yaxis_title=None, title_x=0.5, xaxis_title = "Année")
    fig1 = fig1.update_traces(line_color=colors[0],textposition='middle left', hovertemplate=hovertemp1)
    fig2 = fig2.update_layout(showlegend=False,yaxis_title=None, title_x=0.5,xaxis_title = "Année")
    fig2 = fig2.update_traces(line_color=colors[1],textposition='middle left', hovertemplate=hovertemp2)
    
    return [fig1,fig2]
