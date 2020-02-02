from flask import Blueprint, jsonify, request
from pytimeparse.timeparse import timeparse
from api.slicer import Slicer

api_module = Blueprint('api', __name__)


@api_module.route('/v1.0/slice/<string:source>', methods=['GET'], endpoint='api_v1_slicer')
def get_slice(source):
    video_id = request.args.get("video_id")
    start = request.args.get("start")
    end = request.args.get("end")
    rerender = "true" == request.args.get("rerender", "true")

    try:
        slicer = Slicer(source, video_id, timeparse(start), timeparse(end), rerender)
        url = slicer.get_url()

    except ValueError as e:
        return jsonify({'error_message': str(e)}), 422

    except Exception as e:
        return jsonify({'error_message': str(e)}), 500

    return jsonify({'url': url})
