import os

import yaml
from jinja2 import Environment, FileSystemLoader, meta
from riddles_util.invariant import invariant
from src.steps.docker import docker_build, create_image_uri, docker_tag, docker_session, get_short_image_id

# Step 0: A dirty working tree is not allowed except when force building
from src.steps.git import is_working_tree_dirty
from src.steps.helpers import get_step_output
from src.tasks.build_microservice import tag_invariant, get_version_uri
from src.tasks.helpers import (
    get_image_repository_google_keys_path,
    get_image_repository_project_id,
    does_file_exist)


def config_from_env(keys):
    return {key: os.getenv(key) for key in keys if os.getenv(key)}


def build_context():
    possible_conf_dirs = ['.', '..']
    absolute_possible_conf_dirs = [os.path.abspath(x) for x in possible_conf_dirs]
    for config_dir in absolute_possible_conf_dirs:
        jarvis_config_path = "{}/.jarvis.yaml".format(config_dir)
        if os.path.isfile(jarvis_config_path):
            config = load_project_configuration(jarvis_config_path)

            return {
                'root_working_dir': config_dir,
                'cwd': os.getcwd(),
                'configuration': config
            }

    invariant(False, 'Jarvis could not load a configuration file. Please assert '
                     'that ".jarvis.yaml" is present in "{}" or its parent directory.'
                     ''.format(os.getcwd()))


def load_project_configuration(config_path):
    jinja_env = Environment(
        loader=FileSystemLoader(['.'])
    )
    config_path_basename = os.path.basename(config_path)
    variable_keys = get_undeclared_variables(jinja_env, config_path_basename)

    # foreach var lookup in env, gather undefined vars
    env_config = config_from_env(variable_keys)

    # if there are undefined vars, raise error and print that list
    diff = set(variable_keys) - set(env_config.keys())
    if diff:
        raise RuntimeError("You need to define the environment variables: {}".format(diff))

    template = jinja_env.get_template(config_path_basename)
    rendered_config = template.render(**env_config)

    return yaml.load(rendered_config)


def build_image(image_name, project_id, google_keys_path):
    with docker_session(google_keys_path):
        build_result = docker_build(dockerfile_path=get_dockerfile_path(image_name))
    invariant(build_result.returncode == 0, "build failed:\n{}".format(build_result.stderr.strip()))
    digest = get_step_output(build_result)
    short_image_id = get_short_image_id(digest=digest)
    print('Built {}, Image ID: {}'.format(image_name, short_image_id))

    # Step 2: Construct a versioned image uri
    version_uri = get_version_uri(project_id, short_image_id, image_name, False)

    # Step 3: Tag the image that was just built with the versioned tag
    tag_result = docker_tag(image_id=short_image_id, tag=version_uri)
    tag_invariant(tag_result, image_name, short_image_id, version_uri)

    return short_image_id


def build_sandbox_containers():
    working_tree_is_dirty = is_working_tree_dirty()
    invariant(not working_tree_is_dirty, 'Build canceled: dirty working tree')

    context = build_context()

    google_keys_path = get_image_repository_google_keys_path(context)
    project_id = get_image_repository_project_id(context)

    for sandbox_image_name in os.listdir(os.path.join(os.getcwd(), 'images')):
        short_image_id = build_image(sandbox_image_name, project_id, google_keys_path)

        latest_uri = create_image_uri(namespace=project_id, container=sandbox_image_name, tag='latest')
        latest_tag_result = docker_tag(image_id=short_image_id,
                                       tag=latest_uri)

        tag_invariant(latest_tag_result, sandbox_image_name, short_image_id, latest_uri)


def get_dockerfile_path(image_name):
    dockerfile_path = 'images/{}/Dockerfile'.format(image_name)
    invariant(does_file_exist(dockerfile_path), '{} does not exist or is empty'.format(dockerfile_path))
    return dockerfile_path


def get_undeclared_variables(jinja_env, template_filename):
    # get the template source and just parse it without substitution variables
    template_source = jinja_env.loader.get_source(jinja_env, template_filename)
    parsed_template = jinja_env.parse(template_source)

    # find all undeclared variables
    return list(set(meta.find_undeclared_variables(parsed_template)))


if __name__ == '__main__':
    build_sandbox_containers()
