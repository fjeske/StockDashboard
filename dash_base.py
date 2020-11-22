import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''symbol to graph:'''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(children='''Data range:'''),
    dcc.DatePickerRange(
        id='my_date_picker_range',
        min_date_allowed=datetime.date(2000, 1, 1),
        max_date_allowed=datetime.datetime.now(),
        initial_visible_month=datetime.datetime.now(),
        first_day_of_week=1,
        clearable=True,
        end_date=datetime.datetime.now()
    ),
    html.Div(id='output_graph')
    ])

@app.callback(
    Output(component_id='output_graph', component_property='children'), 
    [Input(component_id='input', component_property='value'),
    Input(component_id='my_date_picker_range', component_property='start_date'),
    Input(component_id='my_date_picker_range', component_property='end_date')])

def update_value(input_data, start_date, end_date):
    # start = datetime.datetime(2015, 1, 1)
    # end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start_date, end_date)
    return dcc.Graph(id='example_graph', figure={'data': [
        {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
        ],
        'layout': {
            'title': input_data}
            }
        )

if __name__ == '__main__':
    app.run_server()