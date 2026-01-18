# Linux Command Line Cheatsheet

## File System Navigation

```bash
pwd                    # Print working directory
cd /path/to/dir       # Change directory
cd ~                  # Go to home directory
cd -                  # Go to previous directory
cd ..                 # Go to parent directory
ls                    # List files
ls -la                # List all files with details
ls -lh                # List with human-readable sizes
tree                  # Show directory tree (if installed)
```

## File Operations

```bash
touch file.txt        # Create empty file
cat file.txt          # Display file content
less file.txt         # Page through file
head file.txt         # First 10 lines
tail file.txt         # Last 10 lines
tail -f file.txt      # Follow file (live updates)

cp source dest        # Copy file
cp -r dir1 dir2       # Copy directory recursively
mv old new            # Move/rename
rm file.txt           # Remove file
rm -r directory       # Remove directory recursively
rm -rf directory      # Force remove (DANGEROUS!)

mkdir dirname         # Create directory
mkdir -p path/to/dir  # Create nested directories
rmdir dirname         # Remove empty directory
```

## File Permissions

```bash
chmod 755 file.sh     # rwxr-xr-x
chmod 644 file.txt    # rw-r--r--
chmod u+x file.sh     # Add execute for user
chmod g-w file.txt    # Remove write for group
chmod o-r file.txt    # Remove read for others

chown user file       # Change owner
chgrp group file      # Change group
chown user:group file # Change both

# Permission values
# r (read) = 4
# w (write) = 2
# x (execute) = 1
```

## Text Processing

```bash
grep "pattern" file           # Search for pattern
grep -r "pattern" dir/        # Recursive search
grep -i "pattern" file        # Case-insensitive
grep -v "pattern" file        # Invert match

sed 's/old/new/' file         # Replace first occurrence
sed 's/old/new/g' file        # Replace all occurrences
sed -i 's/old/new/g' file     # Edit file in-place

awk '{print $1}' file         # Print first column
awk -F: '{print $1}' file     # Custom delimiter

cut -d: -f1 file              # Cut first field
sort file                     # Sort lines
sort -r file                  # Reverse sort
uniq file                     # Remove duplicates
wc -l file                    # Count lines
```

## Process Management

```bash
ps aux                        # List all processes
ps aux | grep process         # Find specific process
top                           # Live process monitor
htop                          # Better process monitor

kill PID                      # Terminate process
kill -9 PID                   # Force kill
killall processname           # Kill by name

bg                            # Send to background
fg                            # Bring to foreground
jobs                          # List background jobs

command &                     # Run in background
nohup command &               # Run after logout
```

## System Information

```bash
uname -a                      # System information
hostname                      # System hostname
uptime                        # System uptime
whoami                        # Current user
who                           # Logged in users

df -h                         # Disk space (human-readable)
du -sh directory              # Directory size
free -h                       # Memory usage

lscpu                         # CPU information
lsblk                         # Block devices
```

## Network Commands

```bash
ip addr                       # IP addresses
ifconfig                      # Network interfaces (deprecated)
ping host                     # Test connectivity
traceroute host               # Trace route
netstat -tulpn                # Network connections
ss -tulpn                     # Socket statistics (modern)

curl URL                      # Transfer data from URL
wget URL                      # Download file
curl -I URL                   # Get headers only

dig domain.com                # DNS lookup
nslookup domain.com           # DNS query
host domain.com               # DNS info
```

## Package Management

### Debian/Ubuntu (apt)
```bash
apt update                    # Update package list
apt upgrade                   # Upgrade packages
apt install package           # Install package
apt remove package            # Remove package
apt search package            # Search for package
apt show package              # Show package info
```

### RHEL/CentOS/Rocky (yum/dnf)
```bash
yum update                    # Update packages
yum install package           # Install package
yum remove package            # Remove package
yum search package            # Search for package
dnf install package           # (dnf is yum successor)
```

## Archive & Compression

```bash
tar -czf archive.tar.gz dir/  # Create compressed archive
tar -xzf archive.tar.gz       # Extract archive
tar -tzf archive.tar.gz       # List archive contents

zip -r archive.zip dir/       # Create zip
unzip archive.zip             # Extract zip

gzip file                     # Compress file
gunzip file.gz                # Decompress
```

## Redirection & Pipes

```bash
command > file                # Redirect stdout to file
command >> file               # Append stdout to file
command 2> file               # Redirect stderr
command &> file               # Redirect both stdout/stderr

command1 | command2           # Pipe output
command < file                # Input from file

# Examples
ls -l > files.txt
grep error logfile | wc -l
cat file1 file2 > combined.txt
```

## Search & Find

```bash
find . -name "*.txt"          # Find files by name
find . -type f -mtime -7      # Modified in last 7 days
find . -size +10M             # Larger than 10MB
find . -user username         # Owned by user

locate filename               # Quick find (uses database)
which command                 # Show command location
whereis command               # Binary, source, manual
```

## User Management

```bash
useradd username              # Create user
userdel username              # Delete user
passwd username               # Change password
usermod -aG group user        # Add user to group

groupadd groupname            # Create group
groupdel groupname            # Delete group

su username                   # Switch user
sudo command                  # Run as superuser
```

## Shell Scripting Basics

```bash
#!/bin/bash                   # Shebang

# Variables
NAME="value"
echo $NAME

# Conditionals
if [ condition ]; then
    commands
fi

# Loops
for i in {1..5}; do
    echo $i
done

while [ condition ]; do
    commands
done

# Functions
function_name() {
    commands
}
```

## Shortcuts & Tips

```bash
Ctrl + C                      # Cancel current command
Ctrl + Z                      # Suspend current command
Ctrl + D                      # Exit shell/logout
Ctrl + L                      # Clear screen
Ctrl + R                      # Search command history

Tab                           # Auto-complete
↑/↓                          # Navigate history
!!                            # Repeat last command
!$                            # Last argument of previous command

alias ll='ls -la'             # Create alias
history                       # Command history
clear                         # Clear terminal
```

## Docker Commands (Preview for Week 3)

```bash
docker run image              # Run container
docker ps                     # List running containers
docker ps -a                  # List all containers
docker images                 # List images
docker build -t name .        # Build image
docker exec -it container sh  # Enter container
docker logs container         # View logs
docker stop container         # Stop container
docker rm container           # Remove container
docker rmi image              # Remove image
```

## Kubectl Commands (Preview for Week 4)

```bash
kubectl get pods              # List pods
kubectl get services          # List services
kubectl describe pod name     # Describe pod
kubectl logs pod-name         # View logs
kubectl exec -it pod sh       # Enter pod
kubectl apply -f file.yaml    # Apply configuration
kubectl delete -f file.yaml   # Delete resources
kubectl get nodes             # List nodes
```

## Useful One-Liners

```bash
# Find large files
find / -type f -size +100M 2>/dev/null

# Count files in directory
ls -1 | wc -l

# Disk usage of subdirectories
du -h --max-depth=1 | sort -hr

# Find and kill process
ps aux | grep process | awk '{print $2}' | xargs kill

# Monitor file changes
watch -n 2 'ls -lh file'

# Extract specific column from CSV
awk -F, '{print $3}' file.csv

# Remove empty lines
sed '/^$/d' file.txt

# Get public IP
curl ifconfig.me

# Weather (fun!)
curl wttr.in/CityName
```

## Common Patterns

### Backup Files
```bash
cp file.txt file.txt.bak
cp file.txt file.txt.$(date +%Y%m%d)
```

### Monitor Logs
```bash
tail -f /var/log/syslog | grep ERROR
```

### Batch Rename
```bash
for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done
```

### Find and Replace in Multiple Files
```bash
find . -type f -name "*.txt" -exec sed -i 's/old/new/g' {} \;
```

---

**Pro Tip**: Keep this cheatsheet handy! Use `man command` for detailed documentation.

**Practice**: Try to use each command at least once. Muscle memory is key!

**Safety**: Always double-check before running destructive commands like `rm -rf`.
