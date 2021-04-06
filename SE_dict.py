from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def preProcessing(text):
    text=text.lower()
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

invertedIndex = {}

for i in fileList:
    readFile = i.read()
    ProcessedFile = preProcessing(readFile)
    for words in ProcessedFile:
        if words not in invertedIndex:
            invertedIndex[words]={}
        if i.name not in invertedIndex[words]:
            invertedIndex[words][i.name]=1
        else:
            invertedIndex[words][i.name]+=1


search = input("Enter the sentence to be searched : ")
outputList = {}
flag=1
processedText = preProcessing(search)
for i in processedText:
    try:
        query = invertedIndex[i]
    except KeyError:
        flag=0
        break
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
