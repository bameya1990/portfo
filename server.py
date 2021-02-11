from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/index.html')
# def home():
#     return render_template('index.html')

# Using the flask variable to route to the right html file
@app.route('/<page_name>')
def display(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
	        data = request.form.to_dict()
	        write_to_csv(data)
	        return redirect('./thankyou.html')
	    except:
	    	return 'Could not save to database'
    else:
        return 'Something went wrong, Try again!'

# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/works.html')
# def wor():
#     return render_template('works.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/about.html')
# def hello_world():
#     return render_template('about.html')


# @app.route('/about.html')
# def hello_world():
#     return render_template('about.html')


# @app.route('/works.html')
# def hello():
#     return 'These are my thoughts on blogs!!!!'


# @app.route('/blog/2021/me')
# def me():
#     return 'These are my thoughts on me!!!!'
