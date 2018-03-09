import dash
import dash_core_components as dcc
import dash_html_components as html

class DataView():
    def dataview(self,loc):
        import pandas as import pdb; pdb.set_trace()
        df = pd.readcsv('media/'+area+'.csv')

    def generate_table(dataframe,max_rows=10):
        return html.Table(
        [html.Tr([
        html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe),max_rows))]
        )

    app = dash.Dash()

    app.layout = html.Div(children = [
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
    ])

if __name__=='__main__':
    app.run_server(debug=True)
