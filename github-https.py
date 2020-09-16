import subprocess
proc_add = subprocess.run(['git', 'add', '/path/to/your/object'] ,stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = "/path/to/your/run/dir")
print(proc_add.stdout.decode("utf8"))
print(proc_add.stderr.decode("utf8"))

try:
    proc_commit = subprocess.run(['git', 'commit', '-m', '"github test"'] ,stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = "/path/to/your/run/dir")
    print(proc_commit.stdout.decode("utf8"))
    print(proc_commit.stderr.decode("utf8"))
except:
    print("変更がないのでcommitできません")
    
try:
    url = "https://{your_user_name}:{your_passwd}@github.com/path/to/repo" 
    proc_push = subprocess.run(['git', 'push', url, ] ,stdout = subprocess.PIPE, stderr = subprocess.PIPE, cwd = "/path/to/your/run/dir")
    print(proc_push.stdout.decode("utf8"))
    print(proc_push.stderr.decode("utf8"))
except:
    print("pushできませんでした")