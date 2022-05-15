from email.mime import image
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Campo Obbligatorio!")])
    password = PasswordField('Password', validators=[DataRequired("Campo Obbligatorio!")])
    remember_me = BooleanField('Ricordami')
    submit = SubmitField('Login')

class SubscribeForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Campo Obbligatorio!")])
    password = PasswordField('Password', validators=[DataRequired("Campo Obbligatorio!")])
    email = StringField('Email - Facoltativa')
    role = StringField('Ruolo')
    submit = SubmitField('Effettua l\'iscrizione')

class PostForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired("Campo Obbligatorio!"), Length(min=3, max=120, message="Il titolo deve contenere tra i 3 e i 120 caratteri!")])
    description = TextAreaField('Descrizione', validators=[Length(max=300, message="Massimo 300 caratteri!")])
    body = TextAreaField('Contenuto', validators=[DataRequired("Campo Obbligatorio!")])
    body2 = TextAreaField('Contenuto #2')
    body3 = TextAreaField('Contenuto #3')
    body4 = TextAreaField('Contenuto #4')
    body5 = TextAreaField('Contenuto #5')
    cit = TextAreaField('Testimonianza')
    cit2 = TextAreaField('Testimonianza #2')
    cit3 = TextAreaField('Testimonianza #3')
    cover = FileField('Copertina Articolo', validators=[FileAllowed(['jpg', 'jpeg', 'png']), ])
    submit = SubmitField('Pubblica')

class FolderForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired("Campo Obbligatorio!"), Length(min=3, max=120, message="Il titolo deve contenere tra i 3 e i 120 caratteri!")])
    description = TextAreaField('Descrizione', validators=[Length(max=300, message="Massimo 300 caratteri!")])
    cover = FileField('Copertina Articolo', validators=[FileAllowed(['jpg', 'jpeg', 'png']), ])
    media = FileField('Materiale', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'mp4', 'mkv', 'avi']), ])
    submit = SubmitField('Pubblica')

class CitaForm(FlaskForm):
    body = TextAreaField('Frase', validators=[DataRequired("Campo Obbligatorio!")])
    submit = SubmitField('Pubblica')