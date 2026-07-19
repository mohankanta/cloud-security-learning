## Day 9 - Linux File System Structure

### Important directories:
- / → root of entire system
- /etc → all configuration files
- /var/log → all system log files
- /home → user home folders
- /bin → essential commands
- /etc/passwd → all system users
- /etc/shadow → hashed passwords

### Commands learned:
- find / -name → find files by name
- which → find where program is installed
- tail -20 → see last 20 lines of file
- tail -f → watch file live in real time
- grep "keyword" → search inside files

### Security relevance:
- /var/log/auth.log shows login attempts
- grep "Failed" finds failed logins
- These are used in real security investigations

### Mini challenge:
- Completed / Struggled with nmap installation
