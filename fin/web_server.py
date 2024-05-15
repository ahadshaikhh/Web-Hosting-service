from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import threading
from werkzeug.serving import run_simple
import os
import requests

PORT = 9899

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///websites.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Website model
class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(200), unique=True, nullable=False)
    html = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.domain_name}'

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for registering a new website
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        domain_name = request.form['domain_name']
        html = request.form['html']

        # Create the HTML file for the website
        filename = f'{domain_name}.html'
        try:
            # Save the website to the database
            website = Website(domain_name=domain_name, html=filename)
            db.session.add(website)
            db.session.commit()
        except:
            print('DOMAIN NOT AVAILABLE')
            return render_template('error.html')

        try:
            with open(f'fin/webs/{filename}', 'w') as file:
                file.write(html)
        except:
            print('html file not added')

        # websites = Website.query.all()
        # print(websites)
        return redirect(url_for('register'))
    else:
        websites = Website.query.all()
        return render_template('register.html', web_pages=websites)

@app.route('/admin/error')
def error():
    return 'DOMAIN ALREADY TAKEN'

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return redirect(url_for('admin'))
    else:
        websites = Website.query.all()
        return render_template('admin.html', web_pages=websites)

@app.route('/admin/<path:path>', methods=['POST'])
def delete_page(path):
    web_pages = Website.query.all()
    for website in web_pages:
        if website.domain_name == path:
            web_pages.remove(website)
            os.remove(f'webs/{path}.html')
            break
    return redirect(url_for('home'))

# Define the route for serving static HTML pages
@app.route('/<path:path>', methods=['GET', 'POST'])
def serve_page(path):
    if request.method == 'POST':
        print('POST request done ')
    
    website = Website.query.filter_by(domain_name=f'{path}').first()
    if website is None:
        return f'<h1>Created new website</h1><p>Error 404 <br> Website Content Not Found</p>', 404
    else:
        web_name = str(website) + '.html'
        #print(web_name)
        return send_from_directory('webs/', web_name)
        


if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the server on port 5000 and use threading to handle multiple requests
    thread = threading.Thread(target=run_simple, kwargs={'application': app, 'hostname': 'localhost', 'port': PORT, 'use_reloader': False, 'use_debugger': True})
    thread.start()



