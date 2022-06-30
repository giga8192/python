import os
import pathlib
import logging


logger = logging.getLogger("myLogger")

# networkdから
def scripts_in_path(path, subdir):
    """Given directory names in PATH notation (separated by :), and a
    subdirectory name, return a sorted list of executables
    contained in that subdirectory, such that executables in earlier
    path components override those with the same name in later path
    components."""
    script_list = []
    base_filenames = set()
    for one_path in path.split(":"):
        one_path = os.path.join(one_path, subdir)
        #print(one_path)
        if not os.path.exists(one_path):
            logger.debug("Path %r does not exist; skipping", one_path)
            continue
        base_filenames.update(os.listdir(one_path))
        # debug
        print(base_filenames)
    for filename in sorted(base_filenames):
        for one_path in path.split(":"):
            pathname = os.path.join(one_path, subdir, filename)
            print("2" + pathname)

            if os.path.isfile(pathname):
                print("check")
                try:
                    print("check5: " + pathname)
                    realpath = pathlib.Path(pathname).resolve()
                    print("check6")
                    # Make sure that the file's parent dir has the correct
                    # perms, without following any symlinks
                    # uid=0,gid=0はroot、　ここではテストのため改変する
                    if not check_perms(os.path.dirname(pathname),
                                       0o755, 1000, 1000):
                        print("3:error")
                        continue

                    # Make sure file has correct perms, after following any
                    # symlink(s)
                    if not check_perms(realpath, 0o755, 1000, 1000):
                        print("4:error")
                        continue
                except FileNotFoundError:
                    print("check3")
                    continue

                script_list.append(pathname)
                print("check2")
                break

    return script_list

# 0oは8進数
def check_perms(path, mode=0o755, uid=0, gid=0):
    """ Check that the given file or dir @ path has the given mode set, and is
    owned by the given uid/gid. Symlinks are *not* followed. Raises
    FileNotFoundError if path doesn't exist."""

    if not os.path.exists(path):
        raise FileNotFoundError
    st = os.stat(path, follow_symlinks=False)
    st_mode = st.st_mode & 0x00FFF
    if st.st_uid == uid and st.st_gid == gid and st_mode == mode:
        return True

    logger.error("invalid permissions on %s. expected mode=%s, uid=%d, "
                 "gid=%d; got mode=%s, uid=%d, gid=%d", path, oct(mode), uid,
                 gid, oct(st_mode), st.st_uid, st.st_gid)
    return False


path1 = "/home/user01/Programming"
path2 = "../../../tmp" # パスとラバーサル
symlink = "hoge"

pathResult1 = os.path.join(path1,path2)
print(pathResult1)

# パストラバーサルが動作してしまう
os.chdir(pathResult1)
print(os.getcwd()) # /tmp


pathResult2 = os.path.join(path1,path2,symlink)
print(pathResult2) # /home/user01/Programming/../../../tmp/hoge -> /tmp/hoge
if os.path.isfile(pathResult2):
    print(pathResult2 + " isfile OK")
else:
    print(pathResult2 + " isfile NG")
testpath1 = "/home/user01/Programming/python/test1/test1.py"
if check_perms(testpath1,uid=1000,gid=1000):
    print(testpath1 + ": OK")

myPythonDir1 = "/home/user01/Programming/python/"
myPythonSubDir1 = "test1"

print("--------------------------")
result = scripts_in_path(myPythonDir1, myPythonSubDir1)
print("戻り値")
print(result)
