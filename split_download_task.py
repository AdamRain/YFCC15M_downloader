import pandas as pd
from tqdm.autonotebook import tqdm

dataframe = pd.read_json('./yfcc15m_clean_open_data.json', lines=True)

i = 1
num = 0
total_len = len(dataframe)
num_of_process = 30  # how many process you want to open simultaneously

for row in tqdm(dataframe.itertuples()):
    with open("new_urls_split_{}.txt".format(i),"a") as file:
        file.write(getattr(row, 'url'))
        file.write("\n")
        num += 1
    if num%(total_len//num_of_process) == 0:
        print("file_{} finished!".format(i))
        i += 1