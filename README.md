# Laundrowat?? - MHacks 12

This web app is built on Python's Flask framework with Bootstrap, using a [Flask Boilerplate](https://github.com/realpython/flask-boilerplate).  It uses Google Cloud Platform's AutoML Vision API to train and deploy a custom model on laundry symbols.

To use (use `pip` on Windows/Linux, and `pip3` for macOS):
```bash
$ git clone https://github.com/Liew211/laundrowat.git
$ cd laundrowat
$ pip install virtualenv
$ virtualenv env
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flask run 
```
The Flask app runs on port 5000 by default, so go to [http://localhost:5000/](http://localhost:5000/)
