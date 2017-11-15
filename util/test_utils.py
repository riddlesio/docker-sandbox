
def image(kind, language_shorthand, version):
    return 'gcr.io/riddles-microservices/sandbox-{}-{}:{}'.format(kind, language_shorthand, version)

def compiler_image(language_shorthand, version):
    return image('compiler', language_shorthand, version)

def runtime-image(language_shorthand, version):
    return image('runtime', language_shorthand, version)

def create_docker_compile_command(self, source_dir, bin_dir, image) -> str:
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

def create_docker_runtime_command(self, bot_dir, executable_filename, image) -> str:
    bot_dir_host_path = bin_dir
    bot_dir_mount_point = '/bot'

    return (
        'docker run '
        '-c {cpu_shares} '
        '-m {max_memory} '
        # Mount bot_dir as read-only
        '-v {bot_dir_host_path}:{bot_dir_mount_point}:ro '
        '--net none '
        '{image} '
        '{bot_dir_mount_point}/{executable_filename}'
    ).format(
        bot_dir_host_path=bot_dir_host_path,
        bot_dir_mount_point=bot_dir_mount_point,
        cpu_shares=512,
        executable_filename=executable_filename,
        max_memory='200M',
        image=image
    )
