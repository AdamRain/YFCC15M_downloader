# YFCC15M_downloader
A subset of YFCC100M. Tools, checking scripts and links of web drive to download datasets.

---

We followed the dataset preparing process of [DeCLIP](https://github.com/Sense-GVT/DeCLIP) at 
[here](https://github.com/Sense-GVT/DeCLIP/blob/main/docs/dataset_prepare.md#prepare-datasets).

1. First Download DeCLIP's YFCC15M label file **'yfcc15m_clean_open_data.json'** at [Google Driver](https://drive.google.com/file/d/1P-2_dHNc_c5XMY0A-89iNF5Cz_Y_Cfsy/view?usp=sharing).
2. Extract the url from json file and split into several url list files for download using **split_download_task.py**.
3. Crawl the image by the url dirctely using **auto_download.bat** (Here we use [Wget](https://eternallybored.org/misc/wget/), you may need to install that). The bat file is for Windows, you may need to rewrite a shell file if using linux. Or, simply download form links below! (In process of organizing, perhaps dividing into several zip packages. Will update sooooon!)
    - If something wrong, you can stop the process and start over afterwards, Wget will skip the downloaded files and clean log files.
    - The error will be recorded in log files. Before re-start download, it is recommend to run **clean_err_file_from_logs.py** to filter and delete the wrong files.
4. Check the downloaded images using **check_images.py**.

---
Dataset infos:

- The dataset should contains 15,388,848 images.
- We managed to crawl xxxx of them.
- Total space occupied: XXXX G.

Web Drive links: (todo)

original: [yfcc15m_clean_open_data.json]()

our: [data(all in one file)](), filtered meta file (all in one file): [yfcc15m_clean.json]()

our: [data(splited packages)](), filtered meta file (splited files): [jsons]()

---
