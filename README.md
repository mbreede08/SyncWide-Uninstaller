# SyncWide Uninstaller 🔄  

The **SyncWide Uninstaller** is your go-to solution for rolling back changes made by SyncWide installations or configurations. Designed for efficiency and simplicity, this script will revert your server to its pre-SyncWide state by uninstalling and cleaning up modifications.  

---

## Features ✨  
- 🔹 Removes SyncWide-installed software packages, including:  
  - Apache  
  - Nginx  
  - Python  
  - NodeJS  
  - PHP  
  - MySQL  
  - MongoDB  
  - PostgreSQL  
  - SQLite  
- 🔹 Clears SyncWide-specific configuration files.  
- 🔹 Rolls back any system environment changes.  
- 🔹 Verifies cleanup to ensure no residual files remain.  

---

## Usage 📚  

### Step 1: Clone the Repository  
To get started, clone the repository:  
```bash  
git clone https://github.com/SyncWide-Solutions/SyncWide-Uninstaller.git  
cd SyncWide-Uninstaller  
```  

### Step 2: Run the Script  
Make the script executable and run it:  
```bash  
chmod +x syncwide-uninstaller.sh  
sudo ./syncwide-uninstaller.sh  
```

###Step 3: Follow On-Screen Prompts  
The uninstaller will guide you through its process. Confirm actions as necessary.  

---

## Compatibility 🖥️  
- Works with Ubuntu and Debian-based operating systems.  
- Requires sudo (root) permissions for uninstallation tasks.  

---

## Caution ⚠️  
- Ensure you’ve backed up all important data before running the uninstaller, as it will remove files and configurations!  
- If certain software or configurations weren’t installed through SyncWide, they will remain untouched.  

---

## Support 💬  
Encounter an [issue](https://github.com/SyncWide-Solutions/SyncWide-Uninstaller/issues)? Open an Issue on GitHub, or email us at [info@syncwi.de](mailto://info@syncwi.de).  

---

## License 📜  
This project is licensed under the MIT License.  
Feel free to use, modify, and distribute, but credit to the original creator is appreciated!  

---

### Let’s keep your system clean and optimized! 🚀
