from pathlib import Path

root_dir = Path('C:/Users/HP/Desktop/Material/UpSkill/Automation')

for i in root_dir.rglob('*.txt'):
    if i.is_file():
        new_file_extension = i.with_suffix('.csv')
        # i.rename(new_file_extension)

    print(new_file_extension)
