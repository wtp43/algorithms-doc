## Enable Logging
1. Enable logging for the sshd daemon: sudo vi /etc/ssh/sshd_config
2. Under logging uncomment:

SyslogFacility AUTH  
LogLevel INFO

1. Change LogLevel from INFO to DEBUG
2. Save and exit
3. Restart the SSH daemon with sudo systemctl restart sshd
4. Watch the messages file tail -l /var/log/auth.log