import re
import os

g = os.walk('./images')

for path,dir_list,file_list in g:
    for file_name in file_list:
        with open(os.path.join('./images',file_name), 'r+') as f:
            if file_name[-1] <= '9' and file_name[-1] >='0':
                os.rename(os.path.join('./images',file_name), os.path.join('./images',file_name+'.png'))
            # content = f.read()
            # print(file_name, len(content))
            # content = content.replace(r'http://cdn.sshpark.com.cn/', '../images/')
            # content = re.sub('(?<=../images/).*?(?="|\))', lambda m: m.group(0) + '.png', content)
            # f.seek(0)
            # f.truncate()
            # f.write(content)