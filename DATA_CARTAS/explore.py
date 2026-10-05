import os

def explore():
    base = "C:/projects/NUCLEO_YUGI"
    for root, dirs, files in os.walk(base):
        for f in files:
            p = os.path.join(root, f)
            print(p)

if __name__ == "__main__":
    explore()
