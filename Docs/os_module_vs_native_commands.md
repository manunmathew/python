| **Function** | **Python `os` Module**                  | **Windows Native Command**           | **Linux Native Command**             |
|--------------|-----------------------------------------|--------------------------------------|--------------------------------------|
| **Get Current Directory** | `os.getcwd()` gets the current working directory. | `cd` (no arguments) shows the current directory. | `pwd` prints the current working directory. |
| **List Directory Contents** | `os.listdir(path)` lists the contents of a directory. | `dir` lists the contents of a directory. | `ls` lists the contents of a directory. |
| **Create Empty File**  | `open('file.txt', 'a').close()` creates an empty file. | `type nul > file.txt` creates an empty file. | `touch file.txt` creates an empty file. |
| **Create Directory**  | `os.mkdir('new_folder')` creates a directory. | `mkdir new_folder` creates a directory. | `mkdir new_folder` creates a directory. |
| **Remove Empty Directory** | `os.rmdir('folder')` removes an empty directory. | `rmdir folder` removes an empty directory. | `rmdir folder` removes an empty directory. |
| **Remove File** | `os.remove('file.txt')` deletes a file. | `del filename` deletes a file. | `rm file.txt` deletes a file. |
| **Remove Directory and Contents** | `os.rmdir('folder')` removes a directory.<br>`shutil.rmtree('folder')` removes a directory and its contents. | `rmdir /S /Q folder` removes a directory and its contents. | `rm -r folder` removes a directory and its contents. |
| **Change Directory** | `os.chdir('new_path')` changes the current directory. | `cd new_path` changes the current directory. | `cd new_path` changes the current directory. |
| **Move or Rename File** | `os.rename('old_name', 'new_name')` renames or moves a file or directory. | `move old_name new_name` moves or renames a file or directory. | `mv old_name new_name` renames or moves a file or directory. |
| **Copy File** | `shutil.copy('source', 'destination')` copies a file. | `copy source destination` copies a file. | `cp source destination` copies a file. |
