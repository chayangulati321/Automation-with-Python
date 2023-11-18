from pathlib import Path

root_dir = Path('C:/Users/HP/Desktop/Material/UpSkill/Automation')
root_file = root_dir.iterdir()

print(Path.cwd())
''' This will rename the file in root directory i.e., Automation

for path in root_file:
    new_filename = 'New_' + path.stem + path.suffix
    new_filepath = Path(new_filename)
    print(new_filepath)
    # Path.rename(new_filepath)
'''

# To rename file in other folder like Automation/files/filename.txt 

for path in root_file:
    new_filename = 'New_' + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    # Path.rename(new_filepath)