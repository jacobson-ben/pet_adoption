"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPet(FlaskForm): 
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Link to Photo", validators=[URL(), Optional()])
    age = SelectField("Age", choices=[('baby', 'baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')], validators=[InputRequired()])
    notes = StringField("Notes", validators=[InputRequired()])

class EditPet(FlaskForm):
    """Form for adding pets."""
    photo_url = StringField("Link to Photo", validators=[URL(), Optional()])
    notes = StringField("Notes", validators=[InputRequired()])
    available = BooleanField("available")