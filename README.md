# 📦 GitHub Repo Backup Tool

The **GitHub Repo Backup Tool** is a Python automation script that fetches public repositories of any GitHub user via the GitHub REST API, saves the data in JSON format, organizes backups using the OS module, and compresses the backup using `shutil`. The tool includes basic error handling for reliable API and file operations.

---

## 🚀 Features
- Fetch repository data via GitHub API (GET requests)
- Save repository details into a JSON file
- Automatic folder creation for backups
- ZIP archive generation using `shutil`
- Error handling for API and network issues
- Simple command-line interface

---

## 🛠️ Technologies Used
- Python 3
- Requests library
- JSON module
- OS module
- Shutil module

---

## 📁 Project Structure
GitHub-Repo-Backup-Tool/
├── main.py
├── README.md
├── backup_data/
│ └── repos.json
└── backup_archive.zip

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GitHub-Repo-Backup-Tool.git
cd GitHub-Repo-Backup-Tool

2. Install dependencies:
pip install requests

---

## ▶️ Usage

Run the script:

```bash
python main.py

---

## ✅ Example Output
Enter GitHub username: torvalds
Repository data saved: backup_data/repos.json
Backup archive created: backup_archive.zip
Backup completed successfully!


---

## 💡 Learning Objectives

This project demonstrates:

- API integration using Python  
- JSON data handling  
- File system automation  
- Error handling with exceptions  
- Backup and archiving techniques  

---

## 📌 Future Improvements

- GitHub authentication for private repositories  
- Clone repositories into backups  
- GUI interface  
- Scheduled automatic backups  

---

## 👨‍💻 Author

**Ayush Ashwani Jaiswal**

