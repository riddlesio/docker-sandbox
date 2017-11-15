

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

def create_docker_runtime_command(self, bot_dir, image) -> str:
    raise NotImplementedError()
