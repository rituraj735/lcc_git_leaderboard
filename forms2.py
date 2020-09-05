from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import requests
import psycopg2


HOST = "localhost"
PORT = "5432"
USERNAME = 'lcc'
PASSWORD = '12345678'
DATABASE = 'git_session'

db = psycopg2.connect(user=USERNAME, password=PASSWORD,
                      host=HOST, database=DATABASE)


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    team = SelectField('Team Name', choices=[
                       ('team-1', 'team1'), ('team-2', 'team2')])
    github_link = StringField('Github Link', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_github_link(self, github_link):
        print("here\n")
        user_name = github_link.data.split('/')[-1]

        query_url = github_link.data
        print(query_url)

        data = requests.get(query_url)

        if data.status_code != 200:
            raise ValidationError(
                "User not Found on github! Please check the link or contact administrator")

        sql_query = 'SELECT github_name FROM users where github_name=%s'

        user_name = github_link.data.split('/')[-1]

        cursor = db.cursor()
        cursor.execute(sql_query, (user_name,))
        res = cursor.fetchone()
        cursor.close()

        if res is not None:
            raise ValidationError("You are already in the contest!")

    def validate_name(self, name):
        print("here\n")

        sql_query = 'SELECT display_name FROM users where display_name=%s'

        name = name.data.strip()

        cursor = db.cursor()
        cursor.execute(sql_query, (name,))
        res = cursor.fetchone()
        cursor.close()

        if res is not None:
            raise ValidationError("Name already taken!")


class LoginForm(FlaskForm):
    github_link = StringField('Github Link', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_github_link(self, github_link):
        print("here\n")
        user_name = github_link.data.split('/')[-1]

        query_url = github_link.data
        print(query_url)

        data = requests.get(query_url)

        if data.status_code != 200:
            raise ValidationError(
                "User not Found on github! Please check the link or contact administrator")

        sql_query = 'SELECT github_name FROM users where github_name=%s'

        user_name = github_link.data.split('/')[-1]

        cursor = db.cursor()
        cursor.execute(sql_query, (user_name,))
        res = cursor.fetchone()
        cursor.close()

        if res is None:
            raise ValidationError("Please Register!")
