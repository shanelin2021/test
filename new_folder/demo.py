"""
Demo of the File System Tool
Demonstrates all functionality
"""

from filesystem import FileSystem


def demo():
    """Demonstrate the file system operations"""
    print("=" * 60)
    print("FILE SYSTEM TOOL DEMO")
    print("=" * 60)
    
    # Initialize file system with current directory as root
    fs = FileSystem(".")
    
    # 1. List root directory
    print("\n1. Listing root directory (/):")
    items = fs.ls("/")
    print(f"   Files: {items['files']}")
    print(f"   Directories: {items['directories']}")
    
    # 2. Create a new directory
    print("\n2. Creating new directories:")
    try:
        dir_path = fs.mkdir("/", "demo_dir")
        print(f"   Created directory: {dir_path}")
        
        # Create a subdirectory
        subdir_path = fs.mkdir("demo_dir", "sub_dir")
        print(f"   Created subdirectory: {subdir_path}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # 3. Create a file
    print("\n3. Creating files:")
    try:
        file_path = fs.create_file("/", "demo_file.txt", "Hello, World!\nThis is a demo file.")
        print(f"   Created file: {file_path}")
        
        # Create file in subdirectory
        subfile_path = fs.create_file("demo_dir", "sub_file.txt", "Content in subdirectory")
        print(f"   Created file: {subfile_path}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # 4. List directory with new items
    print("\n4. Listing root directory after creating items:")
    items = fs.ls("/")
    print(f"   Files: {items['files']}")
    print(f"   Directories: {items['directories']}")
    
    # 5. Read a file
    print("\n5. Reading file content:")
    try:
        content = fs.read_file("demo_file.txt")
        print(f"   Content of demo_file.txt:")
        print(f"   {repr(content)}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # 6. List subdirectory
    print("\n6. Listing subdirectory:")
    try:
        items = fs.ls("demo_dir")
        print(f"   Files: {items['files']}")
        print(f"   Directories: {items['directories']}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # 7. Search for files
    print("\n7. Searching for files containing 'demo':")
    results = fs.search("demo", "/")
    print(f"   Found {len(results)} items: {results}")
    
    # 8. Test name collision detection
    print("\n8. Testing name collision detection:")
    try:
        # Try to create a file with same name as directory
        fs.create_file("demo_dir", "sub_dir", "This should fail")
        print("   ERROR: Name collision not detected!")
    except ValueError as e:
        print(f"   ✓ Properly caught collision: {e}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    demo()


