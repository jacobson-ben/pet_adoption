"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email


class AddPet(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name")
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Link to Photo")
    age = SelectField("Age", choices=[('baby', 'baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])
    notes = StringField("Notes")
