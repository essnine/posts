import json
import os
import pathlib
import sqlite3


def load_posts_into_db():
    curdir_path = os.path.abspath(os.path.curdir)
    posts_dir = pathlib.Path(curdir_path).parent
    for child in posts_dir.iterdir():
        if child.is_dir() or child.name.startswith("."):
            continue
        print(child)
    ...


def main():
    ...


if __name__ == "__main__":
    main()
