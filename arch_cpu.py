import sys

def main():
    if sys.maxsize == 0x7FFFFFFF:
        print("32 bit")
    elif sys.maxsize == 0x7FFFFFFFFFFFFFFF:
        print("64 bit")
    else:
        print("ARM/64bits")

if __name__ == "__main__":
    main()
