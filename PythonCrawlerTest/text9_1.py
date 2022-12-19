import csv
import re


def openfile(path):
    file = open(r'{}'.format(path), 'r')
    data = csv.reader(file)
    return data


def ngram(gramNum):
    wordsDict = {}
    for i in data:
        for seq in i:
            re.sub(" |”|“", "", seq)
            seq = re.split(",|，|。|\.|!|！|？|\?|、|：|:|;|；", seq)
            seq = list(filter(None, seq))
            stopWords = "的 得 地"
            stopWords = stopWords.split(" ")
            seqs = list(map(lambda x: "".join(re.split("|".join(stopWords), x)), seq))
            for seq in seqs:
                for i in range(len(seq) - gramNum + 1):
                    wordSeq = seq[i:i + gramNum]
                    if wordSeq not in wordsDict:
                        wordsDict[wordSeq] = 1
                    else:
                        wordsDict[wordSeq] = wordsDict[wordSeq] + 1
    print(wordsDict)


if __name__ == '__main__':
    path = 'E:\mypro\Crawler\\taobaoComment-data-csv.csv'
    data = openfile(path)
    ngram(2)
