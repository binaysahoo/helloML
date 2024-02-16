Certainly! Here's an example using Python with the `asyncio` library for asynchronous operations:

```python
import os
import asyncio
from pathlib import Path

async def remove_directory(directory):
    full_path = Path(directory)
    try:
        os.rmdir(full_path)
        print(f"Removed directory: {full_path}")
    except Exception as e:
        print(f"Failed to remove directory {full_path}: {e}")

async def process_directories(dir_path, directories_to_keep):
    for directory in os.listdir(dir_path):
        full_path = Path(dir_path) / directory
        if full_path.is_dir() and directory not in directories_to_keep:
            await remove_directory(full_path)

async def main():
    dir_path = '/path/to/directories'
    directories_to_keep = sorted(os.listdir(dir_path), key=lambda x: os.path.getmtime(os.path.join(dir_path, x)), reverse=True)[:3]

    await process_directories(dir_path, directories_to_keep)

if __name__ == "__main__":
    asyncio.run(main())
```

This Python script utilizes the `asyncio` library to perform asynchronous directory removal. It defines an asynchronous function `remove_directory` to handle the removal of a directory and another function `process_directories` to iterate through directories asynchronously. The `main` function sets up the directory path and directories to keep, then calls the asynchronous processing function.

Note: Ensure that you have the necessary permissions to remove directories, and replace `'/path/to/directories'` with the actual path to your directories.
