def main():
    for i in range(1, 10):
        k = 0
        for j in range(1, 10 - i): print(" ", end="")
        for j in range(0, i):
            k += 1
            print(k, end="")
        for j in range(0, i - 1):
            k -= 1
            print(k, end="")
        print()

if __name__ == '__main__':
    main()


