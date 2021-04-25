# Kaggle Titanic Flask App
Deployment of a machine learning model trained on Kaggle's Titanic dataset as a Flask app hosted on Heroku.

## *Overview*
Dataset: https://www.kaggle.com/c/titanic

## *Installation*

1. Clone the repository

``` sh
git clone https://github.com/henrylao/kaggle-titanic.git
```

2. Create the virtual environment in project root directory<br>

Windows:

```sh
python -m venv c:\path\to\myenv
```

MacOS/Linux:

```sh
python -m venv path/to/project/myenv
```

3. Activate the virtual environment<br>

Windows:

```sh
path\to\project\myenv\Scripts\activate
```

MacOS/Linux

```sh
source path/to/project/myvenv/activate
```

4. Install package dependencies<br>

Run one of the following:

``` sh
pip install -r requirements.txt
```

``` sh
pip3 install -r requirements.txt
```

## *REST API Server Startup*

1. Ensure installation of dependencies from the installation section and activation of the virtual environment.
2. Navigate to the server directory.

``` sh
cd path/to/project/kaggle-titanic/
```

3. Run the server driver app.py<br>

Windows/Linux

``` sh
python app.py
```

MacOS

``` sh
python3 app.py
```

## *Milestones*
Model API + Data Pipelining:
- [ ] loading data / existing model binaries
- [ ] preprocess data

REST API:

* [ ] Complete creation of REST API endpoint for LGBM model
    * [x] Create POST method for handling a request
    * [ ] Create a method of configuring the model to be loaded (Ex. dzone, oos, etc)
* [ ] Complete migration of model application to be deployed using Docker
* [ ] Complete method for persisting configurations of models deployed
* [ ] Completed refactoring of codebase for OOP
* [ ] Complete testing for operating systems:
    * [ ] Windows 10
    * [ ] Linux
    * [ ] MacOS
* [ ] Refactor server.driver.py to be a controller stored in the server.controller package
  
Website
* [ ] Support for displaying different singular models
* [ ] Comparison of pycaret models vs self-configured
* [ ] Add footer routing to internet accounts + contact info

Documentation
- [ ] Model and data used
- [ ] Website design docs
  
Stretch
- [ ] Add 