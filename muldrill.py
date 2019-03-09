import random

print ('かけ算ドリルを開始します。（全10問）')
for i in range(10):
    x = random.randint(1,9)
    y = random.randint(1,9)
    question = ('({}):{}x{}=').format(i,x,y)
    ans = input(question)
    if int(ans) == x*y:
        print('〇')
    else:
        print('×　正解は:', question, x*y)
