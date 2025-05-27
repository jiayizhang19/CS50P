def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    print(f"{au} AU is {convert(au)} m")


def convert(n):
    if not isinstance(n ,(int, float)):
        raise TypeError("au must be an integer or float")
    return n * 149597870700
    # without above if statement, the below code won't return a TypeError as we expected, as string can do multiplication as well.
    # return n * 4 
        
    
if __name__ == "__main__":
    main()
    # print(convert("cat"))