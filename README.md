### Enrique Tolentino python interview

This is a little project builded with python, using flask.
I'm happy to share my work with you.

#### For download and install the project
You need clone the repository

``git clone https://github.com/enriquetolentinog/python-interview.git``

Then you need install the pip dependencies *(I recommend use venv)*, typing in a console placed in project folder:

``pip install -r requirements.txt``

If you are using venv, needs be activate previously.


#### For run the project
Just type in a console placed in project folder:

``python app.py``

and that's all. Now the project is running in http://127.0.0.1:5000

If you have issues with port 5000, you can change that in app.py file: ``app.run(debug=True, port=YOUR_PORT_WITHOUT_ISSUES)``

#### For use the project
I include 3 json files in testdata folder, and you can use for test the endpoints.

Additionally, I include a postman collection json. You can import the collection, but you needs to have postman software installed.
