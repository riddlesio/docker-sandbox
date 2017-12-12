import os
import pytest
from riddles.jarvis.steps.docker import get_latest_tag_for_commit_hash
from riddles.jarvis.steps.git import get_latest_commit_hash

def as_id(datum):
    # Important:
    # 
    # This function cannot return a value which is also
    # used as a marker. This screws up the test selection
    # for some reason.
    return 'ProgrammingLanguage(slug={})'.format(datum)

def as_param(datum):
    # Dynamically create a marker from fixture data,
    # so it becomes possible to run the compiler tests
    # for a subset of programming languages.
    mark = getattr(pytest.mark, datum[0])
    return pytest.param(datum, marks=mark)

def image(kind, language_shorthand):
    image = 'sandbox-{}-{}'.format(kind, language_shorthand)

    commit_hash = get_latest_commit_hash()
    version = get_latest_tag_for_commit_hash(
        hash=commit_hash, microservice_name=image)

    return 'gcr.io/riddles-microservices/{}:{}'.format(image, version)


def compiler_image(language_shorthand):
    return image('compiler', language_shorthand)


def runtime_image(language_shorthand):
    return image('runtime', language_shorthand)


def create_docker_compile_command(source_dir, bin_dir, image) -> str:
    source_dir_host_path = source_dir
    source_dir_mount_point = '/tmp/riddles/compiler/source'

    bin_dir_host_path = bin_dir
    bin_dir_mount_point = '/tmp/riddles/compiler/bin'

    return (
        'docker run '
        '-c {cpu_shares} '
        '-e "SOURCE_DIR={source_dir_mount_point}" '
        '-e "BIN_DIR={bin_dir_mount_point}" '
        '-m {max_memory} '
        # Mount source_dir as read-only, bin_dir as read-write
        '-v {source_dir_host_path}:{source_dir_mount_point}:ro '
        '-v {bin_dir_host_path}:{bin_dir_mount_point}:rw '
        '--net none '
        '{image}'
    ).format(
        source_dir_host_path=source_dir_host_path,
        source_dir_mount_point=source_dir_mount_point,
        bin_dir_host_path=bin_dir_host_path,
        bin_dir_mount_point=bin_dir_mount_point,
        cpu_shares=512,
        max_memory='200M',
        image=image
    )


def create_docker_runtime_command(bot_dir, runtime, executable_filename, image) -> str:
    bot_dir_host_path = bot_dir
    bot_dir_mount_point = '/bot'

    if runtime is None:
        cmd = '{bot_dir_mount_point}/{executable_filename}'.format(
            bot_dir_mount_point=bot_dir_mount_point,
            executable_filename=executable_filename,
        )
    else:
        cmd = '{runtime} {bot_dir_mount_point}/{executable_filename}'.format(
            bot_dir_mount_point=bot_dir_mount_point,
            executable_filename=executable_filename,
            runtime=runtime,
        )

    return (
        'docker run '
        '-a STDIN '
        '-a STDOUT '
        '-a STDERR '
        '-i '
        '-c {cpu_shares} '
        '-m {max_memory} '
        # Mount bot_dir as read-only
        '-v {bot_dir_host_path}:{bot_dir_mount_point}:ro '
        '--net none '
        '{image} '
        '{cmd}'
    ).format(
        bot_dir_host_path=bot_dir_host_path,
        bot_dir_mount_point=bot_dir_mount_point,
        cmd=cmd,
        cpu_shares=512,
        max_memory='200M',
        image=image
    )


def get_manifest_executable(manifest_path):
    with open(manifest_path) as manifest:
        data = manifest.read()
        return data.strip()
