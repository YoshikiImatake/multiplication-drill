import random

point = 0
print ('かけ算ドリルを開始します。（全10問）')
for i in range(10):
    x = random.randint(1,9)
    y = random.randint(1,9)
    question = ('({}):{}x{}=').format(i,x,y)
    ans = input(question)
    if int(ans) == x*y:
        print('〇')
        point += 1
    else:
        print(('x　正解は:{}×{}={}').format(x,y,x*y))

print(('正解率は{}％です。').format(point/10 *100))