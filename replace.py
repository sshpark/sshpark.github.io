import re
import sys
import os

# g = os.walk('./_posts')

# for path,dir_list,file_list in g:
    # for file_name in file_list:
    #     with open(os.path.join('./_posts',file_name), 'r+') as f:
file_name = sys.argv[1]
with open(os.path.join(file_name), 'r+') as f:
    content = f.read()
    print(file_name, len(content))
    content = re.sub('(?<=\().*?(?=/images)', 'http://sshpark.github.io', content)
    f.seek(0)
    f.truncate()
    f.write(content)