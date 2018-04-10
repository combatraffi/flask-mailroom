import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation 
totaldonation = 0
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/<string:dname>/') 
def donationsfordonor(dname):
    donations = Donation.select()
    return render_template('individualdon.jinja2', dname=dname, donations=donations)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port, debug = True)

