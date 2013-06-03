import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class error404(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('404.html')
      self.response.write(template.render())

app = webapp2.WSGIApplication([('/404', error404),
                              ], 
                              debug=True)
