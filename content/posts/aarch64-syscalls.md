+++
title = 'Aarch64 Syscalls'
date = 2024-10-21T11:08:36Z
+++
Here is a list of common system calls (syscalls) for AArch64 architecture along with their syscall numbers:

### Process Management
- `sys_exit` (93): Exit a program.
- `sys_fork` (220): Fork a process.
- `sys_execve` (221): Execute a program.
- `sys_wait4` (260): Wait for a child process.

### File Operations
- `sys_read` (63): Read from a file.
- `sys_write` (64): Write to a file.
- `sys_openat` (56): Open a file.
- `sys_close` (57): Close a file.
- `sys_lseek` (62): Set the file offset.
- `sys_statx` (291): Get file status.

### Memory Management
- `sys_brk` (214): Change data segment size.
- `sys_mmap` (222): Map memory.
- `sys_munmap` (215): Unmap memory.

### File System Operations
- `sys_chdir` (49): Change current working directory.
- `sys_mkdirat` (34): Create a directory.
- `sys_rmdir` (84): Remove a directory.
- `sys_unlinkat` (35): Delete a file.
- `sys_renameat` (38): Rename a file.

### I/O Operations
- `sys_ioctl` (29): Control a device.
- `sys_fcntl` (25): File control operations.

### Network
- `sys_socket` (198): Create a socket.
- `sys_connect` (203): Connect to a remote socket.
- `sys_bind` (200): Bind a name to a socket.
- `sys_sendto` (206): Send a message on a socket.
- `sys_recvfrom` (207): Receive a message from a socket.
- `sys_accept` (202): Accept a socket connection.

### Time Management
- `sys_nanosleep` (101): Sleep for a certain number of nanoseconds.
- `sys_gettimeofday` (169): Get the current time.
- `sys_settimeofday` (170): Set the current time.

### Other
- `sys_getpid` (172): Get process ID.
- `sys_getppid` (173): Get parent process ID.
- `sys_kill` (129): Send a signal to a process.
- `sys_getuid` (174): Get user ID.
- `sys_getgid` (176): Get group ID.

To use these syscalls in assembly code, you load the corresponding syscall ID into register `x8`, and the appropriate arguments into registers `x0` to `x7`, then call `svc 0`. 
