from config import jinja_env

def render_template(template_name, **context):
    template = jinja_env.get_template(template_name)
    return template.render(context)