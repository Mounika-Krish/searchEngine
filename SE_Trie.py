from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.file = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, fileName):
        key = key.lower()
        pCrawl = self.root
        for i in range(len(key)):
            index = ord(key[i]) - ord('a')
            if pCrawl.children[index] is None:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True
        if fileName not in pCrawl.file:
            pCrawl.file[fileName] = 1
        else:
            pCrawl.file[fileName] += 1

    def search(self, key):
        key = key.lower()
        pCrawl = self.root
        for i in key:
            index = ord(i) - 97
            if pCrawl.children[index] is None:
                return False
            pCrawl = pCrawl.children[index]
        if pCrawl.isEndOfWord is False:
            return False
        return pCrawl.file


def preProcessing(text):
    punctuation = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '>', '.', '/', '?', '@', '#',
                   '$', '%', '^', '&', '*', '_', '~']
    for character in text:
        if character in punctuation:
            text = text.replace(character, " ")
    textTokens = word_tokenize(text)
    tokenWithoutStop = [j for j in textTokens if not j in stopwords.words()]
    return tokenWithoutStop


file1 = open("MyBook")
file2 = open("Himalayas")
file3 = open("Hill station")

fileList = [file1, file2, file3]

invertedIndex = Trie()
for i in fileList:
    readFile = i.read()
    ProcessedFile = preProcessing(readFile)
    for words in ProcessedFile:
        invertedIndex.insert(words, i.name)

search = input("Enter the sentence to be searched : ")
outputList = {}
flag=1
processedText = preProcessing(search)
for i in processedText:
    query = invertedIndex.search(i)
    if query is not False:
        if len(outputList)!=0:
            copy=outputList.copy()
            for j in copy:
                if j in query:
                    outputList[j]=max(outputList[j],query[j])
                else:
                    del outputList[j]
                    if len(outputList)==0:
                        flag=0
                        break
        else:
            outputList=query
        if flag==0:
            break
    else:
        flag=0
        break
if flag==1:
    print(sorted(outputList.items(),key=lambda k:(k[1],k[0]),reverse=True))
else:
    print("required contents are not available")
