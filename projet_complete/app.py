
# -*- coding: utf-8 -*-
from tkinter.ttk import Style
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

import line_chart
import preprocess as preproc
import beeswarm_viz
import world_map_viz


from modes import MODES
import line_chart_revenue
import bar_chart_CO2
from dash.dependencies import Input, Output, State
import line_chart_emissions
import template


# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)
app.title = 'Carbon Tax and ETS, all you need to know | Voilà | INF8808'

template.create_custom_theme()

template.set_default_theme()


# AXE 1
sample_countries = ["Finland", "France", "Ireland", "New Zealand", "Mexico", "Switzerland"]


# AXE 2 imports
# import data into dataframes
dataframe_1 = pd.read_csv('https://raw.githubusercontent.com/LamiaSal/data_project_INF8808/main/assets/Carbon_Pricing_Initiatives/Data_Overall.csv')
dataframe_2 = pd.read_csv('https://raw.githubusercontent.com/LamiaSal/data_project_INF8808/main/assets/dataset_4.csv',sep = ';')

# join dataframes on country names
dataframe_3 = preproc.clean_and_join_dataframes(dataframe_1, dataframe_2) 

df_fig2 = preproc.preprocess_implemented_and_scheduled(dataframe_1)

# figure for the map
fig_map = world_map_viz.draw_map(df_fig2)

# figure for beeswarms
fig_3 = beeswarm_viz.beeswarm_trace_GDB(dataframe_3)
fig_4 = beeswarm_viz.beeswarm_trace_CO2(dataframe_3)


### AXE 3 imports

# CO2 emissions data
emissions_df = preproc.prep_emissions_data()

# general axis 3 data
ax3_data = preproc.prep_ax3_data()

# revenue per tax data
rev_data = preproc.prep_revenue_data()

#figure made from that data
fig_line_revenue = line_chart_revenue.draw(rev_data)
for i in range(2):
    fig_line_revenue[i].layout.xaxis.fixedrange = True
    fig_line_revenue[i].layout.yaxis.fixedrange = True

# CO2 emissions linked to that data
fig_line_emissions = line_chart_emissions.draw(emissions_df)
fig_line_emissions.layout.xaxis.fixedrange = True
fig_line_emissions.layout.yaxis.fixedrange = True



# HTML definition
 
layout_Title = html.Div([
    html.H1("La taxe carbone et l'ETS, intiatives contre le réchauffement climatique")], style={"font-size": "300%"})

layout_intro_page = html.Div([
    html.H5('Par Vincent Du, Victor Nogues, Lamia Salhi, Olivier Bertrand-Vachet et Thomas Côté'),
    html.P('Le réchauffement climatique est un sujet qui est au cœur des débats politiques et qui concerne le monde entier. Il est à la source de dérèglements climatiques qui mettent en danger la vie de certaines populations et mettent en péril la survie de certaines espèces animalières. Aujourd’hui, de nombreux gouvernements ont décidé de prendre de réel mesure contre le réchauffement climatique comme par exemple imposer une taxe carbone ou la taxe ETS. Mais quel est l’intérêt de ces taxes et sont-elles vraiment pertinentes ?'),
])

layout_presentation_initiatives = html.Div([
    html.H3("Que sont les taxes carbone et l'ETS?"),
    dcc.Markdown('''
        Les taxes carbone et l’ETS (Emission Trading System) sont les deux types d’initiatives utilisées afin de réduire l’émission de CO2 et le réchauffement climatique. Depuis plusieurs années, plusieurs pays imposent ces deux initiatives afin de réduire leur émissions de CO2.
        **L'ETS** est le système de droit d’émission de CO2 de l'Union européenne lancé en 2005. Les entreprises ont un quota d’émissions, mise en place d’un marché du carbone permettant d’acheter ou de revendre le CO2 non produit/consommé en excès par rapport aux quotas.
        **La taxe carbone** est sensiblement la même chose à la différence près qu’on ne fixe pas le seuil d’émissions mais le prix du carbone. Donc dans le cadre d’ETS on met une “borne supérieure” sur la production de CO2, là où la taxe carbone fixe le prix du carbone pour encourager les entreprises à polluer moins.
    ''')
])

layout_interet_initiatives = html.Div([
    html.H3("Quel est l'avantage d'implémenter ces initiatives?"),
    html.P("Les principales motivations derrières l'implémentation de ces initiatives pour les gouvernements sont la diminution de l'émission de CO2 et le gain économique. Du côté environnemental, on peut observer, à travers les 6 figures suivants, l'impact qu'une initiative peut avoir sur l'émission de carbone. Chaque figure montre l'émission carbone d'un pays à travers le temps et la date d'établissement d'une mesure (représenté par le point rouge). On peut observer qu'il y a une diminution visible d'émission de CO2 après la mise en place d'une initiative pour chacun des pays présenté dans les figures ci-dessous.")
])

layout_line_charts = html.Div(className='container-fluid', children=[
    html.H4("La taxe Carbone et l'ETS contribue à la baisse de l'émission de CO2 au cours des années"),
    html.Div(className='row', children=[
        line_chart.get_figure_html("Finland"),
        line_chart.get_figure_html("France"),
        line_chart.get_figure_html("Ireland")
    ]),
    html.Div(className='row', children=[
        line_chart.get_figure_html("New Zealand"),
        line_chart.get_figure_html("Mexico"),
        line_chart.get_figure_html("Switzerland")
    ])
], style={'display': 'inline-block', 'vertical-align': 'top', 'horizontal-align': 'center'})

layout_correlation_map = html.Div([
    html.H3('Quels pays utilisent ces taxes?'),
    html.P("Dans cette section, nous allons d'abord analyser quels pays ont présentement implémenté des initiatives de tarification du carbone. Ensuite, nous vous présentons une deuxième visualisation avec les pays qui sont en voie d'implémenter de telles mesures en plus de ces pays pour qui c'est déjà fait. Il est aussi possible de cliquer sur la légende de droite pour visualiser uniquement les catégories de pays d'inérêt. Cette deuxième carte interactive donne un aperçu de ce à quoi ressemblera la situation mondiale de tarification du carbone.")
])

layout_maps = html.Main(className='row', 
            children=[
                dcc.Graph(
                    id='choropleth_1',
                    className='graph',
                    figure=fig_map,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    )
                )
        ], style={'display': 'inline-block', 'vertical-align': 'top', 'horizontal-align': 'center', 'width': '100%'})


layout_correlation_GDP = html.Div([
    html.H3('Les pays qui utilisent les taxes carbone et ETS sont-ils plus riches ?'),
    html.P("Géographiquement on peut constater que la majorité des pays qui implémentent ces taxes sont dans l’hémisphére ce qui nous amène à nous demander si le PIB d’un pays est corrélé à l’implémentation de ces taxes. Le beeswarm suivant nous montre que la plupart des pays qui implémentent ces taxes ont tendance à avoir un PIB par habitant élevé avec l’Ukraine étant le pays au PIB/habitant le plus faible ayant implémenté un des 2 intiatives avec 2124 $ de PIB/habitant.")
])

layout_strip_GDP = html.Main(className='row', 
            children=[
                dcc.Graph(
                    id='scatter_GDP',
                    className='graph',
                    figure=fig_3,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    )
                )
        ], style={'display': 'inline-block', 'vertical-align': 'top', 'horizontal-align': 'center', 'width': '100%'})

layout_correlation_CO2 = html.Div([
    html.H3('Les pays qui utilisent les taxes carbone et ETS émettent-ils moins de CO2 ?'),
    html.P("Si le PIB/habitant est potentiellement corrélé à l’application de ces mesures, l’émission de CO2 pourrait-elle aussi l’être. Et c’est en effet ce qu’on observe ici dans le beeswarm suivant. Les pays qui implémentent ces mesures ont tous émis entre 1.7 et 16 tonnes de C02/habitant en 2018. D’ailleurs, les pays qui émettent peu de CO2 sont souvent également ceux ayant les plus faibles pays.")
])

layout_strip_CO2 = html.Main(className='row', 
            children=[
                dcc.Graph(
                    id='scatter_CO2',
                    className='graph',
                    figure=fig_4,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    )
                )   

        ], style={'display': 'inline-block', 'vertical-align': 'top', 'horizontal-align': 'center', 'width': '100%'})


layout_correlation_CO2_PIB_explication = html.Div([
    html.H3('Les pays qui utilisent les taxes carbone et ETS émettent-ils moins de CO2 ?'),
    html.P("Mais alors pourquoi les pays émergents et en développement n’appliquent pas ces mesures ? Tout d’abord, même si la plupart de ces pays n’émettent pas énormément de C02/habitant ils restent fortement concernés par le réchauffement climatique et sont même parfois les premières victimes de catastrophe naturel. Le Bangladesh en est un exemple, avec un PIB/habitant de 1248$ en 2015 et une émission de CO2/habitant évalué à 0.46 en 2018, ce pays a connu de violentes inondations et précipitations. Ceci a notamment obligé les habitants à migrer, pour beaucoup, vers la capital et à changer complétement leur mode de vie et en particulier leur agriculture. Ensuite, d’après une étude faites OCDE (2021), Taxer la consommation d’énergie au service du développement durable, Certains pays émergent pourrait bénéficier économiquement de ces taxes. Enfin il est difficile d’expliquer réellement pourquoi ces pays n’implémentent pas la taxe carbone ou ETS. Chaque pays a une situation différente économiquement et climatiquement parlant. D’autant plus que ces ne sont pas les seules mesures qui peuvent être réalisés. Notamment, le Kenya tente de proposer des énergies plus propres aux particuliers et aux entreprises et même si le pays n’applique pas l’ETS ou la taxe carbone il prélève des taxes d’accise sur les carburants et a réussi à diminuer fortement ses subventions aux combustibles fossiles (src : https://oecd-development-matters.org/2021/02/17/pourquoi-les-pays-en-developpement-devraient-taxer-la-consommation-de-carbone-alors-meme-que-les-economies-avancees-sont-tres-loin-du-compte/)."
    )
])


layout_ax_3_intro = html.Div([
    html.H3('Pourquoi certains pays implémentent-ils une de ces deux taxes, ou les deux ?'),
    html.P("Contrairement à l’ETS, la taxe carbone ne borne pas les émissions en quantité mais force “simplement” les pollueurs à payer pour pouvoir polluer. En faisant cela, on permet aux entreprises riches de polluer car le prix du carbone est fixé, donc le coût de la pollution est anticipable, là où dans le cas de l’ETS, il est fixé selon un marché d’offre et de demande (et donc dépendant des pollueurs: si plus personne ne pollue moins que son quota il ne reste plus de dépassement à acheter et donc les entreprises ne devraient en théorie plus polluer en dépassant leurs quotas). En résumé, l’ETS régule la quantité d’émissions (et donc la quantité de CO2 rejeté dans l’atmosphère par un pays), et la taxe carbone permet plutôt de pénaliser les gros pollueurs en leur faisant payer ce qu’ils émettent. Cela permet de répondre en partie à la question suivante :")
])

layout_ax_3_vis1_explication = html.Div([
    html.P("Il paraissait intuitif de penser que l'ETS présentait une meilleure efficacité que la taxe carbone du fait de la borne supérieure qu'elle impose aux émissions de CO2. Or nous constatons qu'il n'en est rien... Pourquoi ?")

])
layout_ax3 = html.Main(className='viz-container', 
            children=[
                html.H4("Les émissions couvertes par l'ETS et la taxe carbone (en MtCO2 émises) pour..."),
                html.H6("(le plus grand est meilleur)"),
                html.Div(className='row', children=[
                bar_chart_CO2.get_figure_html(ax3_data,"Switz"),
                bar_chart_CO2.get_figure_html(ax3_data,"Canada"),
                bar_chart_CO2.get_figure_html(ax3_data,"Newfoundland and Labrador")
            ]),
            layout_ax_3_vis1_explication,
            html.P("Tout fait sens quand on change de prisme, et qu'on regarde les revenus générés par ces deux taxes dans les pays qui les ont implémenté en même temps :"),
            html.H4("Revenus (en M US$) en Suisse générés..."),
            html.Div(className='row', children=[
                dcc.Graph(
                id='line_revenue1',
                className='graph',
                figure=fig_line_revenue[0],
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                    )
                ),
                dcc.Graph(
                id='line_revenue2',
                className='graph',
                figure=fig_line_revenue[1],
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                )
            )
            ]),
            html.P("On constate que si la taxe carbone est plus efficace, c'est qu'elle est largement plus rentable que l'ETS, et donc probablement plus utilisée."),
            html.H3("Que se serait-il passé sans aucune de ces deux taxes ?"),
            dcc.Graph(
                id='line_emissions',
                className='graph',
                figure=fig_line_emissions,
                config=dict(
                    scrollZoom=False,
                    showTips=False,
                    showAxisDragHandles=False,
                    doubleClick=False,
                    displayModeBar=False
                )
            ),
            html.P("Il apparaît donc clair que ces taxes, bien que plutôt appliquées pour leur intérêt économique par les pays participants, aident véritablement à réduire nos émissions de gaz à effet de serre.")  

        ], style={'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'})



app.layout = html.Div(className='article', children=[
    layout_Title,
    layout_intro_page,
    layout_presentation_initiatives,
    layout_interet_initiatives,
    layout_line_charts,
    layout_correlation_map,
    layout_maps,
    layout_correlation_GDP, 
    layout_strip_GDP,
    layout_correlation_CO2, 
    layout_strip_CO2,
    layout_correlation_CO2_PIB_explication,
    layout_ax_3_intro,
    layout_ax3
])
