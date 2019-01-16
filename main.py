from screenshot import card_shot
from image import crop_to_bin, binary_to_hash
from PIL import Image
import time
import os


def convert_image_to_hash(card_img):
    binary = crop_to_bin(card_img)
    hash = binary_to_hash(binary)
    # print(hash)
    return hash


def create_dict():
    hash_dict = {}
    for root, dirs, files in os.walk("bin"):
        file_names = files
    for file_name in file_names:
        hash = convert_image_to_hash(Image.open("bin/" + file_name))
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
    name = min(dist_dict, key=dist_dict.get)
    sim = dist_dict[name]
    return name, sim


def card_sequence_to_link(sequence):
    link = "http://tenhou.net/2/?q="
    for name in sequence:
        link += name
    return link


def shot_and_judge(hash_dict):
    cards = card_shot()
    card_names = []
    sims = []
    threshold = 60
    count = 0
    while count < 28:
        card = cards[count]
        card.save("test\%s.png" % str(count))
        hash = convert_image_to_hash(card)
        name, sim = judge_card_with_hash(hash_dict, hash)
        if sim < threshold:
            card_names.append(name)
            sims.append(sim)
            if count < 14:
                count = count + 1
            else:
                break
        else:
            count = count + 14
    return card_names, sims
