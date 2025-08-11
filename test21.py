

import os
import json
import csv
import shutil

# -------------------------
# TEXT FILE HANDLING
# -------------------------

def write_to_file(filename, content):
    """Write text to file (overwrite)."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written to {filename}")

def read_file(filename):
    """Read entire file."""
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    print(f"Contents of {filename}:\n{data}")
    return data

def append_to_file(filename, content):
    """Append text to file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)
    print(f"Appended to {filename}")

def read_lines(filename):
    """Read file line by line."""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

# -------------------------
# JSON FILE HANDLING
# -------------------------

def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"JSON written to {filename}")

def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"JSON read from {filename}: {data}")
    return data

# -------------------------
# CSV FILE HANDLING
# -------------------------

def write_csv(filename, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"CSV written to {filename}")

def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# -------------------------
# BINARY FILE HANDLING
# -------------------------

def write_binary(filename, data_bytes):
    with open(filename, "wb") as f:
        f.write(data_bytes)
    print(f"Binary data written to {filename}")

def read_binary(filename):
    with open(filename, "rb") as f:
        data = f.read()
    print(f"Read {len(data)} bytes from {filename}")
    return data

# -------------------------
# FILE & DIRECTORY MANAGEMENT
# -------------------------

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted.")
    else:
        print(f"{filename} does not exist.")

def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed {old_name} → {new_name}")
    else:
        print(f"{old_name} does not exist.")

def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied {src} → {dest}")

def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Moved {src} → {dest}")

def list_directory(path="."):
    files = os.listdir(path)
    print(f"Contents of '{path}': {files}")
    return files

def traverse_directory(path="."):
    for root, dirs, files in os.walk(path):
        print(f"\nDirectory: {root}")
        for d in dirs:
            print(f"  [DIR]  {d}")
        for f in files:
            print(f"  [FILE] {f}")

# -------------------------
# CONTEXT MANAGER TRICKS
# -------------------------

class FileHandler:
    """Custom context manager for file operations."""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"Error: {exc_val}")
        return True  # Suppress exceptions for demo purposes

# -------------------------
# DEMO USAGE
# -------------------------

if __name__ == "__main__":
    # Text file
    write_to_file("example.txt", "Hello, World!\n")
    append_to_file("example.txt", "Appended line.\n")
    read_file("example.txt")
    read_lines("example.txt")

    # JSON file
    sample_json = {"name": "Vishwesh", "role": "Developer"}
    write_json("data.json", sample_json)
    read_json("data.json")

    # CSV file
    sample_csv = [["Name", "Role"], ["Vishwesh", "Developer"], ["Alice", "Tester"]]
    write_csv("data.csv", sample_csv)
    read_csv("data.csv")

    # Binary file
    write_binary("data.bin", b'\xDE\xAD\xBE\xEF')
    read_binary("data.bin")

    # File operations
    rename_file("example.txt", "renamed_example.txt")
    copy_file("renamed_example.txt", "copy_example.txt")
    move_file("copy_example.txt", "moved_example.txt")
    list_directory()
    traverse_directory(".")

    # Using custom context manager
    with FileHandler("context_demo.txt", "w") as f:
        f.write("This is written using a custom context manager.\n")

    # Cleanup
    delete_file("renamed_example.txt")
    delete_file("moved_example.txt")
    delete_file("data.json")
    delete_file("data.csv")
    delete_file("data.bin")
    delete_file("context_demo.txt")
