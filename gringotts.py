from flask import Flask, session

app = Flask(__name__)

app.config.from_object('config')

print 'Flask app "%s" initialized' % __name__

import views