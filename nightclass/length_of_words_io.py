
with open('lorem_ipsum.txt', 'r') as c:
    k = str(c.read())
    m = k.split(" ")
    count = {}


    for i in m:
        count[i] = count.get(i, 0) + 1
    words = count.values

    for i in sorted(words, key=len):
        for words in sorted(count, key=len):
            print(words, count[words])
    #print(count)

    #print((len(i)))
    #k.split(' ')


    #m = k(max(len(n)))
        #for phones in sorted(released, key=len):
         #   print
          #  phones, released[phones]

    #