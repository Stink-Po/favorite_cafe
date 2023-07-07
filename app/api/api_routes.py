from app import app
from flask import render_template, jsonify
from flask_login import current_user
from app.methods.get_image import GetPhoto
import json


@app.route('/api/documents')
def main_doc():
    photo = GetPhoto(search_object='computer')
    images = photo.final
    header = {
        'api-key': 'Your API key'
    }
    return render_template('api_doc/doc.html',
                           user=current_user,
                           title='Api Documents',
                           images=images,
                           ex1=json.dumps(header))
