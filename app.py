from flask import Flask, jsonify

from slicer.slicer import Slicer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings_local.py')


@app.route('/slicer/api/v1.0/slice/<string:source>/<string:video_id>/<int:start>/<int:end>', methods=['GET'])
def get_slice(source, video_id, start, end):
    slicer = Slicer(source, video_id, start, end)

    return jsonify({'url': slicer.get_url()})


if __name__ == '__main__':
    app.run()
