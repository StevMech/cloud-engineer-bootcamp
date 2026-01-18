# Week 1 Exercise: Linux File System Mastery

## Overview
Practice essential Linux file system operations, permissions, and text processing.

**Estimated Time**: 90 minutes  
**Difficulty**: Beginner  
**Prerequisites**: Basic terminal knowledge

---

## Exercise 1: Building a Project Structure (20 minutes)

### Task
Create a realistic project directory structure for a web application.

### Requirements

Create the following structure in your home directory:

```
~/web-project/
├── src/
│   ├── frontend/
│   │   ├── components/
│   │   ├── styles/
│   │   └── index.html
│   ├── backend/
│   │   ├── api/
│   │   ├── database/
│   │   └── server.py
│   └── tests/
│       ├── unit/
│       └── integration/
├── docs/
│   ├── README.md
│   └── API.md
├── scripts/
│   ├── deploy.sh
│   └── backup.sh
└── config/
    ├── dev.conf
    └── prod.conf
```

### Commands to Use
```bash
mkdir -p
touch
ls -R
tree (if available)
```

### Validation
Run `ls -R ~/web-project` and verify the structure.

---

## Exercise 2: Permission Management (20 minutes)

### Task
Set appropriate permissions for different file types.

### Requirements

1. Scripts should be executable by owner and group:
   ```bash
   # deploy.sh and backup.sh should have: rwxr-x---
   ```

2. Config files should be readable by owner only:
   ```bash
   # *.conf files should have: rw-------
   ```

3. Documentation should be readable by everyone:
   ```bash
   # *.md files should have: rw-r--r--
   ```

4. Source code should be readable/writable by owner, readable by group:
   ```bash
   # *.py, *.html should have: rw-r-----
   ```

### Commands to Practice
```bash
chmod
chown
ls -l
stat
```

### Validation
```bash
# Check permissions
ls -l ~/web-project/scripts/
ls -l ~/web-project/config/
```

---

## Exercise 3: File Content Creation (15 minutes)

### Task
Create meaningful content in key files.

### Requirements

1. Create `README.md` with project description:
```markdown
# Web Project

A full-stack web application with frontend and backend.

## Structure
- src/frontend: HTML, CSS, JavaScript
- src/backend: Python API server
- docs: Project documentation
- scripts: Deployment and utility scripts
```

2. Create `deploy.sh` script:
```bash
#!/bin/bash
echo "Starting deployment..."
echo "Building frontend..."
echo "Starting backend server..."
echo "Deployment complete!"
```

3. Create `dev.conf`:
```
DATABASE_URL=localhost:5432
API_PORT=8000
DEBUG=true
```

### Commands to Use
```bash
cat > file << EOF
echo "content" > file
nano/vim/vi
```

---

## Exercise 4: Text Processing Challenge (20 minutes)

### Task
Process log files using text processing tools.

### Setup
Create a sample log file:

```bash
cat > ~/web-project/server.log << EOF
2024-01-18 09:00:00 INFO Server started on port 8000
2024-01-18 09:05:23 INFO User login: user123
2024-01-18 09:10:45 ERROR Database connection failed
2024-01-18 09:11:02 INFO Retrying database connection
2024-01-18 09:11:15 INFO Database connected successfully
2024-01-18 09:15:30 WARNING High memory usage: 85%
2024-01-18 09:20:12 ERROR Request timeout: /api/users
2024-01-18 09:25:00 INFO User logout: user123
2024-01-18 09:30:45 ERROR Disk space low: 95% used
EOF
```

### Challenges

1. **Extract all ERROR lines:**
   ```bash
   # Your command here
   # Expected: 3 lines
   ```

2. **Count INFO messages:**
   ```bash
   # Your command here
   # Expected: 5
   ```

3. **Find all timestamps:**
   ```bash
   # Your command here
   # Should show: 2024-01-18 HH:MM:SS
   ```

4. **Create error report (errors.log):**
   ```bash
   # Extract only ERROR lines and save to errors.log
   ```

5. **Find messages with 'user' (case-insensitive):**
   ```bash
   # Your command here
   ```

### Commands to Use
```bash
grep
grep -i
grep -c
wc -l
sed
awk
```

---

## Exercise 5: Search and Navigation (15 minutes)

### Task
Practice finding files and navigating efficiently.

### Challenges

1. **Find all .conf files in web-project:**
   ```bash
   # Your command
   ```

2. **Find all files modified in last 10 minutes:**
   ```bash
   # Your command
   ```

3. **Find all files larger than 0 bytes:**
   ```bash
   # Your command
   ```

4. **Count total number of files:**
   ```bash
   # Your command
   ```

5. **Navigate efficiently:**
   ```bash
   # Start from home, go to web-project/src/backend/api
   # Then go to web-project/docs
   # Then back to home
   # Do this in the minimum number of commands
   ```

### Commands to Use
```bash
find
cd
cd -
pwd
```

---

## Bonus Challenges (Optional)

### Challenge 1: Automation Script
Write a script that:
1. Creates a timestamped backup directory
2. Copies all .conf files to backup
3. Lists what was backed up

```bash
#!/bin/bash
# backup_configs.sh
# Your code here
```

### Challenge 2: Log Analysis
Create a one-liner that:
1. Searches server.log for ERROR
2. Counts how many errors occurred
3. Saves the error count to error_summary.txt

```bash
# Your one-liner here
```

### Challenge 3: Disk Space Monitor
Write a script that:
1. Checks disk usage
2. Warns if any partition is over 80% full
3. Logs the warning to a file

---

## Solution Hints

### Exercise 1 Hints
```bash
mkdir -p ~/web-project/{src/{frontend/{components,styles},backend/{api,database},tests/{unit,integration}},docs,scripts,config}
```

### Exercise 2 Hints
```bash
chmod 750 ~/web-project/scripts/*.sh
chmod 600 ~/web-project/config/*.conf
chmod 644 ~/web-project/docs/*.md
```

### Exercise 4 Hints
```bash
# Extract errors
grep ERROR server.log

# Count INFO
grep -c INFO server.log

# Extract to file
grep ERROR server.log > errors.log
```

---

## Self-Assessment

Check your work:

- [ ] All directories created correctly
- [ ] Permissions set appropriately
- [ ] Files contain expected content
- [ ] Can find specific files using find
- [ ] Can process log files with grep
- [ ] Understand what each command does

## Learning Outcomes

After completing this exercise, you should be able to:

✅ Create complex directory structures efficiently  
✅ Set and understand file permissions  
✅ Create and edit files from command line  
✅ Search and filter text using grep  
✅ Navigate directories quickly  
✅ Use pipes and redirection  
✅ Automate tasks with shell scripts  

---

## Next Steps

1. Try breaking things and fixing them
2. Create your own project structure
3. Practice without looking at hints
4. Time yourself - can you do it faster?
5. Move on to Week 1, Day 2 exercises

**Great work! You're building real Linux skills! 🐧**
