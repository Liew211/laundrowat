# Laundrowat?? - MHacks 12

This web app is built on Python's Flask framework with Bootstrap, using a [Flask Boilerplate](https://github.com/realpython/flask-boilerplate).  It uses Google Cloud Platform's AutoML Vision API to train and deploy a custom model on laundry symbols.

To use (use `pip` on Windows/Linux, and `pip3` for macOS):

1. Clone the repo
```bash
$ git clone https://github.com/Liew211/laundrowat.git
$ cd laundrowat
```

2. Install and activate a virtualenv
```
$ pip install virtualenv
$ virtualenv env
$ source env/bin/activate
```

3. Install dependencies
```
$ pip install -r requirements.txt
```
4. Run the Flask app:
```bash
$ flask run 
```
OR
```bash
$ python app.py
```
(use `python3` on macOS)

The Flask app runs on port 5000 by default, so go to http://localhost:5000/ to view the app.
