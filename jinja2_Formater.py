import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
template = jinja_env.get_template('MATH6303_Warmup_2_1_Part_1.html')

print(template.render())