import requests
import json
import os
import shutil

def fetch_repos(username):
    """
    Fetch list of public repositories for a GitHub user
    """
    url = f"https://api.github.com/users/{username}/repos"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()     
        return response.json()

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        return None


def save_to_json(data, folder):
    """
    Save API data into repos.json inside backup folder
    """
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, "repos.json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Repository data saved:", path)


def create_archive(folder):
    """
    Compress the backup folder
    """
    shutil.make_archive("backup_archive", "zip", folder)
    print("Backup archive created: backup_archive.zip")


def main():
    print("\n------ GitHub Repo Backup Tool ------")
    user = input("Enter GitHub username: ").strip()
    
    data = fetch_repos(user)

    if not data:
        print("No data fetched. Exiting.")
        return

    backup_folder = "backup_data"

    save_to_json(data, backup_folder)
    create_archive(backup_folder)

    print("\nBackup completed successfully!")

if __name__ == "__main__":
    main()
