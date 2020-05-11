from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = StringField('Add a comment',validators = [Required()])
    submit = SubmitField('Submit')
    