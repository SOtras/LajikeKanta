from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class SpeciesForm(FlaskForm):
    name = StringField("Species name")
    done = BooleanField("Done")
  
    class Meta:
        csrf = False