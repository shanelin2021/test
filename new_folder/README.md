# File System Tool

A Python-based file system abstraction that provides convenient functions for directory and file operations with built-in name collision detection.

## Features

- **List Directory Contents**: `ls()` - Get all files and directories in a path
- **Create Directory**: `mkdir(parent_path, dir_name)` - Create new directories
- **Create Files**: `create_file(parent_path, file_name, content)` - Create new files
- **Read Files**: `read_file(file_path)` - Read file contents
- **Write Files**: `write_file(file_path, content)` - Write content to files
- **Search**: `search(query, search_path)` - Search for files and directories
- **Name Collision Protection**: Prevents files and directories from having the same name in the same directory

## Usage

```python
from filesystem import FileSystem

# Initialize with root directory
fs = FileSystem(".")

# List directory contents
items = fs.ls("/")  # Get files and directories
print(f"Files: {items['files']}")
print(f"Directories: {items['directories']}")

# Create a new directory
new_dir = fs.mkdir("/", "my_directory")

# Create a file
new_file = fs.create_file("my_directory", "my_file.txt", "Hello, World!")

# Read a file
content = fs.read_file("my_directory/my_file.txt")
print(content)

# Search for files
results = fs.search("my", "/")
```

## Function Examples

### ls(path)
```python
# List root directory
items = fs.ls("/")  # Returns {'files': [...], 'directories': [...]}
```

### mkdir(parent_path, dir_name)
```python
# Create directory in root
dir_path = fs.mkdir("/", "new_folder")

# Create subdirectory
subdir = fs.mkdir("new_folder", "child")
```

### create_file(parent_path, file_name, content)
```python
# Create file in root
file_path = fs.create_file("/", "data.txt", "File content")

# Create file in subdirectory
subfile = fs.create_file("new_folder", "info.txt", "Info here")
```

### read_file(file_path)
```python
# Read file content
content = fs.read_file("data.txt")
```

### search(query, search_path)
```python
# Search for all files containing 'test'
results = fs.search("test", "/")
```

## Name Collision Protection

The tool enforces that **files and directories cannot have the same name in the same directory**.

**Example:**
```python
# If 'my_dir' directory exists
fs.mkdir("/", "my_dir")

# This will raise an error:
# ValueError: Cannot create file 'my_dir': a directory with this name already exists
fs.create_file("/", "my_dir", "content")
```

## Run the Demo

```bash
cd new_folder
python3 demo.py
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)


