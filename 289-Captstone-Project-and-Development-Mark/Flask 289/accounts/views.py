from flask import(
    Blueprint, 
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)

from flask_rq import get_queue

from app import db
from app.account.forms import (
    ChangeEmailForm,
    ChangePasswordForm,
    CreatePasswordForm,
    LoginForm,
    RegistrationForm,
    RequestResetPasswordForm,
    ResetPasswordForm,
)

from app.email import send_email
from app.models import user

account = Blueprint('account', __name__)

@account.route('/login', methods= ['GET', 'POST'])
def login():
    '''Log in for existing users if they exist in the database'''
    form = LoginForm()
    if form.validate_on_submit():
        user = user.querey.filter_by(email=form.email.data).first()
        if user is not None and user.check_password_hash is not None and \
                user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash('You are logged in.')
            return redirect(request.args.get('next') or url_for('main.index'))
    else:
        flash('Invalid email or password.', 'error')
    return render_template('account/login.html', form=form)

@account.route('/register', methods=['GET', 'POST'])
def register():
    '''Registers a new user, and sends a confirmation email'''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = user(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            password = form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_toke()
        confirm_link = url_for('accoutn.confirm', token=token, _external=True)
        get_queue().enqueue(
            send_email,
            recipient=user.email,
            subject='Confirm Your Account',
            template='account/email/confirm',
            user=user,
            confirm_link=confirm_link)
        flash('A confirmation link has been sent to {}.'.format(user.email),
              'warning')
        return redirect(url_for('main.index'))
    return render_template('account/register.html', form=form)

@account.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.', 'info')
    return redirect(url_for('main.index'))

@account.route('/manage', methods = ['GET', 'POST'])
@account.route('/mangage/info', methods=['GET', 'POST'])
@login_required
def manage():
    '''Displays the user's account information to be managedd'''
    return render_template('account/manage.html', user=current_user, form=None)


@account.route('/reset-password', methods=('GET', 'POST'))
def reset_password_request():
    '''Responding to an existing user's request for a password reset'''
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_password_reeset_token()
            reset_link = url_for(
                'account.resest_password', token=token, _external=True)
            get_queue().enqueue(
                send_email,
                recipient=user.email,
                subject= 'Password Reset Request',
                template='account/email/reset_password',
                user=user,
                reset_link=reset_link,
                next=request.args.get('next'))
        flash('A password reset link has ben sent to {}.'.format(
            form.email.data), 'warning')
        return redirect(url_for('account.login'))
    return render_template('account/reset_password.html', form=form)

@account.rout('reset-password/<token>', methods=['GET', 'POST'])
def resest_password(token):
    '''Allows for an existing user to reset their password'''
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = user.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Invalid email address.', 'form-error')
            return redirect(url_for('mainx.index'))
        if user.resest_password(token, form.new_password.data):
            flash('You have successful changed your password', 'form-success')
        else:
            flash('The password reset link has expired or is invalid.', 'form-error')
    return render_template('account/reset_password.html', form=form)

@account.route('/manage/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    '''This allows for the user to change password on the account manage page'''
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your Password has been successfully updated.', 'form-success')
            return redirect(url_for('main.index'))
        else:
         flash('Original password is invalid', 'form-error')
    return render_template('account/manage.html', form=form)

@account.route('/manage/change-email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    '''Responding to the user's request for changing/updating their email'''      
    form = ChangeEmailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            token = curren_user.generate_mail_change_token(new_email)
            change_email_link = url_for(
                'account.change_email', token=token, _external=True)
            get_queue().enqueue(
                send_email,
                recipient=new_email,
                subject='Confirm Your New Email',
                template='account/email/change_email',
                #current_user is a proxy that we want the underlying
                #user object
                user=current_user._get_current_object(),
                change_email_link= change_email_link)
            flash('A confirmation link has been sent to {}.' .format(new_email),
                  'warning')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.', 'form-error')
            
@account.route('/manage/change-email/<token>', methods=['GET', 'POST'])
@login_required
def change_email(token):
    '''The token required for changing an exist user's email'''
    if current_user.change_email(token):
        flash('Your Email has been Successfully updated.', 'success')
    else:
        flash('The confirmation link has expired or is invalid', 'error')
    return redirect(url_for('main.index'))

@account.route('confirm-account')
@login_required
def confirm_request():
    '''Responds to a new user's request to confirm their account.'''
    token = current_user.generate_mail_change_token()
    confirm_link = url_for('account.confirm', token=token, _external=True)
    get_queue().enqueue(
        send_email,
        recipient=current_user.email,
        subject='Confirm Your Account',
        template='account/email/confirm',
        user=current_user._get_current_object(),
        confirm_link=confirm_link)
    flash('A new confirmation link has been sent to {}.'.format(
        current_user.email), 'warning')
    return redirect(url_for('main.index'))
    
@account.before_app_request
def before_request():
    """Forcea user to confirm email before accessing login-required routes."""
    if current_user.is_authenticated \
            and not current_user.confirmed \
            and request.endpoint[:8] != 'account.' \
            and request.endpoint != 'static':
        return redirect(url_for('account.unconfirmed'))
        