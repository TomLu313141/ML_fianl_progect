import os

json_folder = r"/Users/apple/Desktop/test/"
#  獲取資料夾內的檔名
FileNameList = os.listdir(json_folder)
#  啟用labelme環境
os.system("activate labelme")
for i in range(len(FileNameList)):
    #  判斷當前檔案是否為json檔案
    if(os.path.splitext(FileNameList[i])[1] == ".json"):
        json_file = json_folder + "\\" + FileNameList[i]
        #  將該json檔案轉為png
        os.system("labelme_json_to_dataset " + json_file)

import shutil

JPG_folder = r"/Users/apple/Desktop/test/"
Paste_JPG_folder = r"/Users/apple/Desktop/test/image"
Paste_label_folder = r"/Users/apple/Desktop/test/label"
#  獲取資料夾內的檔名
FileNameList = os.listdir(JPG_folder)
NewFileName = 1
for i in range(len(FileNameList)):
    #  判斷當前檔案是否為json檔案
    if(os.path.splitext(FileNameList[i])[1] == ".jpg"):

        #  複製jpg檔案
        JPG_file = JPG_folder + "\\" + FileNameList[i]
        new_JPG_file = Paste_JPG_folder + "\\" + str(NewFileName) + ".jpg"
        shutil.copyfile(JPG_file, new_JPG_file)

        #  複製label檔案
        jpg_file_name = FileNameList[i].split(".", 1)[0]
        label_file = JPG_folder + "\\" + jpg_file_name + "_json\\label.png"
        new_label_file = Paste_label_folder + "\\" + str(NewFileName) + ".png"
        shutil.copyfile(label_file, new_label_file)

        #  檔案序列名+1
        NewFileName = NewFileName + 1