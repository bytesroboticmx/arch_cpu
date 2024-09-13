import sys

def main():
    if sys.maxsize == 0xFFFFFFFF:
        print("32 bit")
    elif sys.maxsize == 0xFFFFFFFFFFFFFFFF:
        print("64 bit")
    else:
        print("Unknown")

if __name__ == "__main__":
    main()
