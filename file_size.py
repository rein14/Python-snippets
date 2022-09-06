import pathlib

# def print_file_size(path):
#     path_obj = pathlib.Path(path)
#     if path_obj.is_file():
#         print(path, path_obj.stat().st_size)
#     else:
#         for path in path_obj.glob("*"):
#             print_file_size(path)

def print_file_size(dir):

    paths_to_process = [dir]
    path, *paths_to_process  = paths_to_process
    path_obj = pathlib.Path(path)
    if path_obj.is_file():
        print(path, path_obj.stat().st_size)
    else:
        paths_to_process += path_obj.glob('*')

print(print_file_size('hex.py'))
