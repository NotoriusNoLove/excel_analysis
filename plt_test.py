import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# Функция для получения числа из income_archive


def income_archive(ar, br):
    # Ваша логика для получения числа из архива доходов
    # Здесь можно использовать переданные аргументы и ключевые слова

    # Возвращаемое число из архива доходов
    return ar


# Создаем экземпляр Dash
app = dash.Dash(__name__)
app.layout = html.Div(style={'width': '100%', 'height': '100vh', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', "background-color": "black"},
                      children=[
                          html.H3("Fin Stat Dashboard", style={
                                  'position': 'absolute', 'top': '10px', 'left': '100px'}),
                          html.Button('Обновить', id='update-button', n_clicks=0,
                                      style={'position': 'absolute', 'top': '20px', 'left': '20px'}),
                          html.Div(style={'position': 'relative', 'width': '400px', 'height': '400px'},
                                   children=[
                                       html.Div(style={'position': 'absolute', 'top': '50%', 'left': '50%', 'transform': 'translate(-50%, -50%)', 'width': '200px', 'height': '200px', 'border-radius': '50%', 'background-color': 'purple', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})
                                       ]),
                                       html.Div(style={'font-family': 'Arial', 'font-size': '24px', 'position': 'absolute', 'position': 'absolute', 'top': '-30%', 'left': '80%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'red'},
                                                children=[
                                                    html.Div(
                                                        id='number-display1', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white', 'font-family': 'Arial', 'font-size': '24px', 'position': 'absolute'})]),
                                       html.Div(style={'position': 'absolute', 'top': '-25%', 'left': '20%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'purple'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})]),
                                       html.Div(style={'position': 'absolute', 'top': '120%', 'left': '40%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'purple'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})]),
                                       html.Div(style={'position': 'absolute', 'top': '20%', 'left': '120%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'purple'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})]),
                                       html.Div(style={'position': 'absolute', 'top': '90%', 'left': '130%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'purple'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})]),
                                       html.Div(style={'position': 'absolute', 'top': '70%', 'left': '-30%', 'transform': 'translate(-50%, -50%)',
                                                'width': '140px', 'height': '140px', 'border-radius': '50%', 'background-color': 'purple'},
                                                children=[
                                                    html.Div(
                                                        id='number-display', children=(f"{income_archive(4, 2)} \n income acrh"), style={'color': 'white'})]),
                              html.Table(style={'position': 'absolute', 'bottom': '-220px', 'left': '-700px', 'font-family': 'Arial', 'font-size': '20px'},
                                         children=[
                                  html.Tr([html.Th('Category'), html.Th(
                                      'Value'), html.Th('Count')]),
                                  html.Tr([html.Td('Advertising'), html.Td(
                                      '2.0'), html.Td('2844.0')]),
                                  html.Tr([html.Td('Asset sale'), html.Td(
                                      '0.0'), html.Td('26.0')]),
                                  html.Tr([html.Td('Licensing'), html.Td(
                                      '62.0'), html.Td('72768.0')]),
                                  html.Tr([html.Td('Renting'), html.Td(
                                      '14.0'), html.Td('16488.0')]),
                                  html.Tr([html.Td('Subscription'), html.Td(
                                      '11.0'), html.Td('13188.0')]),
                                  html.Tr([html.Td('Usage fees'), html.Td(
                                      '10.0'), html.Td('11856.0')])
                              ])
                          ])
])


@app.callback(
    [Output('number-display1', 'children'),
     Output('number-display', 'children')],
    Input('update-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_number(n_clicks):
    output1 = 14
    output2 = 12
    aa = [14, 12]
    return output1, output2


# test
def update_number(n_clicks):
    # Обновляем число в центре круга
    number = income_archive()

    # Обновляем данные таблицы
    table_data = [
        ['Advertising', '2.0', '2844.0'],
        ['Asset sale', '0.0', '26.0'],
        ['Licensing', '62.0', '72768.0'],
        ['Renting', '14.0', '16488.0'],
        ['Subscription', '11.0', '13188.0'],
        ['Usage fees', '10.0', '11856.0']
    ]

    table_rows = [html.Tr([html.Td(cell) for cell in row])
                  for row in table_data]
    table = html.Table(
        [html.Tr([html.Th('Category'), html.Th('Value'), html.Th('Count')])] + table_rows)

    return number, table


# Запускаем сервер
if __name__ == '__main__':
    app.run_server(debug=True)
