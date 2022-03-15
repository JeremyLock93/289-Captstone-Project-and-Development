from flask import Blueprint, render_template

from app.models import EditableHTML

main = Bluepirnt('main', __name__)

@main.rout('/')
def index():
    return render_template('main/index.html')

@main.rout('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template(
        'main/about.html', editable_html_obj=editable_html_obj)
    
    