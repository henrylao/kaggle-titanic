from flask import Flask, redirect, render_template, request

import pandas as pd

# from titanic_model import deploy_model
from forms import PassengerForm

app = Flask(__name__)
app.secret_key = 'dev fao football app'
prediction = 1.2


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET'])
def index():
    # return redirect("/input")
    return render_template('old-input.html')


@app.route('/prediction', methods=['GET'])
def prediction():
    df = process_inputs()
    # proba = deploy_model(df)

    # return "Probability of survival is: {0:.2f}%".format(100 * proba[0, 1])
    return "Probability of survival is: {0:.2f}%".format(100.2)


@app.route('/input', methods=["GET", "POST"])
def get_passenger():
    global prediction
    # prediction = None
    form = PassengerForm()
    try:
        print("Loading submissions")
        df_submissions = pd.read_csv("submissions.csv")
    except Exception as e:
        print("No submissions.csv found... creating new submissions.csv")
        print("Error:", e)
        df_submissions = pd.DataFrame({
            k: [] for k in [_ for _ in request.form.to_dict().keys() if _ != "submit"]
        })
    # here, if the request type is a POST we get the data on contat
    # forms and save them else we return the contact forms html page
    if request.method == 'POST':
        # print("Reset:", type(request.form['reset']))
        # if request.form['reset']:
        #     return redirect("/input")
        print("POST received")
        data = {k: request.form.to_dict()[k] for k in request.form.to_dict().keys() if k != "submit"}
        print(data)
        print(df_submissions)
        df_submissions = df_submissions.append(data, ignore_index=True)
        df_submissions.to_csv('submissions.csv', index=False)
        print("User submission is saved !")
        prediction = 1.5
        prediction = process_inputs()
        print("Prediction:", prediction)
        return redirect("/input")

        # return render_template('input.html', form=form, prediction=prediction)

    print("GET received")
    return render_template('input.html', form=form, prediction=prediction)


def process_inputs():
    """
    Process input data for the model training.
    """
    print("Called to process inputs")
    return 1.5


if __name__ == '__main__':
    app.run(debug=True)
