from wtforms import StringField, SelectField
from wtforms.validators import InputRequired
from flask_wtf import Form


class SlicerForm(Form):
    video_id = StringField(default='d3D7Y_ycSms', validators=[InputRequired()])
    start = StringField(default='00:00:00', validators=[InputRequired()])
    end = StringField(default='00:00:01', validators=[InputRequired()])
    source = SelectField(choices=[('youtube', 'YouTube'), ('ooyala', 'Ooyala')])
