from flask import Flask
from flask_bootstrap import Bootstrap
from api.controller import api_module
from ui.controller import ui_module
from flask_jsglue import JSGlue

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_pyfile('settings_local.py')

Bootstrap(app)
jsglue = JSGlue(app)

app.register_blueprint(ui_module)
app.register_blueprint(api_module, url_prefix='/api')

if __name__ == '__main__':
    app.run()
