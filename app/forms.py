import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PassengerForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class PassengerForm(FlaskForm):
    prediction = None
    # select fields options
    genders = ["Male", "Female"]
    titles = ["Decline to state", "Mr", "Mrs", "Ms", "Doctor", "Military", "Noble", "Clergy", "Master"]
    locations = ["Cherbourg", "Queenstown", "Southampton"]

    passenger_classes = [1, 2, 3]
    # text fields
    first_name = TextField("First Name")
    last_name = TextField("Last Name")
    sibsp = TextField("Siblings and Spouses")
    parch = TextField("Parents and Children")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    age = TextField("Age")
    # select fields
    gender = SelectField("Gender", choices=genders)
    embarked = SelectField("Location of Departure", choices=locations)
    title = SelectField("Title", choices=titles)
    pClass = SelectField("Class", choices=passenger_classes)

    min, max = 0, 500
    fare = wtforms.DecimalField("Fare", [wtforms.validators.NumberRange(min=min, max=max)])
    submit = SubmitField("Submit")
    reset = SubmitField("Reset")
