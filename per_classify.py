import glob,os
import re, math
import sys

filename = sys.argv[-1]
#/Users/umanggala/Desktop/Courses/NLP/NLP_Email_Classification

newDict = {}
with open("/Users/umanggala/Desktop/Courses/NLP/NLP_Perceptron" + '/nbmodel.txt') as f:

    bias1 = f.readline()
    bias = int(bias1)

    for line in f:
        splitLine = line.split()
        newDict[splitLine[0]] = int(splitLine[1])

f.close()

target = open(filename + "/nboutput.txt", 'w')
classified_correct_spam = 0
classified_incorrect_spam = 0
classified_correct_ham = 0
classified_incorrect_ham = 0
total_files = 0
classified_as_spam = 0
classified_as_ham = 0
file_spam = 0
file_ham = 0

for root, subdirs, files in os.walk(filename + '/dev'):
        os.chdir(root)

        for file in glob.glob("*.txt"):
            with open(file, "r", encoding="latin1") as f1:

                sum_xd = 0
                if os.path.basename(os.path.normpath(root)) == "spam":
                    file_spam = file_spam + 1
                else:
                    file_ham = file_ham + 1

                probability_spam_given_text = 0
                probability_ham_given_text = 0

                for line in f1:
                    line = ''.join(line.splitlines())

                    for word in line.split():
                        if word in newDict:
                            sum_xd = sum_xd + newDict.get(word)

                alpha = sum_xd + bias
                total_files = total_files + 1

                if(alpha > 0):

                    target.write("Spam")

                    classified_as_spam = classified_as_spam + 1
                    if(os.path.basename(os.path.normpath(root)) == "spam"):

                        classified_correct_spam = classified_correct_spam + 1
                    else:
                        classified_incorrect_spam = classified_incorrect_spam + 1

                else:
                    target.write("Ham")

                    classified_as_ham = classified_as_ham + 1
                    if (os.path.basename(os.path.normpath(root)) == "ham"):
                        classified_correct_ham = classified_correct_ham + 1
                    else:
                        classified_incorrect_ham = classified_incorrect_ham + 1

                target.write("\t")
                target.write(root + "/" + file)
                target.write("\n")

precision_spam = classified_correct_spam / classified_as_spam
precision_ham = classified_correct_ham / classified_as_ham

recall_spam = classified_correct_spam / file_spam
recall_ham = classified_correct_ham / file_ham

F1_spam = (2*precision_spam*recall_spam)/(precision_spam + recall_spam)
F1_ham = (2*precision_ham*recall_ham) / (precision_spam + recall_ham)

print(precision_spam)
print(precision_ham)

print(recall_spam)
print(recall_ham)

print(F1_spam)
print(F1_ham)


target.close()





