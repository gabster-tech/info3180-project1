"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app,db
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm
from .models import Property
from werkzeug.utils import secure_filename
import os

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create',methods=['POST', 'GET'])
def create():
    propertyForm = PropertyForm()
    if propertyForm.validate_on_submit():
        title = propertyForm.title.data
        num_of_bedrooms = propertyForm.num_of_bedrooms.data
        num_of_bathrooms = propertyForm.num_of_bathrooms.data
        location = propertyForm.location.data
        price = propertyForm.price.data
        type = propertyForm.type.data
        description = propertyForm.description.data
        photo = propertyForm.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        property = Property(title,num_of_bedrooms,num_of_bathrooms,location,price,type,photo,description)
        db.session.add(property)
        db.session.commit()
        flash("Property was successfully added")
        return redirect(url_for('properties'))

    return render_template('create.html')

@app.route('/properties')
def properties():
    properties = db.session.execute(db.select(Property)).scalars()
    return render_template('properties.html',properties=properties)

@app.route('/properties/<propertyid>')
def view_properties(propertyid):
    propertyid = int(propertyid)
    prop=db.session.execute(db.select(Property).filter_by(id=propertyid)).scalar_one()
    return render_template('view_properties.html', prop=prop)



###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
