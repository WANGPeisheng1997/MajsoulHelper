from screenshot import card_shot
from image import crop_to_bin, binary_to_hash
from PIL import Image
import time
import os


def convert(card_img):
    binary = crop_to_bin(card_img)
    hash = binary_to_hash(binary)
    # print(hash)
    return hash


def create_dict():
    hash_dict = {}
    for root, dirs, files in os.walk("bin"):
        file_names = files
    for file_name in file_names:
        hash = convert(Image.open("bin/" + file_name))
        hash_dict[file_name[:-4]] = hash
    return hash_dict


def hamming_distance_with_hash(hash1, hash2):
    difference = (int(hash1, 2)) ^ (int(hash2, 2))
    return bin(difference).count("1")


def judge_card_with_hash(hash_dict, hash):
    dist_dict = {}
    for card_name in hash_dict:
        dist = hamming_distance_with_hash(hash, hash_dict[card_name])
        # print("%s, %d" % (card_name, dist))
        dist_dict[card_name] = dist
    return min(dist_dict, key=dist_dict.get)


def card_sequence_to_link(sequence):
    link = "http://tenhou.net/2/?q="
    for name in sequence:
        link += name
    return link


def grab():
    hash_dict = create_dict()
    time.sleep(3)
    cards = card_shot()
    count = 0
    card_names = []
    for card in cards:
        card.save("test\%s.png" % str(count))
        count = count + 1
        hash = convert(card)
        card_names.append(judge_card_with_hash(hash_dict, hash))
    return card_names


names = grab()
link = card_sequence_to_link(names)
print(link)
/x