# -*- coding: utf-8 -*-
from PIL import Image
import os, time,csv
import imagehash
from HashResearch.TestHashSimilarity.examination_sad import make_list

def hamming_distance(string1, string2):
    # See: http://en.wikipedia.org/wiki/Hamming_distance
    diffs = 0
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            diffs += 1
    return diffs

def is_similar(image_path1, image_path2):
    """
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    import imagehash

    hash1 = imagehash.phash(image1
    ,hash_size=16)
    hash2 = imagehash.phash(image2,hash_size=16)
    """
    distance = hamming_distance(list(str(image_path1)), list(str(image_path2)))
    value = float(100 - ((100 / 16) * distance))

    return value

def readlist(lineEdit_2,n):

    grouping_list = []
    csvfile = open( lineEdit_2+'\\egg2.csv', 'r')

    csv_reader = csv.DictReader(csvfile)
    for rows in csv_reader:
        if rows["grouping"] == str(n):
            grouping_list.append(rows["photoname"])

    return grouping_list


def doRathernext(lineEdit,lineEdit_2):
    if 1:
        csvfile = open(lineEdit_2 + '\\test_list.csv', 'a+')
        csvfile.write("photo_path_one,photo_path_two,phash_16,phash_32,phash_64,dhash_16,dhash_32,dhash_64\n")
        n = 1
        csvfile.close()
        while 1:
            photoPath_list = readlist(lineEdit_2, n)
            if len(photoPath_list) != 0:
                n = n + 1
                m = 0

                print(photoPath_list)
                while m <= len(photoPath_list) - 1:
                    l = m + 1

                    while l <= len(photoPath_list) - 1:
                        print(photoPath_list[m],photoPath_list[l])
                        photo_path_one = Image.open(lineEdit + "\\" +photoPath_list[m])
                        photo_path_two = Image.open(lineEdit + "\\"+photoPath_list[l])
                        hashs1 = imagehash.phash(photo_path_one, hash_size=16)
                        hashs2 = imagehash.phash(photo_path_two, hash_size=16)
                        hashs1_1 = imagehash.phash(photo_path_one, hash_size=32)
                        hashs2_1 = imagehash.phash(photo_path_two, hash_size=32)
                        hashs1_2 = imagehash.phash(photo_path_one, hash_size=64)
                        hashs2_2 = imagehash.phash(photo_path_two, hash_size=64)

                        true_value_1 = is_similar(hashs1, hashs2)
                        true_value_2 = is_similar(hashs1_1, hashs2_1)
                        true_value_3 = is_similar(hashs1_2, hashs2_2)

                        dhashs1 = imagehash.dhash(photo_path_one, hash_size=16)
                        dhashs2 = imagehash.dhash(photo_path_two, hash_size=16)
                        dhashs1_1 = imagehash.dhash(photo_path_one, hash_size=32)
                        dhashs2_1 = imagehash.dhash(photo_path_two, hash_size=32)
                        dhashs1_2 = imagehash.dhash(photo_path_one, hash_size=64)
                        dhashs2_2 = imagehash.dhash(photo_path_two, hash_size=64)

                        true_value_1d = is_similar(dhashs1, dhashs2)
                        true_value_2d = is_similar(dhashs1_1, dhashs2_1)
                        true_value_3d = is_similar(dhashs1_2, dhashs2_2)

                        photo_path_one.close()
                        photo_path_two.close()
                        csvfile = open(lineEdit_2 + '\\' + 'test_list.csv', 'a+')
                        csvfile.write(photoPath_list[m] + "," + photoPath_list[l] + "," + str(true_value_1) + "," +str(true_value_2) + "," + str(true_value_3) + "," + str(true_value_1d) + "," +str(true_value_2d) + "," + str(true_value_3d) + "\n")
                        l = l + 1
                        csvfile.close()
                    m = m + 1
            else:
               return
    else:
        return

if __name__ == '__main__':
    lineEdit = "j:\\50to100"
    lineEdit_2 = "j:\\csvdoing-1"
    make_list.main(lineEdit,lineEdit_2)
    doRathernext(lineEdit,lineEdit_2)


