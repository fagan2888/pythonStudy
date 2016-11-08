# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。
# 这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

from multiprocessing import Process
import os

print('Process (%s) start...' % os.getpid())

# # Only wroks on Linux/Unix/Mac
# pid = os.fork()
# if pid == 0:
#     print('I\'m child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just craeted a child process (%s)' % (os.getpid(), pid))


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')