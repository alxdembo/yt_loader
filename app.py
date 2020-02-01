from flask import Flask, request

app = Flask(__name__)


@app.route('/slicer/api/v1.0/slice/<str:source>', methods=['GET'])
def get_slice(source):

    slice_start = request.args.get('video_id')
    slice_start = request.args.get('start')
    slice_start = request.args.get('end')

    return


if __name__ == '__main__':
    app.run(debug=True)
    app.config.from_pyfile('settings.py')
