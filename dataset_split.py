import os
from PIL import Image
import numpy as np
import random
import shutil


'''
:Breif: Clean a text file(i.e. suffix of it suppose to be '.txt')
:Author: CheasonY
:param file_name: The name of the text file which need to be cleaned(p.s. file path has to be contained here)
'''
def clean_file(file_name):
    f = open(file_name, 'w')
    f.close()


'''
:Breif: Split the original dataset to train, validation, test which follow the rate 7:2:1
:Author: CheasonY
'''
def split_data_set(path='T:/PyProjects/Garbage_Sorting/MyDatas/images/', train=20, val=6, test=3,
                   num=100, save_path='T:/PyProjects/Garbage_Sorting/MyDatas/dataset/',
                   ori_label_path='./MyDatas/annotions/',
                   label_path='./MyDatas/labels/'):
    # set a fixed seed here
    random.seed(1107)
    size = train+val+test

    # Clean all the text files need to write first
    clean_file(save_path + 'train.txt')
    clean_file(save_path + 'val.txt')
    clean_file(save_path + 'test.txt')

    # Generate the correct data files here
    for i in range(1, num+1):
        temp = [0]*size

        # train-datas here
        with open(save_path+'train.txt', 'a') as f:
            for j in range(train):
                index = random.randint(1, size)
                # Remove repeated indexes here
                while temp[index-1] != 0:
                    index = random.randint(1, size)
                # Sign the current index
                temp[index-1] = 1
                # Get File name here
                file_name = str(i)
                if index != 1:
                    index -= 1
                    if index < 10:
                        file_name += "000"+str(index)
                    else:
                        file_name += "00"+str(index)

                # Get the image file name and corresponding label-txt name
                label_name = file_name+'.txt'
                file_name += ".jpg"
                # Move corresponding labeld text file to specified storation path
                shutil.copyfile(ori_label_path + label_name, label_path + 'train/' + label_name)
                # write in
                f.write(path+file_name+'\n')

        # validation-datas here
        with open(save_path+'val.txt', 'a') as f:
            for j in range(val):
                index = random.randint(1, size)
                # Remove repeated indexes here
                while temp[index-1] != 0:
                    index = random.randint(1, size)
                # Sign the current index
                temp[index-1] = 1
                # Get File name here
                file_name = str(i)
                if index != 1:
                    index -= 1
                    if index < 10:
                        file_name += "000" + str(index)
                    else:
                        file_name += "00" + str(index)
                # Get the image file name and corresponding label-txt name
                label_name = file_name + '.txt'
                file_name += ".jpg"
                # Move corresponding labeld text file to specified storation path
                shutil.copyfile(ori_label_path + label_name, label_path + 'val/' + label_name)
                # write in
                f.write(path + file_name + '\n')

        # test-datas here
        with open(save_path+'test.txt', 'a') as f:
            for j in range(test):
                index = random.randint(1, size)
                # Remove repeated indexes here
                while temp[index-1] != 0:
                    index = random.randint(1, size)
                # Sign the current index
                temp[index-1] = 1
                # Get File name here
                file_name = str(i)
                if index != 1:
                    index -= 1
                    if index < 10:
                        file_name += "000" + str(index)
                    else:
                        file_name += "00" + str(index)
                # Get the image file name and corresponding label-txt name
                label_name = file_name + '.txt'
                file_name += ".jpg"
                # Move corresponding labeld text file to specified storation path
                shutil.copyfile(ori_label_path + label_name, label_path + 'test/' + label_name)
                # write in
                f.write(path + file_name + '\n')


if __name__ == '__main__':
    split_data_set()
