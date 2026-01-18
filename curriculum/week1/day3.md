# Week 1, Day 3: Text Processing & Log Analysis

## 🎯 Learning Objectives
- Master grep for pattern searching
- Use sed for text transformation
- Apply awk for column-based processing
- Analyze system logs effectively

---

## 🌅 Morning Session: Text Processing Tools

### grep - The Pattern Searcher
```bash
grep "pattern" file.txt          # Basic search
grep -i "pattern" file.txt       # Case-insensitive
grep -r "pattern" directory/     # Recursive search
grep -v "pattern" file.txt       # Invert match (exclude)
grep -n "pattern" file.txt       # Show line numbers
grep -c "pattern" file.txt       # Count matches
grep -E "regex" file.txt         # Extended regex
```

### sed - Stream Editor
```bash
sed 's/old/new/' file.txt        # Replace first occurrence per line
sed 's/old/new/g' file.txt       # Replace all occurrences
sed '1,5d' file.txt              # Delete lines 1-5
sed -n '10,20p' file.txt         # Print lines 10-20
sed -i 's/old/new/g' file.txt    # Edit in-place
```

### awk - Column Processing
```bash
awk '{print $1}' file.txt        # Print first column
awk -F: '{print $1}' /etc/passwd # Custom delimiter
awk '{sum+=$1} END {print sum}'  # Sum first column
awk '$3 > 100' file.txt          # Filter rows
```

---

## ☀️ Afternoon Session: Log Analysis

### Exercise 1: System Log Analysis
```bash
# View system logs
sudo tail -f /var/log/syslog

# Find all errors
grep -i error /var/log/syslog

# Count error types
grep -i error /var/log/syslog | awk '{print $5}' | sort | uniq -c

# Find failed login attempts
grep "Failed password" /var/log/auth.log
```

### Exercise 2: Web Server Logs
Create a sample Apache log:
```bash
cat > access.log << EOF
192.168.1.1 - - [18/Jan/2024:10:00:00] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [18/Jan/2024:10:01:00] "GET /about.html HTTP/1.1" 200 5678
192.168.1.1 - - [18/Jan/2024:10:02:00] "POST /api/login HTTP/1.1" 500 0
192.168.1.3 - - [18/Jan/2024:10:03:00] "GET /images/logo.png HTTP/1.1" 404 0
EOF

# Extract IP addresses
awk '{print $1}' access.log

# Find 404 errors
grep " 404 " access.log

# Count requests per IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn

# Find POST requests
grep "POST" access.log
```

---

## 🌙 Evening Session: Real-World Scenarios

### Pipeline Challenge
Build analysis pipelines:
```bash
# Top 10 most common commands in history
history | awk '{print $2}' | sort | uniq -c | sort -rn | head -10

# Find large log files
find /var/log -type f -size +10M -exec ls -lh {} \;

# Monitor real-time errors
tail -f /var/log/syslog | grep --color=auto -i error
```

**Tomorrow: Process Management! 🔄**
