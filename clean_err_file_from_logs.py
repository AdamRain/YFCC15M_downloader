import re,os
from tqdm import tqdm
from PIL import Image

reg = re.compile(r'URL:http://10\.0\.1\.165/.*$')
# You may change the regex patten to fit your error logs. Here in my case, the error under my Internet environment is 
# ```
# 2022-09-13 14:57:26 URL:http://10.0.1.165/ [3783/3783] -> "./images/3137289417_d161d3b9c2.jpg" [1]
# ```
# when the internet access (sometimes) cut off but the Wget still can get image from login page.

num_of_logs = 31 # 1 to 30
for i in tqdm(range(1,num_of_logs,1), position=0, desc="File", leave=False, colour='green', ncols=80):
    with open("url_{}.log".format(i),"r") as file:
        for line in tqdm(file, position=0, desc="line", leave=False, colour='red', ncols=80):
            match = reg.search(line)
            if match:
                del_file_name = match.string.split(' ')[-2].replace('\"','')
                try:
                    Image.open(del_file_name).convert('RGB')
                except:
                    os.remove(del_file_name)
