from flask import Flask, jsonify, request
from googletrans import Translator
from urllib.parse import unquote

# app
app = Flask(__name__)

# routes
@app.route('/',methods = ['POST'])

def summarizer():
    translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

    token = request.args.get('token')
    encoded_input_text = request.args.get('text')
    text_dest = request.args.get('dest')

    if token == 'c0ncret10':
        uncoded_input_text = unquote(encoded_input_text)

        clean_input_text = uncoded_input_text.strip('\n')

        input_text_list = clean_input_text.split('#')

        translations = translator.translate(input_text_list, dest=text_dest)

        output_text = ''

        for translation in translations:
            output_text = output_text + translation.text + '$'
        
        return output_text
    else:
        return 'Please Enter the correct Token'


if __name__ == '__main__':
    app.run()
