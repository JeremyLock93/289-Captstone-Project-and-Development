import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for


from werkzeug.security import check_password_hash, generate_password_hash

from dba import get_db_connection

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET','POST'))
def register():
    '''Main handler of the registeration function using the methods GET and POST to create new
    New user names and passwords and adding them to the database.'''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db_connection()
        error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    if error is None:
        try:
            db.execute(
                "INSERT INTO user (username, password) VALUES (?,?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except db.InterityError:
            error = f"User {username} is already registered."
        else:
            return redirect(url_for("auth.login"))

        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db_connection()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username =?', (username,)
        ).fetchone()

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user['id']
        return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db_connection().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    return wrapped_view 