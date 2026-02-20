import os

path_config = r'E:\Documents\GitHub\scripts\confs'
template_config = 'E:/Documents/GitHub/Scripts/confs/@template-18.conf'


def detect_configs() -> list[str]:
    confs = [template_config]
    paths = [os.environ.get('PYCHARM_PROJECT_DIR', False), os.getcwd()]
    for path in paths:
        conf = search_config(path)
        if conf:
            confs.append(conf)
            break
    return confs


def search_config(project_path: str) -> str:
    conf = False
    if project_path and os.path.isdir(path_config) and os.path.exists(project_path):
        base_name = os.path.basename(os.path.normpath(project_path))
        projected_conf = f'{base_name}.conf'
        for file in os.listdir(path_config):
            file_dir = os.path.join(path_config, file)
            if file.lower() == projected_conf.lower() and os.path.isfile(file_dir):
                print(f'Archivo de configuración detectado: {file_dir}')
                conf = file_dir
                break
    return conf
