from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    shop = StringField('Shop name', validators=[DataRequired()])
    location = StringField("Shop Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    cost_rating = SelectField("Cost rating", choices=["💵", "💵💵", "💵💵💵", "💵💵💵💵", "💵💵💵💵💵"], validators=[DataRequired()])
    speed_rating = SelectField("Speed Rating", choices=["💨", "💨💨", "💨💨💨", "💨💨💨💨", "💨💨💨💨💨"], validators=[DataRequired()])
    service_rating = SelectField("Customer Service Rating", choices=["👍", "👍👍", "👍👍👍", "👍👍👍👍", "👍👍👍👍👍"], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_shop():
    form = CafeForm()
    if form.validate_on_submit():
        with open("data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.shop.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.cost_rating.data},"
                           f"{form.speed_rating.data},"
                           f"{form.service_rating.data}")
        return redirect(url_for('shops'))
    return render_template('add.html', form=form)


@app.route('/shops')
def shops():
    with open('data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('shops.html', shops=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
