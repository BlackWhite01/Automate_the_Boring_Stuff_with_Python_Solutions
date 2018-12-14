
def smoke(spam):
    output = ""
    for i in range(len(spam)):
        if i == len(spam) - 1:
            output += spam[i]
        else:
            output += spam[i]+", "
    print(output)


spam = ['apples', 'bananas', 'tofu', 'cats']
smoke(spam)