# import all required libraries  

import pandas as pd
import webbrowser

import dash
import dash_html_components as html
from dash.dependencies import Input, State, Output 
import dash_core_components as dcc 
import plotly.graph_objects as go  
import plotly.express as px
from dash.exceptions import PreventUpdate

# creating an object for dash nameing it as app

app = dash.Dash()


def load_data():                          # a method written to read the data from csv and get required data and sort them for the dropdowns
  dataset_name = "global_terror.csv"

  pd.options.mode.chained_assignment = None
  
  global df
  df = pd.read_csv(dataset_name)
  
  global month_list
  month = {
         "January":1,
         "February": 2,
         "March": 3,
         "April":4,
         "May":5,
         "June":6,
         "July": 7,
         "August":8,
         "September":9,
         "October":10,
         "November":11,
         "December":12
         }
  month_list= [{"label":key, "value":values} for key,values in month.items()]

  global date_list
  date_list = [x for x in range(1, 32)]


  global region_list
  region_list = [{"label": str(i), "value": str(i)}  for i in sorted( df['region_txt'].unique().tolist() ) ]
  
  global country_list
  country_list = df.groupby("region_txt")["country_txt"].unique().apply(list).to_dict()


  global state_list
  state_list = df.groupby("country_txt")["provstate"].unique().apply(list).to_dict()


  global city_list
  city_list  = df.groupby("provstate")["city"].unique().apply(list).to_dict()


  global attack_type_list
  attack_type_list = [{"label": str(i), "value": str(i)}  for i in df['attacktype1_txt'].unique().tolist()]


  global year_list
  year_list = sorted ( df['iyear'].unique().tolist()  )

  global year_dict
  year_dict = {str(year): str(year) for year in year_list}

  global chart_dropdown_values
  chart_dropdown_values = {"Terrorist Organisation":'gname', 
                             "Target Nationality":'natlty1_txt', 
                             "Target Type":'targtype1_txt', 
                             "Type of Attack":'attacktype1_txt', 
                             "Weapon Type":'weaptype1_txt', 
                             "Region":'region_txt', 
                             "Country Attacked":'country_txt'
                          }
                              
  chart_dropdown_values = [{"label":keys, "value":value} for keys, value in chart_dropdown_values.items()]
  
def open_browser():
  webbrowser.open_new('http://127.0.0.1:8050/')

def create_app_ui():

  dropdown_style={
        'width': '99%',
        'margin': 'auto',
        "padding-top": "4px",
        "padding-bottom": "2px",
        "border-radius":"25px"
   }

  main_layout = html.Div(
      style={"background-color": "#FFE9DB"},
      className="Test",
      children=[
  html.H1('Terrorism Analysis with Insights', id='Main_title',style={"text-align": "center","background-color": "#FFA38A","margin":"0","padding-top": "7px","padding-bottom": "7px"}),
    dcc.Tabs(id="Tabs", value="Map",children=[
      dcc.Tab(label="Map tool   "	u"\U0001F30D" ,selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"},id="Map tool",value="Map",children=[
          dcc.Tabs(id = "subtabs", value = "WorldMap",children = [
              dcc.Tab(label="World Map tool   "	u"\U0001F30D",selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"}, id="World", value="WorldMap"),
              dcc.Tab(label="India Map tool   "	u"\U0001F30D",selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"}, id="India", value="IndiaMap")
              ]),
          dcc.Dropdown(
              id='month', 
                options=month_list,
                placeholder='Select Month',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='date', 
                placeholder='Select Day',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='region_dropdown', 
                options=region_list,
                placeholder='Select Region',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='country_dropdown', 
                options=[{'label': 'All', 'value': 'All'}],
                placeholder='Select Country',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='state_dropdown', 
                options=[{'label': 'All', 'value': 'All'}],
                placeholder='Select State or Province',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='city_dropdown', 
                options=[{'label': 'All', 'value': 'All'}],
                placeholder='Select City',
                multi = True,
                style=dropdown_style
                  ),
          dcc.Dropdown(
                id='attacktype_dropdown', 
                options=attack_type_list,
                placeholder='Select Attack Type',
                multi = True,
                style=dropdown_style
                  ),

          html.H4('Select the Year', id='year_title',style={"padding-left": "20px"}),
          dcc.RangeSlider(
                    id='year_slider',
                    min=min(year_list),
                    max=max(year_list),
                    value=[min(year_list),max(year_list)],
                    marks=year_dict,
                    step=None
                      ),
    ]),
      dcc.Tab(label = "Chart Tool   " u"\U0001F4CA",selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"}, id="chart tool", value="Chart", children=[
          dcc.Tabs(id = "subtabs2", value = "WorldChart",children = [
              dcc.Tab(label="World Chart tool   "u"\U0001F4CA",selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"}, id="WorldC", value="WorldChart"),          
            dcc.Tab(label="India Chart tool   "u"\U0001F4CA",selected_style={"fontWeight": "bold"},style={"fontWeight": "bold"}, id="IndiaC", value="IndiaChart")]),
            dcc.Dropdown(id="Chart_Dropdown", options = chart_dropdown_values, placeholder="Select option", value = "region_txt",style={'width': '99%','margin': 'auto',"padding-top": "2px","padding-bottom": "2px","border-radius":"25px"}), 
            html.Br(),
            html.Hr(),
            html.Center( dcc.Input(id="search", placeholder="Search Filter",style={"width":"97%","padding-bottom": "10px","padding-top": "10px","border-radius":"25px"}) ),
            html.Hr(),
            html.Br(),
            html.H4('Select the Year', id='year_titlee',style={"padding-left": "20px"}),
            dcc.RangeSlider(
                    id='cyear_slider',
                    min=min(year_list),
                    max=max(year_list),
                    value=[min(year_list),max(year_list)],
                    marks=year_dict,
                    step=None
                      ),
            html.Br()
              ]),
         ]),
    dcc.Loading(children=[dcc.Graph(id='graph-object')],type='graph',style={"backgroundColor": "transparent","z-index":"1","position":"absolute"}),
    html.Footer(id= "footer",
        style={"padding-bottom": "1px"},
        children=[
            html.H3(style={"text-align": "center"},children=[
                html.H3(children="Made with ",style={"display": "inline"}),
                html.H3(children="\u2764",style={"color":"red","display": "inline"}),
                html.H3(children=" by ESWAR",style={"display": "inline"}),
                ]) 
            ])
  

  ])
        
  return main_layout

@app.callback(dash.dependencies.Output('graph-object', 'figure'),
    [
     dash.dependencies.Input("Tabs", "value"),
    dash.dependencies.Input('month', 'value'),
    dash.dependencies.Input('date', 'value'),
    dash.dependencies.Input('region_dropdown', 'value'),
    dash.dependencies.Input('country_dropdown', 'value'),
    dash.dependencies.Input('state_dropdown', 'value'),
    dash.dependencies.Input('city_dropdown', 'value'),
    dash.dependencies.Input('attacktype_dropdown', 'value'),
    dash.dependencies.Input('year_slider', 'value'), 
    dash.dependencies.Input('cyear_slider', 'value'), 
    
    dash.dependencies.Input("Chart_Dropdown", "value"),
    dash.dependencies.Input("search", "value"),
    dash.dependencies.Input("subtabs2", "value")
    ]
    )

def update_app9_ui(Tabs, month_value, date_value,region_value,country_value,state_value,city_value,attack_value,year_value,chart_year_selector, chart_dp_value, search,
                   subtabs2):
    figure = None
     
    if Tabs == "Map":
        print("Data Type of month value = " , str(type(month_value)))
        print("Data of month value = " , month_value)
        
        print("Data Type of Day value = " , str(type(date_value)))
        print("Data of Day value = " , date_value)
        
        print("Data Type of region value = " , str(type(region_value)))
        print("Data of region value = " , region_value)
        
        print("Data Type of country value = " , str(type(country_value)))
        print("Data of country value = " , country_value)
        
        print("Data Type of state value = " , str(type(state_value)))
        print("Data of state value = " , state_value)
        
        print("Data Type of city value = " , str(type(city_value)))
        print("Data of city value = " , city_value)
        
        print("Data Type of Attack value = " , str(type(attack_value)))
        print("Data of Attack value = " , attack_value)
        
        print("Data Type of year value = " , str(type(year_value)))
        print("Data of year value = " , year_value)

        # year_filter
        year_range = range(year_value[0], year_value[1]+1)
        new_df = df[df["iyear"].isin(year_range)]
        
        # month_filter
        if month_value==[] or month_value is None:
            pass
        else:
            if date_value==[] or date_value is None:
                new_df = new_df[new_df["imonth"].isin(month_value)]
            else:
                new_df = new_df[new_df["imonth"].isin(month_value)
                                & (new_df["iday"].isin(date_value))]

        # region, country, state, city filter
        if region_value==[] or region_value is None:
            pass
        else:
            if country_value==[] or country_value is None :
                new_df = new_df[new_df["region_txt"].isin(region_value)]
            else:
                if state_value == [] or state_value is None:
                    new_df = new_df[(new_df["region_txt"].isin(region_value))&
                                    (new_df["country_txt"].isin(country_value))]
                else:
                    if city_value == [] or city_value is None:
                        new_df = new_df[(new_df["region_txt"].isin(region_value))&
                        (new_df["country_txt"].isin(country_value)) &
                        (new_df["provstate"].isin(state_value))]
                    else:
                        new_df = new_df[(new_df["region_txt"].isin(region_value))&
                        (new_df["country_txt"].isin(country_value)) &
                        (new_df["provstate"].isin(state_value))&
                        (new_df["city"].isin(city_value))]
                        
        if attack_value == [] or attack_value is None:
            pass
        else:
            new_df = new_df[new_df["attacktype1_txt"].isin(attack_value)] 
              
        mapFigure = go.Figure()
        if new_df.shape[0]:
            pass
        else: 
            new_df = pd.DataFrame(columns = ['iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate',
               'city', 'latitude', 'longitude', 'attacktype1_txt', 'nkill'])
            
            new_df.loc[0] = [0, 0 ,0, None, None, None, None, None, None, None, None]
            
        
        mapFigure = px.scatter_mapbox(new_df,
          lat="latitude", 
          lon="longitude",
          color="attacktype1_txt",
          hover_name="city", 
          hover_data=["region_txt", "country_txt", "provstate","city", "attacktype1_txt","nkill","iyear","imonth", "iday"],
          zoom=1
          )                       
        mapFigure.update_layout(mapbox_style="open-street-map",
          autosize=True,
          margin=dict(l=20, r=20, t=20, b=20),
          )
          
        figure = mapFigure

    elif Tabs=="Chart":
        figure = None
        
        
        year_range_c = range(chart_year_selector[0], chart_year_selector[1]+1)
        chart_df = df[df["iyear"].isin(year_range_c)]
        
        
        if subtabs2 == "WorldChart":
            pass
        elif subtabs2 == "IndiaChart":
            chart_df = chart_df[(chart_df["region_txt"]=="South Asia") &(chart_df["country_txt"]=="India")]
        if chart_dp_value is not None and chart_df.shape[0]:
            if search is not None:
                chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name = "count")
                chart_df  = chart_df[chart_df[chart_dp_value].str.contains(search, case=False)]
            else:
                chart_df = chart_df.groupby("iyear")[chart_dp_value].value_counts().reset_index(name="count")
        
        
        if chart_df.shape[0]:
            pass
        else: 
            chart_df = pd.DataFrame(columns = ['iyear', 'count', chart_dp_value])
            
            chart_df.loc[0] = [0, 0,"No data"]
        chartFigure = px.area(chart_df, x="iyear", y ="count", color = chart_dp_value)
        figure = chartFigure
    return figure

@app.callback(
  Output("date", "options"),
  [Input("month", "value")])
def update_date(month):
    option = []
    if month:
        option= [{"label":m, "value":m} for m in date_list]
    return option

@app.callback([Output("region_dropdown", "value"),
               Output("region_dropdown", "disabled"),
               Output("country_dropdown", "value"),
               Output("country_dropdown", "disabled")],
              [Input("subtabs", "value")])
def update_r(tab):
    region = None
    disabled_r = False
    country = None
    disabled_c = False
    if tab == "WorldMap":
        pass
    elif tab=="IndiaMap":
        region = ["South Asia"]
        disabled_r = True
        country = ["India"]
        disabled_c = True
    return region, disabled_r, country, disabled_c

@app.callback(
    Output('country_dropdown', 'options'),
    [Input('region_dropdown', 'value')])
def set_country_options(region_value):
    option = []
    if region_value is  None:
        raise PreventUpdate
    else:
        for var in region_value:
            if var in country_list.keys():
                option.extend(country_list[var])
    return [{'label':m , 'value':m} for m in option]

@app.callback(
    Output('state_dropdown', 'options'),
    [Input('country_dropdown', 'value')])
def set_state_options(country_value):
    option = []
    if country_value is None :
        raise PreventUpdate
    else:
        for var in country_value:
            if var in state_list.keys():
                option.extend(state_list[var])
    return [{'label':m , 'value':m} for m in option]

@app.callback(
    Output('city_dropdown', 'options'),
    [Input('state_dropdown', 'value')])
def set_city_options(state_value):
    option = []
    if state_value is None:
        raise PreventUpdate
    else:
        for var in state_value:
            if var in city_list.keys():
                option.extend(city_list[var])
    return [{'label':m , 'value':m} for m in option]


def application():

  load_data()
  
  open_browser()
  
  global app
  app.layout = create_app_ui()

  app.title = "Terrorism Analysis with Insights"
 
  app.run_server()

  print("Stopped by the user")
  #df = None
  app = None

if __name__ == '__main__':
    application()
