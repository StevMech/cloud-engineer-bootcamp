# Week 1 Assessment

## 📝 Linux Fundamentals Assessment

**Time Limit**: 2 hours  
**Passing Score**: 70%  
**Total Points**: 100

---

## Part 1: Knowledge Check (30 points)

### Multiple Choice (2 points each)

1. What command displays your current working directory?
   - a) `cwd`
   - b) `pwd`
   - c) `dir`
   - d) `where`

2. Which permission allows you to enter a directory?
   - a) Read
   - b) Write
   - c) Execute
   - d) All of the above

3. What does `chmod 755` mean?
   - a) Owner: rwx, Group: r-x, Others: r-x
   - b) Owner: rwx, Group: rw-, Others: r--
   - c) Owner: rw-, Group: r--, Others: r--
   - d) Owner: r-x, Group: r-x, Others: r-x

4. Which command creates nested directories in one command?
   - a) `mkdir -r`
   - b) `mkdir -p`
   - c) `mkdir -n`
   - d) `mkdir -recursive`

5. What does the `~` symbol represent?
   - a) Root directory
   - b) Home directory
   - c) Parent directory
   - d) Current directory

---

## Part 2: Practical Tasks (50 points)

Complete these tasks in your terminal and save your commands.

### Task 1: Directory Structure (10 points)

Create the following directory structure:
```
~/assessment/
├── project/
│   ├── src/
│   ├── tests/
│   └── docs/
└── backup/
```

**Commands to submit:**
```bash
# Write your commands here
```

### Task 2: File Operations (10 points)

1. Create a file named `config.txt` in `~/assessment/project/`
2. Copy it to the `backup/` directory
3. Rename the copy to `config.backup.txt`
4. List all files recursively in `~/assessment/`

**Commands:**
```bash
# Your commands
```

### Task 3: Permissions Management (15 points)

1. Create a script file `deploy.sh` in `~/assessment/project/`
2. Make it executable for the owner only
3. Set permissions so:
   - Owner can read, write, execute
   - Group can read and execute
   - Others have no permissions

**Commands:**
```bash
# Your commands
```

### Task 4: Text Processing (15 points)

1. Create a log file with the following content:
```
2024-01-18 10:00:00 INFO Server started
2024-01-18 10:05:00 ERROR Connection failed
2024-01-18 10:10:00 INFO Retry successful
2024-01-18 10:15:00 ERROR Timeout
```

2. Extract only ERROR lines
3. Count total number of log entries
4. Save ERROR lines to `errors.log`

**Commands:**
```bash
# Your commands
```

---

## Part 3: Troubleshooting Scenarios (20 points)

### Scenario 1: Permission Denied (10 points)

You're trying to execute a script but get "Permission denied". The current permissions are:
```
-rw-r--r-- 1 user group 1234 Jan 18 10:00 deploy.sh
```

**Questions:**
1. Why can't you execute the script?
2. What command would fix this?
3. What permissions should production scripts have?

**Your Answer:**
```
1. 
2. 
3. 
```

### Scenario 2: Disk Space Investigation (10 points)

Your server is running out of disk space. What commands would you use to:
1. Check overall disk usage
2. Find the largest files in `/var/log/`
3. View the size of each directory in your home folder

**Commands:**
```bash
1. 
2. 
3. 
```

---

## Bonus Challenge (10 points)

Write a bash one-liner that:
1. Lists all `.txt` files in the current directory
2. Counts how many there are
3. Saves the list to `txt_files.list`

**Your one-liner:**
```bash

```

---

## Submission

1. Save all your commands in a file named `week1_assessment.txt`
2. Include output screenshots where applicable
3. Mark yourself using the answer key provided

## Answer Key

Available after completing the assessment. Check `assessments/week1_answers.md`

---

## Grading Rubric

- **90-100**: Excellent - Deep understanding, efficient solutions
- **80-89**: Very Good - Solid understanding, minor improvements
- **70-79**: Good - Meets requirements, some gaps
- **Below 70**: Needs Review - Revisit the material

**Good luck! 🚀**
