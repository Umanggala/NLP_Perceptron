import glob, os
import sys

filename = sys.argv[-1]


class input_processing:
    def __init__(self, dir):
        self.dir = dir

    def extract_token(self):

        alpha = 0
        new_dict = {}
        bias = 0
        sum_xd_wd = 0
        spam_y = 1
        ham_y = -1
        new_dict_xd = {}

        for root, subdirs, files in os.walk(self.dir):
            os.chdir(root)
            for file in glob.glob("*.txt"):
                #new_dict_xd = {}
                with open(file, "r", encoding="latin1") as f1:
                    for line in f1:
                        #Calculating the xd
                        for word in line.strip().split():
                            if word not in new_dict_xd:
                                new_dict_xd[word] = 1
                            else:
                                new_dict_xd[word] = new_dict_xd.get(word) + 1

                #Calculating alpha
                    for word in new_dict_xd:
                        if word in new_dict:
                            #sum_xd_wd += new_dict.get(word)*new_dict_xd.get(word)
                        #else:
                            new_dict[word] = 0
                            #sum_xd_wd += 0
                '''
                print(sum_xd_wd)
                alpha = sum_xd_wd + bias
                #print(alpha)
                if(os.path.basename(os.path.normpath(root)) == 'spam'):
                    y_alpha = spam_y * alpha
                else:
                    y_alpha = ham_y * alpha

                if(y_alpha <= 0):
                    for words in new_dict_xd:
                        new_dict[words] = new_dict.get(words) + (y_alpha * new_dict_xd.get(words))
                '''
        return new_dict_xd

calculating = input_processing(filename+"/train")

probability_words = calculating.extract_token()