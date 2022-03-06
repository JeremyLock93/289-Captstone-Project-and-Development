""" from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegisterationForm(Form):
    username = StringField('Username', [validatior.Length(min=4, max=30)])
    email = StringField('Email Address', [validators.Length(min=8, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I Accept the TOS', [validators.DataRequired()])
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm(request.form)
    if request.method == 'POST' and form.validat():
        user = User(form.username.data, form.email.data,form. password.data)
        db_session.add(user)
        flash('Thank you for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form) """