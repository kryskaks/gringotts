# -*- coding: utf8 -*-
from datetime import datetime
from flask import render_template, request, redirect, url_for, jsonify, session, flash, make_response
from gringotts import app

@app.route("/hello")
def hello():	
	return "{0:%d-%m-%Y %H:%M:%S} => Hello, world!".format(datetime.now())

@app.route("/pay")
def pay():
	return render_template("pay.html")

@app.route("/test")
def test():
	return render_template("test.html")