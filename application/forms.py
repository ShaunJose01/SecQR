from wtforms import StringField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class QRCodedata(FlaskForm):
    data = StringField("Data",validators=[DataRequired(),Length(min = 2, max= 600)])
    submit = SubmitField('Generate QR')