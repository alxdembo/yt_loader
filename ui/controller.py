from flask import Blueprint, render_template, url_for
from forms import SlicerForm

ui_module = Blueprint('ui', __name__)


@ui_module.route('/', methods=['GET', 'POST'], endpoint='home')
def web_ui():
    form = SlicerForm()
    return render_template('slicer-ui.html', form=form)
