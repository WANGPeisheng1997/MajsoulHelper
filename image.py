def image_gray(img):
    return img.convert('L')


def image_binary(gray_img, threshold=200):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    binary = gray_img.point(table, '1')
    return binary


def calculate_average_gray(gray_img):
    total = 0
    pixels = gray_img.getdata()
    for pixel in pixels:
            total += pixel
    return int(total / len(pixels))


def binary_to_hash(bin_img):
    pixels = bin_img.getdata()
    hash = ""
    for pixel in pixels:
        hash += str(pixel)
    return hash


def crop_to_bin(crop):
    gray_img = image_gray(crop)
    resize_width = 16
    resize_height = 23
    smaller_image = gray_img.resize((resize_width, resize_height))
    threshold = calculate_average_gray(smaller_image)
    binary = image_binary(smaller_image, threshold)
    return binary
