import requests
import shutil

from zipfile import ZipFile
from pathlib import Path

from src.updater.version import CURRENT_VERSION

repo_owner = "alekssdz123"
repo_name = "Weather-Notifier"

REPO_URL = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

def get_last_release():
    release = requests.get(REPO_URL)
    release.raise_for_status()
    return release.json()

def check_new_release():
    latest_release = get_last_release()["tag_name"]

    if CURRENT_VERSION != latest_release:
        return True
    return False

def download_repo_archive(download_url):
    response = requests.get(download_url)
    response.raise_for_status()
    archive_path = "update.zip"

    with open(archive_path, "wb") as file:
        file.write(response.content)

    return archive_path

def unpack_archive(archive_path):
    temp_dir = "temp"

    with ZipFile(archive_path) as zip_file:
        zip_file.extractall(temp_dir)
    return temp_dir

def replace_dirs(temp_dir):
    source = next(Path(temp_dir).iterdir())
    destination = Path(__file__).resolve().parent.parent.parent

    for item in source.iterdir():
        target = destination / item.name

        if ".git" in item.name:
            continue

        if item.name == "config.json":
            continue

        if item.name == ".venv":
            continue

        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
            continue
        shutil.copy2(item, target)

def delete_temp_dir(temp_dir, archive_path):
    shutil.rmtree(temp_dir)
    Path(archive_path).unlink()

def update():
    release = get_last_release()
    if release["tag_name"] != CURRENT_VERSION:
        archive_path = download_repo_archive(release["zipball_url"])
        print("Zip archive with update downloaded.")

        temp_dir = unpack_archive(archive_path)
        print("Zip archive with update unpacked.")

        replace_dirs(temp_dir)
        print("Current directory replaced with temporary directory.")

        delete_temp_dir(temp_dir, archive_path)
        print("Temporary directory removed.")
