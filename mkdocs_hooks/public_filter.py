import yaml


def on_files(files, config):
    """public: true でないページをビルドから除外"""
    to_remove = []
    for file in files:
        if not file.src_path.endswith('.md'):
            continue
        with open(file.abs_src_path, 'r') as f:
            content = f.read()
        if content.startswith('---'):
            fm = yaml.safe_load(content.split('---')[1])
            if not (fm and fm.get('public') is True):
                to_remove.append(file)
        else:
            to_remove.append(file)
    for file in to_remove:
        files.remove(file)
    return files
