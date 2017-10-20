import os

from riddles.invariant import invariant
from riddles.jarvis.jarvis import Jarvis
from riddles.jarvis.steps.docker import (
    create_image_uri,
    docker_build,
    docker_session,
    docker_tag,
    get_short_image_id,
)
from riddles.jarvis.steps.git import is_working_tree_dirty
from riddles.jarvis.steps.helpers import get_step_output
from riddles.jarvis.tasks.build_microservice import get_version_uri, tag_invariant
from riddles.jarvis.tasks.decorators import task
from riddles.jarvis.tasks.helpers import (
    get_image_repository_google_keys_path,
    get_image_repository_project_id,
    file_exist_non_empty,
)


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


@task('build sandbox images')
def build_sandbox_images(context):
    working_tree_is_dirty = is_working_tree_dirty()
    invariant(not working_tree_is_dirty, 'Build canceled: dirty working tree')

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
    invariant(file_exist_non_empty(dockerfile_path), '{} does not exist or is empty'.format(dockerfile_path))
    return dockerfile_path


if __name__ == '__main__':
    Jarvis([
        build_sandbox_images
    ]).run(['jarvis', 'build', 'sandbox', 'images'])
