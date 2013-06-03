import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

# For Udacity blog
from google.appengine.ext import db

import jinja2
import webapp2

PROJECT_DIR = os.path.dirname(__file__);

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(PROJECT_DIR),
    extensions=['jinja2.ext.autoescape'])


# Following Udacity handler stuff for templating
class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
      self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
      t = JINJA_ENVIRONMENT.get_template(template)
      return t.render(params)

  def render(self, template, **kw):
      self.write(self.render_str(template, **kw))



# Misc....
class index(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('index.html')
      self.response.write(template.render())

class banana(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('banana.html')
      self.response.write(template.render())

class about(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('about.html')
      self.response.write(template.render())

class resume(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('resume.html')
      self.response.write(template.render())

class contact(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('contact.html')
      self.response.write(template.render())

class error404(webapp2.RequestHandler):
  def get(self):
      template = JINJA_ENVIRONMENT.get_template('404.html')
      self.response.write(template.render())


# ------ Udacity HW3: Basic blog -------- #

class blogPostingDB(db.Model):
  # Datastore stuff
  subject = db.StringProperty(required = True)
  content = db.TextProperty(required = True)
  created = db.DateTimeProperty(auto_now_add = True) # Just a time stamp
 

class blog(Handler):
  # Blog front page
  def get(self):
      # Query all blog posts in database
      blogPosts = db.GqlQuery("SELECT * FROM blogPostingDB ORDER BY created DESC ")
      self.render('blog.html', blogPosts = blogPosts)


class newpost(Handler):
  # Interface to make new blog posts
  def render_newpost(self, subject="", content="", error=""):
      self.render('newpost.html', subject=subject, content=content, error=error)

  def get(self):
      self.render_newpost()

  def post(self):
      subject = self.request.get("subject")
      content = self.request.get("content")

      if subject and content:
        # Successful post
        bp = blogPostingDB(subject = subject, content = content)
        bp_key = bp.put() # Store data in database
        # Redirect to blog posting
        self.redirect('/blog/%d' % bp_key.id()) 
      else:
        # Error handling
        error = "Need both a subject and content"
        self.render_newpost(subject, content, error)


class permalink(blog):
  # for handling permalink to new blog posting
  def get(self, blog_id):
      s = blogPostingDB.get_by_id(int(blog_id))
      self.render("blog.html", blogPosts=[s])


# App definition stuff
app = webapp2.WSGIApplication([('/',        index),
                               ('/blog',    blog),
                               ('/blog/newpost', newpost),
                               ('/blog/(\d+)',   permalink),
                               ('/index',   index),
                               ('/home',    index),
                               ('/banana',  banana),
                               ('/about',   about),
                               ('/resume',  resume),
                               ('/contact', contact),
                               ('/404',     error404)
                              ], 
                              debug=True)

