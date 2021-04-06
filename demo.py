from rake_nltk import Rake
import re
# file = open(r"C:\Users\TJava07\Project\demo_data\ExampleHadoop\Input\example.txt")
# line = file.read().replace("\n", " ")
# file.close()
with open("C:\\Users\\TJava07\\Project\\Files\\TextData.txt", "r") as f:
    j = f.read()
    print(j)
    for i in j:
        j = re.split('\t', j)
        # k = j.read()
        print(j)
        res = [j[k] for k in range(len(j)) if k % 2 != 0]
        print(res)
        for data in res:
            print(data)
            with open(data, 'r') as rg:
                p = rg.read()
                # print(p)

                r = Rake()
                r.extract_keywords_from_text(p)
                g = r.get_ranked_phrases()[0:5]
                print(g)

