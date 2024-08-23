# os module interact with operating system
import os

cwd = os.getcwd()
print("path of cwd", cwd)

# mkdir
# r stands for raw string : which used to remove unicode escape error.. for windows
#os.mkdir("test")
#os.mkdir(r"/Users/manumathew/Repos/test2")

# # listdir()
# li = os.listdir("/Users/manumathew/Repos/python/code")
# print(li)

# # rmdir()
# os.rmdir("/Users/manumathew/Repos/test2")
# To remove dir with files
# import shutil
# shutil.rmtree()

# os.chdir("python")
# cwd = os.getcwd()
# print("path of cwd", cwd)
# remove() to remove files
# os.remove("/Users/manumathew/Repos/test.txt")
help(os)
