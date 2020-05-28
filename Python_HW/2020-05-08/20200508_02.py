def main():
    print("********************************")


a = 0
b = 0
summary = 0
# main()
for i in range(2, 10):
    a = i
    main()
    for j in range(1, 10):
        b = j
        summary = i*j
        print(" %d * %d = %d " % (i, j, summary))
main()
