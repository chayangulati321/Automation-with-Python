from pathlib import Path

root_dir = Path('C:/Users/HP/Desktop/Material/UpSkill/Automation')

for i in range(10,11):
    filename = str(i) + '.txt'
    filepath = root_dir / Path(filename)
    filepath.touch()