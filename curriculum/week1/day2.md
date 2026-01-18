# Week 1, Day 2: File Permissions & Ownership

## 🎯 Learning Objectives
- Understand Linux permission model (read, write, execute)
- Manage file ownership and groups
- Use chmod, chown, and chgrp commands
- Apply proper security practices

---

## 🌅 Morning Session: Theory

### Linux Permission Model

Every file and directory has three permission sets:
- **Owner** (user): The person who owns the file
- **Group**: Users in the file's group
- **Others**: Everyone else

Each set has three permissions:
- **Read (r)**: View file contents or list directory
- **Write (w)**: Modify file or create/delete files in directory
- **Execute (x)**: Run file as program or enter directory

### Viewing Permissions

```bash
ls -l filename
-rw-r--r-- 1 user group 1234 Jan 18 10:00 filename
│││││││││
│││││││└┴── Others permissions (r--)
│││││└┴──── Group permissions (r--)
│││└┴────── Owner permissions (rw-)
││└──────── Number of hard links
│└───────── File type (- = regular file, d = directory)
```

### Permission Notation

**Symbolic**: rwx r-x r--
**Numeric (Octal)**: 754
- r = 4, w = 2, x = 1
- rwx = 4+2+1 = 7
- r-x = 4+0+1 = 5
- r-- = 4+0+0 = 4

---

## ☀️ Afternoon Session: Hands-On

### Exercise 1: Understanding Permissions

```bash
# Create test file
touch testfile.txt

# View permissions
ls -l testfile.txt

# Try different permission combinations
chmod 644 testfile.txt  # rw-r--r--
chmod 755 testfile.txt  # rwxr-xr-x
chmod 600 testfile.txt  # rw-------

# Symbolic notation
chmod u+x testfile.txt  # Add execute for user
chmod g-w testfile.txt  # Remove write for group
chmod o-r testfile.txt  # Remove read for others
```

### Exercise 2: Directory Permissions

```bash
mkdir testdir
chmod 755 testdir  # Standard directory permissions

# Without execute on directory
chmod 644 testdir
cd testdir  # This will fail!

# Restore
chmod 755 testdir
```

### Exercise 3: Ownership

```bash
# View owner and group
ls -l file.txt

# Change owner (requires sudo)
sudo chown newuser file.txt

# Change group
sudo chgrp newgroup file.txt

# Change both
sudo chown newuser:newgroup file.txt

# Recursive change
sudo chown -R user:group directory/
```

---

## 🌙 Evening Session: Security Scenarios

### Scenario 1: Securing Sensitive Files
```bash
# Create sensitive file
echo "password123" > secrets.txt

# Only owner can read/write
chmod 600 secrets.txt

# Verify
ls -l secrets.txt
```

### Scenario 2: Shared Project Directory
```bash
# Create shared directory
mkdir /shared/project
sudo chgrp developers /shared/project
chmod 770 /shared/project  # Group can read/write/execute
```

### Key Takeaways
- Always use principle of least privilege
- Scripts need execute permission
- Directories need execute to access contents
- Never use 777 on production systems!

---

**Tomorrow: Text Processing & Filters! 🔍**
