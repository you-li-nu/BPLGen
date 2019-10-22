def main():
    train_file = "bplgen_train.csv"
    test_file = "bplgen_test.csv"
    verify_file = "bplgen_verify.csv"
    with open(train_file, 'w') as trainfile:
        with open(test_file, 'w') as testfile:
            with open(verify_file, 'w') as verifyfile:
                for i in range(1, 51):
                    filename = "./" + str(i) + ".csv"
                    infile = open(filename, 'r')
                    for i in range(2000):
                        line = infile.readline()
                        trainfile.write(line)
                    for i in range(500):
                        line = infile.readline()
                        testfile.write(line)  
                    for i in range(500):
                        line = infile.readline()
                        verifyfile.write(line)
                    infile.close()


if __name__== "__main__":
    main()