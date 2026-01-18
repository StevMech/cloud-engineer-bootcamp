# Week 1, Day 4: Process Management

## 🎯 Learning Objectives
- Understand Linux processes and their lifecycle
- Monitor system resources effectively
- Control running processes
- Manage background jobs

---

## 🌅 Morning Session: Process Fundamentals

### What is a Process?
A process is a running instance of a program with:
- **PID** (Process ID): Unique identifier
- **PPID** (Parent Process ID): Who started it
- **State**: Running, sleeping, stopped, zombie
- **Priority**: Scheduling importance
- **Memory**: RAM allocation
- **CPU**: Processor usage

### Viewing Processes
```bash
ps                    # Current shell processes
ps aux                # All processes, detailed
ps aux | grep nginx   # Find specific process
pstree               # Process tree

top                  # Interactive monitor
htop                 # Better interactive monitor (install: apt install htop)

# Useful ps options
ps -ef               # Full format listing
ps -u username       # Processes for specific user
ps -C processname    # Processes by name
```

---

## ☀️ Afternoon Session: Process Control

### Managing Processes
```bash
# Starting processes
command              # Foreground
command &            # Background
nohup command &      # Background, persist after logout

# Stopping processes
kill PID             # Terminate (SIGTERM)
kill -9 PID          # Force kill (SIGKILL)
killall processname  # Kill by name

# Process priority
nice -n 10 command   # Start with lower priority
renice -n 5 -p PID   # Change priority of running process
```

### Background Jobs
```bash
jobs                 # List background jobs
fg %1                # Bring job 1 to foreground
bg %1                # Send job 1 to background
Ctrl+Z               # Suspend current job
Ctrl+C               # Kill current job
```

---

## 🌙 Evening Session: System Monitoring

### Resource Monitoring
```bash
# CPU and memory
top                  # Real-time monitor
htop                 # Enhanced monitor
free -h              # Memory usage
uptime               # System load

# Disk I/O
iostat               # I/O statistics
iotop                # I/O by process

# Network
netstat -tulpn       # Network connections
ss -tulpn            # Socket statistics (modern netstat)
```

### Troubleshooting Scenario
Find and kill a misbehaving process:
```bash
# 1. Find high CPU process
top
# Press 'P' to sort by CPU

# 2. Get more info
ps aux | grep PID

# 3. Investigate
lsof -p PID          # Open files
strace -p PID        # System calls

# 4. Terminate gracefully
kill PID

# 5. Force if needed
kill -9 PID
```

**Tomorrow: Package Management! 📦**
