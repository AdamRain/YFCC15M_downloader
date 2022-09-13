@echo off
set num_of_process=30
for /l %%i in (1,1,%%num_of_process) do (
    start cmd /k "cd /[YOUR LOCAL DRIVE] [YOUR DIR for DATASET]&&wget -i new_urls_split_%%i.txt --rejected-log download_%%i.log -P ./images/ --no-check-certificate -t 3 -T 10 -nc -nv -c -o url_%%i.log"
)
