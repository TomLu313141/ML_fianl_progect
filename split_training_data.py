import os
import random
import shutil    # 用於檔案批次處理


# Copy the list of string and replace '.jpg' to '.json'
def processList(img_list):

    label_list = []

    for i in range(0, len(img_list)):
        label_list.append(img_list[i].replace('.jpg', '.json'))

    return label_list


# Use 'copy' rather than 'move' to keep the original data

def split(src_path, ann_path, split_paths):

    random.seed(529) # split the data randomly

    # Deal with img
    img_file = os.listdir(src_path)     # type is list
    label_file = os.listdir(ann_path)
    
    train_img = random.sample(img_file, int(len(img_file) * train_percent))
    train_label = processList(train_img)


    for img, label in zip(img_file, label_file):

        # Deal with img
        if not os.path.isdir(img):
            if img in train_img:
                shutil.copy(os.path.join(src_path, img), os.path.join(split_paths[0], img))
            else:
                shutil.copy(os.path.join(src_path, img), os.path.join(split_paths[1], img))

        # Deal with label
        if not os.path.isdir(label):
            if label in train_label:
                shutil.copy(os.path.join(ann_path, label), os.path.join(split_paths[3], label))
            else:
                shutil.copy(os.path.join(ann_path, label), os.path.join(split_paths[4], label))

    
    # 上面分出 train img/train label 及 val img/val label 後
    # 需再從 val img/val label 分出 test img/test label

    val_img_path = os.listdir(split_paths[1])
    val_label_path = os.listdir(split_paths[4])

    val_img = random.sample(val_img_path, int(len(val_img_path) * val_percent))
    val_label = processList(val_img)

    for left_img in val_img_path:
        if left_img not in val_img:   # 其餘皆為 test
            shutil.copy(os.path.join(split_paths[1], left_img), os.path.join(split_paths[2], left_img))

    for left_label in val_label_path:
        if left_label not in val_label:   # 其餘皆為 test
            shutil.copy(os.path.join(split_paths[4], left_label), os.path.join(split_paths[5], left_label))


if __name__ == '__main__':
    img_path = r'/Users/apple/Desktop/Final/TrainingData/images'
    ann_path = r'/Users/apple/Desktop/Final/TrainingData/labels'    # ann for annotation

    split_path = [r'/Users/apple/Desktop/Final/split_img/train_img',
                 r'/Users/apple/Desktop/Final/split_img/val_img',
                 r'/Users/apple/Desktop/Final/split_img/test_img',
                 r'/Users/apple/Desktop/Final/split_img/train_label',
                 r'/Users/apple/Desktop/Final/split_img/val_label',
                 r'/Users/apple/Desktop/Final/split_img/test_label']


    # training : test : validation = 0.8 : 0.1 : 0.1
    train_percent = 0.8
    val_percent = 0.5    # val 佔剩下的比例

    # 若資料夾不存在，則新增之
    for path in split_path:
        if not os.path.exists(path):
            os.makedirs(path)

    split(img_path, ann_path, split_path)

