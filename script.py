import os
import requests

PAGE_ID = os.environ["PAGE_ID"]
ACCESS_TOKEN = os.environ["FB_TOKEN"]

IMAGE_FOLDER = "images"
COUNTER_FILE = "counter.txt"

def get_index():
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def save_index(i):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(i))

def post_image(i):
    image_path = os.path.join(IMAGE_FOLDER, f"{i}.png")

    if not os.path.exists(image_path):
        print("No more images.")
        return

    caption = f"#free_{i}"

    url = f"https://graph.facebook.com/{PAGE_ID}/photos"

    data = {
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    files = {
        "source": open(image_path, "rb")
    }

    r = requests.post(url, data=data, files=files)
    print(r.json())

    save_index(i + 1)

if __name__ == "__main__":
    i = get_index()
    post_image(i)
