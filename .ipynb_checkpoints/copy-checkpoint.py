import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
copyanything('../data/DAVIS/DAVIS-2017-test-challenge-480p/DAVIS/JPEGImages/480p','../InstanceId2/Data')