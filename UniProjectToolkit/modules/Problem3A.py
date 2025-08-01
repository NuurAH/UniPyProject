def fileLine(fileOf):
    interest = open(fileOf, "rt")
    length = len(interest.readlines())
    print("Lines", length)
    interest.close()

if __name__ == "__main__":
    fileOf = "file_of_interest"
    fileLine(fileOf)