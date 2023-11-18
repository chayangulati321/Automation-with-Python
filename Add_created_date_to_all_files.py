from pathlib import Path
from datetime import datetime

path = Path('C:/Users/HP/Desktop/Material/UpSkill/Automation')
stats = path.stat()
seconds_created = stats.st_ctime

date_created = datetime.fromtimestamp(seconds_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S')

root_file = path.iterdir()
for i in root_file:
    new_filename = date_created_str + '_' + i.stem + i.suffix
    print(new_filename)

    # Path.rename(new_filepath)     # use i.wit_name(new_filename) if it is in sub-folder