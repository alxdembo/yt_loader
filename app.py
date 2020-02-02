from pytimeparse.timeparse import timeparse
from flask import Flask, jsonify, request

from slicer.slicer import Slicer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings_local.py')


@app.route('/slicer/api/v1.0/slice/<string:source>/<string:video_id>', methods=['GET'])
def get_slice(source, video_id):
    start = request.args.get("start")
    end = request.args.get("end")
    rerender = "true" == request.args.get("rerender", "true")

    try:
        slicer = Slicer(source, video_id, timeparse(start), timeparse(end), rerender)
        url = slicer.get_url()

    except ValueError as e:
        return jsonify({'error': str(e)}), 422

    return jsonify({'url': url})


if __name__ == '__main__':
    app.run()
