# import importlib.util

# module_name = "my_logging"
# module_file_path = "path/to/my_logging_module"

# module_spec = importlib.util.spec_from_file_location(
#     module_name, module_file_path)
# module = importlib.util.module_from_spec(module_spec)
# module_spec.loader.exec_module(module)

# print(dir(module))

print("{2},{1},{0}".format(*"abc"))  # pylint: disable

# import os
# os.chdir(r"c:\Users\Admin")
# print(os.getcwd())

# numbers = range(3)
# output = {*numbers}
# print(output)

from collections import deque
import string

d = deque(string.ascii_lowercase)
d.append("bark")
d.appendleft("yo")
d.rotate()
print(d)
