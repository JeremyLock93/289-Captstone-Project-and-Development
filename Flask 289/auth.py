import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, sessions, url_for
)

from werkzeug.sercurity import check_password_hash, generate_password_hash

from dba import get_db_connection
