import os
from jinja2 import meta


def config_from_env(keys):
    return {key: os.getenv(key) for key in keys if os.getenv(key)}


def get_undeclared_variables(jinja_env, template_filename):
    # get the template source and just parse it without substitution variables
    template_source = jinja_env.loader.get_source(jinja_env, template_filename)
    parsed_template = jinja_env.parse(template_source)

    # find all undeclared variables
    return list(set(meta.find_undeclared_variables(parsed_template)))
