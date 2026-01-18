# Week 1, Day 1: Linux Introduction & File System Navigation

## 🎯 Learning Objectives
By the end of today, you will be able to:
- Understand the Linux file system hierarchy
- Navigate directories using command-line tools
- Perform basic file operations
- Use absolute and relative paths effectively

---

## 🌅 Morning Session (09:00-11:00): Theory & Concepts

### What is Linux?
Linux is an open-source, Unix-like operating system kernel that powers everything from smartphones to supercomputers. As a cloud platform engineer, you'll work with Linux daily because:
- Most cloud servers run Linux
- Container images are typically Linux-based
- Linux offers powerful command-line tools for automation

### Linux Distributions
Common distributions you'll encounter:
- **Ubuntu**: Popular for cloud instances (AWS, Azure, GCP)
- **Red Hat Enterprise Linux (RHEL)**: Enterprise-focused
- **CentOS/Rocky Linux**: RHEL alternatives
- **Amazon Linux**: Optimized for AWS
- **Alpine Linux**: Minimal, used in containers

### The Linux File System Hierarchy

```
/                    # Root directory (top of the hierarchy)
├── bin             # Essential user binaries (ls, cat, cp)
├── boot            # Boot loader files
├── dev             # Device files
├── etc             # System configuration files
├── home            # User home directories
│   └── username    # Your personal directory
├── lib             # System libraries
├── opt             # Optional application packages
├── tmp             # Temporary files
├── usr             # User programs and data
│   ├── bin        # User binaries
│   ├── lib        # User libraries
│   └── local      # Locally installed software
└── var             # Variable data (logs, caches)
    └── log        # System log files
```

### Understanding Paths

**Absolute Path**: Starts from root `/`
```bash
/home/username/documents/file.txt
```

**Relative Path**: Relative to current directory
```bash
documents/file.txt    # From home directory
../username/file.txt  # Using parent directory
```

**Special Directories**:
- `.` = Current directory
- `..` = Parent directory
- `~` = Your home directory
- `/` = Root directory

---

## ☀️ Afternoon Session (14:00-17:00): Hands-On Practice

### Exercise 1: Getting Your Bearings

Open your terminal and try these commands:

```bash
# Print working directory (where am I?)
pwd

# List files in current directory
ls

# List with details (permissions, size, date)
ls -l

# List including hidden files
ls -a

# Combine options
ls -lah
```

**Challenge**: What's the difference between `ls`, `ls -l`, and `ls -lh`?

### Exercise 2: Navigation

```bash
# Change to home directory
cd ~

# Change to root directory
cd /

# Go back to previous directory
cd -

# Change to parent directory
cd ..

# Change to specific directory
cd /var/log
```

**Practice Task**: Start from your home directory and navigate to `/etc`, then back to home, then to `/tmp`.

### Exercise 3: File Operations

```bash
# Create an empty file
touch myfile.txt

# Create a directory
mkdir mydir

# Create nested directories
mkdir -p mydir/subdir1/subdir2

# Copy a file
cp myfile.txt myfile_backup.txt

# Copy a directory (recursive)
cp -r mydir mydir_backup

# Move/rename a file
mv myfile.txt newname.txt

# Remove a file
rm newname.txt

# Remove an empty directory
rmdir mydir

# Remove a directory and its contents
rm -r mydir_backup
```

**⚠️ Warning**: `rm -rf` is dangerous! It permanently deletes without confirmation. Always double-check before using it.

### Exercise 4: Real-World Scenario

Let's set up a project directory structure:

```bash
# Create project structure
mkdir -p ~/projects/cloud-bootcamp/{week1,week2,week3,week4}
mkdir -p ~/projects/cloud-bootcamp/week1/{notes,exercises,labs}

# Navigate to the project
cd ~/projects/cloud-bootcamp/week1

# Create some files
touch notes/day1.md
touch exercises/exercise1.sh

# List the structure
ls -R ~/projects/cloud-bootcamp
```

### Exercise 5: Viewing Files

```bash
# View entire file
cat filename.txt

# View file one screen at a time
less filename.txt    # Press 'q' to quit, arrows to navigate

# View first 10 lines
head filename.txt

# View last 10 lines
tail filename.txt

# View first 20 lines
head -n 20 filename.txt

# Follow a file (useful for logs)
tail -f /var/log/syslog
```

---

## 🌙 Evening Session (19:00-20:00): Review & Reinforcement

### Key Takeaways
1. **Everything in Linux is a file** - even devices and directories
2. **The file system is hierarchical** - starts from root `/`
3. **Use tab completion** - press Tab to auto-complete file/directory names
4. **Be careful with rm** - there's no recycle bin in Linux!

### Quick Quiz

1. What command shows your current directory?
2. How do you create a directory called "test"?
3. What's the difference between `cp` and `mv`?
4. How do you list hidden files?
5. What does `cd ..` do?

### Command Cheat Sheet

| Command | Purpose | Example |
|---------|---------|---------|
| `pwd` | Print working directory | `pwd` |
| `ls` | List files | `ls -lah` |
| `cd` | Change directory | `cd /home` |
| `mkdir` | Make directory | `mkdir mydir` |
| `touch` | Create file | `touch file.txt` |
| `cp` | Copy | `cp file1 file2` |
| `mv` | Move/rename | `mv old new` |
| `rm` | Remove | `rm file.txt` |
| `cat` | View file | `cat file.txt` |
| `less` | Page through file | `less file.txt` |

### Tomorrow's Preview
Tomorrow we'll dive into **file permissions and ownership** - understanding who can read, write, and execute files, and how to manage security in Linux.

### Optional Practice
- Explore your system's `/etc` directory (configuration files)
- Check out `/var/log` to see system logs
- Create a personal note-taking system using directories and files
- Practice navigating without using `cd` (hint: use full paths)

---

## 💡 Pro Tips
1. **Use tab completion** - Start typing and press Tab to auto-complete
2. **Use up arrow** - Recall previous commands
3. **Use man pages** - `man ls` shows the manual for the `ls` command
4. **Copy-paste carefully** - Right-click or Ctrl+Shift+V in terminals
5. **Create aliases** - Add shortcuts to your `.bashrc` file

## 📚 Additional Resources
- [Linux Journey](https://linuxjourney.com/) - Interactive tutorials
- [ExplainShell](https://explainshell.com/) - Breakdown of shell commands
- [Linux Command Library](https://linuxcommandlibrary.com/) - Quick reference

---

**Great start! See you tomorrow for Day 2! 🚀**
