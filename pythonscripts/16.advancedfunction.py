import os


print(os.listdir("files"))      # linux's command: ls
for files in os.listdir("files"):
    print(files)

print(os.getcwd())              # linux's command: pwd

# os.chdir('files')               # linux's command: cd
# print(os.getcwd())

# os.path.isdir(dirname) // os.path.isfile(filename) // os.path.exists(dirname or filename)
if os.path.exists("17.functionopera.py"):
    print("files is exists")
else:
    print("files is not exists")

# 获取文件的大小 8byte = 1bit // 1024bit = 1kbit // 1024kbit = 1mbit
print(os.path.getsize("16.advancedfunction.py"))

# 获取文件的绝对路径
print(os.path.abspath("files"))     # cd + pwd // find

# 分割目录与文件
path = os.path.abspath("16.advancedfunction.py")
print(os.path.split(path))

# 分割文件名与拓展名
print(os.path.splitext("16.advancedfunction.py"))
print(os.path.splitext("admin.sh.py.sh"))
print(os.path.splitext("admin.dissssstrtttdfagferasg"))

# 连接目录名 与 文件名和目录名
dirname = "/Users"
filename = "01.variables.py"
print(os.path.join(dirname, filename))

# 获取文件名及目录名
print(os.path.basename(dirname))
print(os.path.dirname(dirname))





