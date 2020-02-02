from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from api.controller import api_module
from forms import SlicerForm
from flask_jsglue import JSGlue

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings_local.py')

Bootstrap(app)
jsglue = JSGlue(app)

app.register_blueprint(api_module, url_prefix='/api')


@app.route('/', methods=['GET', 'POST'], endpoint='home')
def web_ui():
    form = SlicerForm()
    return render_template('slicer-ui.html', form=form)


if __name__ == '__main__':
    app.run()
