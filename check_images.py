from PIL import Image
from tqdm import tqdm
import os, shutil, win32file

################################
#   Check the downloaded images
#   if error, delete it
################################

def is_used(file_name):
    try:
        vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
        return int(vHandle) == win32file.INVALID_HANDLE_VALUE
    except:
        return True
    finally:
        try:
            win32file.CloseHandle(vHandle)
        except:
            pass

if __name__ == "__main__" :
    bar_format = '{desc}{percentage:3.0f}%|{bar}|{n_fmt}/{total_fmt}[{elapsed}<{remaining}{postfix}]'
    with tqdm(total=len(os.listdir('images')), bar_format = bar_format) as pbar:
        i = 0
        pbar.set_description('{}'.format("Check imgs"))
        for img in os.listdir('images'):
            try:
                Image.open(os.path.join('images', img)).convert('RGB')
            except:
                if not is_used(os.path.join('images', img)):
                    shutil.move(os.path.join('images', img),os.path.join('err_images', img))
                    i += 1
                pbar.set_postfix(Total_err_imgs = i)
            pbar.update(1)