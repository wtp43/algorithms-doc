### chmod
>ls -l 
`drwxr-xr-x`
- first letter is d if directory, else -
- next 3 groups are user, group, and other permissions (anyone not in the first two groups)

0: (000) No permission.
1: (001) Execute permission.
2: (010) Write permission.
3: (011) Write and execute permissions.
4: (100) Read permission.
5: (101) Read and execute permissions.
6: (110) Read and write permissions.
7: (111) Read, write, and execute permissions.

### Systemctl
- systemctl restart/enable/disable/stop/start
- service <service> status
- 