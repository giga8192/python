import subprocess

#
#path = "/home/user01/Programming/C/HelloWorld/hello"
# hellolink シンボリックリンク
path = "./hellolink" 
proc = subprocess.Popen(path,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stdout.readline().decode())
