# Week 1, Day 5: Package Management & System Updates

## 🎯 Learning Objectives
- Understand Linux package management systems
- Install, update, and remove software
- Manage package repositories
- Troubleshoot dependency issues

---

## 🌅 Morning Session: Package Management Basics

### Debian/Ubuntu (apt)
```bash
# Update package lists
sudo apt update

# Upgrade all packages
sudo apt upgrade

# Search for packages
apt search package-name

# Install a package
sudo apt install package-name

# Remove a package
sudo apt remove package-name

# Remove package and config files
sudo apt purge package-name

# Clean up
sudo apt autoremove        # Remove unused dependencies
sudo apt autoclean         # Clear old package files

# Package information
apt show package-name
apt list --installed       # List all installed packages
```

### RHEL/CentOS/Rocky (yum/dnf)
```bash
# Update package lists
sudo yum update

# Install package
sudo yum install package-name

# Remove package
sudo yum remove package-name

# Search packages
yum search package-name

# Package info
yum info package-name

# List installed
yum list installed

# Note: dnf is the successor to yum
sudo dnf install package-name
```

---

## ☀️ Afternoon Session: Hands-On Practice

### Exercise 1: Essential Tools Installation
```bash
# Install development tools
sudo apt update
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    htop \
    tree \
    net-tools \
    build-essential

# Verify installations
curl --version
git --version
htop --version
```

### Exercise 2: Working with Repositories
```bash
# List repositories
apt-cache policy

# Add PPA (Ubuntu)
sudo add-apt-repository ppa:example/ppa
sudo apt update

# Add repository manually
echo "deb http://example.com/repo stable main" | sudo tee /etc/apt/sources.list.d/example.list

# Add GPG key
curl -fsSL https://example.com/gpg | sudo apt-key add -
```

### Exercise 3: Dependency Management
```bash
# Check dependencies
apt-cache depends package-name
apt-cache rdepends package-name  # Reverse dependencies

# Fix broken dependencies
sudo apt --fix-broken install

# Hold package version
sudo apt-mark hold package-name
sudo apt-mark unhold package-name
```

---

## 🌙 Evening Session: System Maintenance

### System Updates
```bash
# Safe update process
sudo apt update                    # Update package lists
apt list --upgradable              # See what will be upgraded
sudo apt upgrade                   # Upgrade packages
sudo apt dist-upgrade              # Upgrade with dependency changes
sudo apt autoremove                # Clean up

# Reboot if kernel updated
uname -r                           # Current kernel version
# Check if /var/run/reboot-required exists
ls /var/run/reboot-required
sudo reboot
```

### Troubleshooting Common Issues

**Problem**: Package conflicts
```bash
sudo dpkg --configure -a           # Configure unconfigured packages
sudo apt --fix-broken install      # Fix broken dependencies
```

**Problem**: Locked database
```bash
# Wait for other package operations to finish, or:
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo dpkg --configure -a
```

**Problem**: Disk space full
```bash
df -h                              # Check disk usage
sudo apt clean                     # Clean package cache
sudo apt autoremove                # Remove unused packages
sudo journalctl --vacuum-time=3d   # Clean old logs
```

---

## 📝 Week 1 Wrap-Up

### What We Covered
- ✅ Linux file system navigation
- ✅ File permissions and ownership
- ✅ Text processing and log analysis
- ✅ Process management
- ✅ Package management

### Prepare for Assessment
Review key commands:
- File operations: ls, cd, cp, mv, rm
- Permissions: chmod, chown
- Text processing: grep, sed, awk
- Processes: ps, top, kill
- Packages: apt install, apt update

### Weekend Challenge
1. Set up a personal Linux VM or WSL2
2. Practice all commands from this week
3. Complete Week 1 assessment
4. Review any weak areas

**Next Week: Networking & Scripting! 🌐**
