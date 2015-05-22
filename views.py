# -*- coding: utf8 -*-
from datetime import datetime

from flask import render_template, request, redirect, url_for, jsonify, session, flash, make_response
import requests

from gringotts import app

@app.route("/hello")
def hello():	
	return "{0:%d-%m-%Y %H:%M:%S} => Hello, world!".format(datetime.now())

@app.route("/pay")
@app.route("/pay/<action>")
def pay(action=None):
	if not action:
		return render_template("pay.html", form_action=None, form_data=None, form_method=None)
	
	# get form from mgeller
	request = "http://localhost:5005/invoice?partner_invoice_id=10&amount=560&extra=some_data&payway_id=1&partner_id=1&sign=secret"
	response = requests.get(request)

	json_response = response.json()

	response_data = json_response["data"]
	
	print response_data

	if response_data:
		print response_data["invoice_id"], "created"
		return render_template("pay.html", form_data=response_data["data"], form_method=response_data["method"], form_action=response_data["source"])
	
	flash("Unable to get iframe data: %s" % json_response["message"])
	return render_template("pay.html", form_action=None, form_data=None, form_method=None)


@app.route("/test")
def test():
	return render_template("test.html")