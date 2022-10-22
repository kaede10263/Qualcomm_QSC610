platform-tools\adb.exe wait-for-device
platform-tools\adb.exe push detect.py /data/misc/snpe/
platform-tools\adb.exe push data.zip /data/misc/snpe/
platform-tools\adb.exe shell rm -r /data/misc/snpe/images/
platform-tools\adb.exe shell mkdir /data/misc/snpe/images/
platform-tools\adb.exe shell 'cd /data/misc/snpe/images/; unzip ../data.zip'
platform-tools\adb.exe shell 'cd /data/misc/snpe/; python3 detect.py images inputs output result'
platform-tools\adb.exe pull /data/misc/snpe/result
platform-tools\adb.exe shell 'cd /data/misc/snpe/; rm -r detect.py data.zip images inputs result filelist.txt'
explorer.exe result
