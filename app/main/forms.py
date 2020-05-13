from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = StringField('Add a comment',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself...',validators = [Required()])
    submit = SubmitField('Update profile')

class BloggingForm(FlaskForm):
    title = StringField('Post title', validators = [Required()])
    content = TextAreaField('Blog here...', validators = [Required()], render_kw={'class': 'form-control', 'rows': 20})
    submit = SubmitField('Submit')
