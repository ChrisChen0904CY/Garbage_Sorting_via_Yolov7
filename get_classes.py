def classes(class_file='./MyDatas/classes.txt'):
    ans = []
    with open(class_file, 'r') as f:
        for line in f.readlines():
            ans.append(line.strip())
    return ans


if __name__ == '__main__':
    class_names = classes()
    print(class_names)
