"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db 
from flask import render_template, request, redirect, url_for, flash
from forms import AddProfileForm 
from models import UserProfile
from werkzeug.utils import secure_filename

###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Akeam Williams")
    
@app.route('/profile', methods=['POST','GET'])
def profile():
    """Render the website's Add Profile page."""
    form=AddProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        fname = form.firstname.data
        lname = form.lastname.data
        username= fname+","+lname
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        bio=form.bio.data
        photo=form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        photo=photo.filename
        
        user = UserProfile.query.filter_by(username=username).first()
        if user is None :
            user=UserProfile(first_name=fname,last_name=lname, gender=gender, location=location, email=email, bio=bio, photo=photo)
            db.session.add(user)
            db.session.commit()
            flash('Profile was successfully added.', 'success')
            return redirect(url_for('profile'))
        elif user is not None:
            flash("already a member", 'danger')

    flash_errors(form)
    return render_template('profile.html',form=form)

@app.route('/profiles')
def profiles():
    """Render the website Profiles page"""
    return render_template('profiles.html')

@app.route('/secure-page')
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


###
# The functions below should be applicable to all Flask apps.
###

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


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
