import re
import os

g = os.walk('./_posts')

for path,dir_list,file_list in g:
    for file_name in file_list:
        with open(os.path.join('./_posts',file_name), 'r+') as f:
            content = f.read()
            print(file_name, len(content))
            content = content.replace(r'http://cdn.sshpark.com.cn/', '../images/')
            content = re.sub('(?<=../images/).*?(?="|\))', lambda m: m.group(0) + '.png', content)
            f.seek(0)
            f.truncate()
            f.write(content)