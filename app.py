# -*- coding: utf-8 -*-
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import dash
import base64

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ], title='Ner')

server = app.server


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


app.layout = dbc.Container([

    dbc.Row(
        [
            html.Div([html.P(['NER Text Summerizer and Token Analysis'], id='ner',
                             style={'marginBottom': 15, 'marginTop': 15, 'font-family': 'cursive',
                                    'text-align': 'center', 'color': '#00FFFF',
                                    'fontSize': 20})]),
            html.Br(),
            html.Br(),
            html.Div([
                dbc.Label("Paste your Short story here!",
                          style={'marginBottom': 15, 'marginTop': 15, 'font-family': 'cursive', 'text-align': 'center',
                                 'color': '#00FFFF',
                                 'fontSize': 20}),
                dcc.Textarea(
                    id='textarea',
                    placeholder="Paste your Short story here!",
                    style={'width': '100%', 'height': 200, 'marginBottom': 15,
                           'marginTop': 15, 'color': 'black',
                           'textAlign': 'center', 'font-family': 'cursive', 'fontSize': 14},
                ),
                html.Br(),
                html.Div(id='tex', style={'whiteSpace': 'pre-line'}),
                dbc.Label("View the Entities discovered by the model!",
                          style={'marginBottom': 15, 'marginTop': 15, 'font-family': 'cursive', 'text-align': 'center',
                                 'color': '#00FFFF',
                                 'fontSize': 20}),
                dcc.Textarea(
                    id='textarea1',
                    placeholder="The analysed story!",
                    style={'width': '100%', 'height': 200, 'marginBottom': 15,
                           'marginTop': 15, 'color': 'black',
                           'textAlign': 'center', 'font-family': 'cursive', 'fontSize': 14},
                ),
                html.Div(id='tx', style={'whiteSpace': 'pre-line'}),
            ], style={'marginBottom': 15, 'marginTop': 15, 'color': '#00FFFF', 'fontSize': 14})
        ]),

    html.Button('Analyse Story', id='submitTextarea', n_clicks=0,
                style={'marginBottom': 15, 'marginTop': 15, 'fontSize': 14}),

    dbc.Row([
        dbc.Col([
            dbc.Label("Summerized Story",
                      style={'marginBottom': 15, 'color': '#800040', 'marginTop': 15, 'fontSize': 16}),
            html.Div(id='summary'),
            html.Br(),
            html.Br(),
            dbc.Label("Headline",
                      style={'marginBottom': 15, 'color': '#800040', 'marginTop': 15, 'fontSize': 16}),
            html.Marquee(id='headline'),
        ], style={'width': '100%', 'height': 200, 'marginBottom': 15,
                  'marginTop': 15, 'color': '#00FFFF',
                  'textAlign': 'center', 'font-family': 'cursive', 'fontSize': 14}, ),

        dbc.Col([
            dbc.Label("Word Cloud",
                      style={'marginBottom': 15, 'color': '#800040', 'marginTop': 15, 'fontSize': 16}),
            dbc.CardImg(id='wordcloud', top=True),
        ], style={'width': '100%', 'height': 200, 'marginBottom': 15,
                  'marginTop': 15, 'color': '#00FFFF',
                  'textAlign': 'center', 'font-family': 'cursive', 'fontSize': 14}, ),
    ]),

    html.Br(),

], style={'backgroundColor': 'F0E68C', 'marginTop': '20px', 'font-family': 'cursive', 'marginBottom': '40px',
          'border': '2px', 'color': 'cyan'})


@app.callback(Output('textarea1', 'value'),
              Output('wordcloud', 'src'),
              Output('summary', 'children'),
              Output('headline', 'children'),
              State('textarea', 'value'),
              Input('submitTextarea', 'n_clicks'), prevent_initial_call=True)
def update_output(state, n_clicks, ):
    if n_clicks:

        # summerizer!

        import requests

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        def summerizer(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        summerizedText = summerizer(state)[0]["summary_text"]

        # Headline Generator!

        API_URL2 = "https://api-inference.huggingface.co/models/JulesBelveze/t5-small-headline-generator"
        headers2 = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL2, headers=headers2, json=payload)
            return response.json()

        headline = query(summerizedText)[0]["summary_text"]

        # Ner Model

        import spacy
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud, STOPWORDS

        stopwords = set(STOPWORDS)
        stopwords.add("said")

        wc = WordCloud(background_color="white", max_words=2000,
                       stopwords=stopwords, contour_width=3, contour_color='steelblue')

        # Generate a word cloud image
        wordcloud = wc.generate(state)

        # Display the generated image:
        # the matplotlib way:
        import matplotlib.pyplot as plt

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("on")
        plt.savefig("test.jpeg")
        wordCloud = b64_image("test.jpeg")

        # Loading the Spacy model
        model_best = "./model-best/"
        nlp = spacy.load(model_best)

        # Process the text
        doc = nlp(state)

        new_dic = []
        for i in range(1, len(doc)):
            for ent in doc.ents:
                entity = f"{ent.text} = {ent.label_}"
                new_dic.append(entity)
            return f"\nThere are {len(new_dic)} Entities. \n\n {new_dic}", wordCloud, summerizedText, headline


if __name__ == "__main__":
    app.run_server(debug=True)
