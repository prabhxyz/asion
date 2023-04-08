from PIL import Image, ExifTags

def get_metadata():
    img = Image.open("../ml/input/image.jpg")
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    return exif

if __name__ == "__main__":
    metadata = get_metadata()
    for tags in metadata:
        print(f"{tags}: {metadata[tags]}")