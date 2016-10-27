import glob, os
import sys, random

filename = sys.argv[-1]
#/Users/umanggala/Desktop/Courses/NLP/NLP_Email_Classification
target = open("/Users/umanggala/Desktop/Courses/NLP/NLP_Perceptron" + "/nbmodel.txt", 'w')

class input_processing:
    def __init__(self, dir):
        self.dir = dir

    def calculate_perceptron(self,new_dict,new_dict_1,bias,my_list,average_weight,average_bias,count1):


        for count in my_list:
            sum_xd_wd = 0
            weight_dict = new_dict_1
            alpha = 0
            y_spam = 1
            y_ham = -1
            y_alpha = 0



            for word in new_dict[count][0]:
                sum_xd_wd += new_dict[count][0].get(word) * weight_dict.get(word)

            alpha = sum_xd_wd + bias

            if(new_dict[count][1] == 'spam'):
                y_alpha = y_spam * alpha
            elif(new_dict[count][1] == 'ham'):
                y_alpha = y_ham * alpha

            if (y_alpha <= 0):
                if (new_dict[count][1] == 'spam'):
                    for words in new_dict[count][0]:

                        weight_dict[words] = weight_dict.get(words) + (y_spam * int(new_dict[count][0].get(words)))
                        average_weight[words] = average_weight.get(words) + (y_spam * count1 * int(new_dict[count][0].get(words)))
                    bias = bias + y_spam
                    average_bias = average_bias + (y_spam * count1)
                else:
                    for words in new_dict[count][0]:
                        weight_dict[words] = weight_dict.get(words) + (y_ham * int(new_dict[count][0].get(words)))
                        average_weight[words] = average_weight.get(words) + (y_ham * count1 * int(new_dict[count][0].get(words)))
                    bias = bias + y_ham
                    average_bias = average_bias + (y_ham * count1)
            count1 += 1
        return weight_dict,bias,average_weight,average_bias,count1

    def extract_token(self):

        new_dict = {}
        count = 0
        weights = {}
        average_weight = {}

        for root, subdirs, files in os.walk(self.dir):
            os.chdir(root)
            for file in glob.glob("*.txt"):
                count += 1
                new_dict_xd = {}

                with open(file, "r", encoding="latin1") as f1:
                    for line in f1:
                        #Calculating the xd
                        for word in line.strip().split():
                            if word not in new_dict_xd:
                                new_dict_xd[word] = 1
                            else:
                                new_dict_xd[word] = new_dict_xd.get(word) + 1
                            if word not in weights:
                                weights[word] = 0
                                average_weight[word] = 0

                if (os.path.basename(os.path.normpath(root)) == 'spam'):
                    new_dict[count] = new_dict_xd, 'spam'
                elif(os.path.basename(os.path.normpath(root)) == 'ham'):
                    new_dict[count] = new_dict_xd, 'ham'



        return new_dict,weights,count,average_weight

calculating = input_processing(filename+"/train")

probability_words,weight_words,count,average_weight= calculating.extract_token()
bias = 0
average_bias = 0
my_list=list(range(1,count+1))
count1 = 1
#Have to do randomize
for i in range (0,30):
    random.shuffle(my_list)
    weight_words,bias,average_weight,average_bias,count1 = calculating.calculate_perceptron(probability_words,weight_words,bias,my_list,average_weight,average_bias,count1)

for words in average_weight:
    average_weight[words] = weight_words.get(words) - ((1/count1)*average_weight.get(words))

average_bias = bias - ((1/count1)*average_bias)
target.write(str(average_bias))
target.write("\n")

for i in average_weight:
    target.write(i)
    target.write("\t")
    target.write(str (average_weight.get(i)))
    target.write("\n")

target.close()