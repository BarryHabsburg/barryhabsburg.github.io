import jinja2
import os

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))

jinja_var = {
    'title': 'this is a test content page'
}

template = jinja_env.get_template('MATH6391_Warmup_1_2.html')
print(template.render(jinja_var))