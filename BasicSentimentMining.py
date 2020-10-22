
from spellchecker import SpellChecker
import os


class SentimentMining:
    senti_word_file = "Support_files/SentiWordNet3.txt"
    stop_word_file = "Support_files/Stopwords.txt"
    senti_word_dict = {}

    def __init__(self, input_file_name):
        # receives path of a text file and limits on chars
        # Read more on file processing https://realpython.com/read-write-files-python/
        self.filename = input_file_name
        file = open(os.path.join(os.getcwd(), 'student_input_files', self.filename), 'r', encoding="utf8")

        self.content = file.read()
        self.clean_content = self.preprocess()
        self.unique_words = self.get_set_of_unique_words()

        # Read the content of the SentiWordNet3.txt and populate the following dictionary
        # Keys: words, values: positive and negative scores corresponding to keys
        SentimentMining.senti_word_dict = {}
        file = open(self.senti_word_file, 'r', encoding="utf8")  # dummy assignment
        lines = file.readlines()
        for line in lines: #each line
            values = line.split(',') #split each value at the comma
            rating = (values[0], values[1]) #positive negative sentiment is in tuple
            for i in range(2, len(values)): #all words with this sentiment score become there own line in the dict
                SentimentMining.senti_word_dict[values[i]] = rating #word is value, tuple ratings are key

    def print_content(self):
        print('The original content of the file {} is printed below:'.format(self.filename))
        print("\"{}\"".format(self.content))

    def preprocess(self):
        characters = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z') #keep letters
        # makes a copy of the "self.content"

        # remove everything but a-z/A-Z/ and spaces from the text
        # returns the cleaned content
        # spell = SpellChecker()
        space_it = False #keeps track if space needed after period or comma
        cleaned_content = ""
        for x in self.content: #each character in string

            if x in characters: #if acceptable character
                if space_it == True and x != " ":  # If no space after period make a space
                    x = " " + x
                space_it = False #does not need space next turn
                cleaned_content = cleaned_content + x.lower() # dummy assignment
            if x == "." or x == ",": #remember this for next round
                space_it = True
        return self.auto_correct(cleaned_content)

    def auto_correct(self, string):
        # find helpful resources in UsefulCodeBase.py, just control/command F and find auto_correct in UsefulCodeBase.py
        # makes a copy of the "self.content"
        # replaces mis-spelled words with correct ones
        # returns the edited content
        spell = SpellChecker()
        word_list = string.split(" ") #creates list of words
        checked_list = []
        for word in word_list:
            correct = spell.correction(word)
            checked_list.append(correct) #makes list of all words spelled correctly

        return ' '.join(checked_list) #rejoin

    def get_letter_frequency(self):
        # works on self.clean_content
        # returns a dictionary with (key: value) => (letter:frequency)
        letter_freq_dict = dict()

        for x in self.clean_content:
            if x in letter_freq_dict: #word already in dict used again
                letter_freq_dict[x] += 1
            else: #new word in dict
                letter_freq_dict[x] = 1

        return letter_freq_dict

    def get_word_frequency(self):

        # works on self.clean_content
        # returns a dictionary with (key: value) => (word:frequency)
        word_freq_dict = dict()
        words = self.clean_content.split(" ")
        for x in words: #works same as letter frequency
            if x in word_freq_dict:
                word_freq_dict[x] += 1
            else:
                word_freq_dict[x] = 1

        # dummy assignment
        return word_freq_dict

    def get_set_of_unique_words(self):

        # works on self.clean_content
        allWords = self.clean_content.split(' ')
        # returns a "set" of unique words (set here is a data structure)
        unique_word_set = set(allWords)  # set key cannot have same value twice, so already unique
        return unique_word_set

    def get_useful_words(self):
        # works on self.clean_content
        # returns list of NON-stopwords (see Stopwords.txt under Support_files folder)
        file = open(os.path.join(os.getcwd(), SentimentMining.stop_word_file), 'r',
                    encoding="utf8")
        stop_words = file.read()
        file.close()
        stop_words = set(stop_words.splitlines())
        useful_word_list = [] #array for all non stop words
        prior_word_neg = False  # starting state
        words = self.clean_content.split(" ")
        negation = set(["no", "not", "none", "nobody", "nothing", "neither", "nowhere", "never", "hardly", "scarcely", "barely", "doesnt", "wasnt", "isnt", "shouldnt", "wouldnt", "couldnt", "wont", "cant", "dont"])
        for word in words:

            if word not in stop_words:  # all non stop words
                if prior_word_neg == True:  # if last non stop word is negation
                    word = "N" + word  # non stop word after negation is marked
                    prior_word_neg = False  # resolves negation

                useful_word_list.append(word)
            if word in negation:  # next word is a negation word
                prior_word_neg = True  # mark it

        return useful_word_list

    def get_keywords(self):
        # works on self.clean_content
        # makes use of useful words in the word dictionary
        # returns a list of UPTO 6 most frequent NON-stopwords words (see Stopwords.txt)
        word_use = self.get_word_frequency()
        key_words = 0 #amount
        last_value = 0  # last used word frequency to compare how often used
        keywords = []
        possible_keywords = sorted(word_use.items(), key=lambda x: x[1], reverse=True) #orders amount a word is used by key
        file = open(os.path.join(os.getcwd(), SentimentMining.stop_word_file), 'r',
                    encoding="utf8")
        stop_words = file.read()
        stop_words = stop_words.splitlines()
        for senti in possible_keywords:
            if senti[0] not in stop_words: #tracks how many keywords are being added
                key_words += 1
                if key_words > 6 and last_value != senti[1]: #no more key words if more than 6 and the last word is not equally as used
                    break
                last_value = senti[1]
                keywords.append(senti[0])

        # possible_keywords = []  # dummy assignment
        return keywords

    def get_the_sentiment(self):
        sentiment_scores = []
        senti_dict = SentimentMining.senti_word_dict
        useful_words = self.get_useful_words()
        for word in useful_words:
            if word[0] == "N":
                if word[1:] in senti_dict:
                    negative_score = senti_dict[word[1:]]
                    score = float(negative_score[0]) - float(negative_score[1])
                    # sentiment_scores.append(-1 * score) #original approach
                    sentiment_scores.append(0.0)

            else:
                if word in senti_dict:
                    normal_score = list(senti_dict[word])
                    score = float(normal_score[0]) - float(normal_score[1])
                    sentiment_scores.append(score)
        filtered_scores = [number for number in sentiment_scores if number != 0.0]
        # negative = 0
        # positive = 0
        # for number in filtered_scores:
        #     if number < 0:
        #         negative += 1
        #     else:
        #         positive +=1
        # if positive == 0:
        #     positive = 1
        # if negative == 0:
        #     negative = 1
        # if positive/negative < 1.6:
        #     return "Negative"
        # if positive/negative > 2.2:
        #     return "Positive"
        # else:
        #     return "Neutral"


        filtered_scores.sort()
        if (len(filtered_scores) == 0):
            median = 0
        else:
            median = filtered_scores[(len(filtered_scores) - 1)//2]

        if median < 0:
            return "Negative"
        if median > .125:
            return "Positive"
        else:
            return "Neutral"
        return median



        # returns the sentiment of the text (read the sentiment computation in the description)
        # This will make use of the content of the file named SentiWordNet3.txt
        # The content of the file is taken from https://raw.githubusercontent.com/aesuli/SentiWordNet/master/data/SentiWordNet_3.0.0.txt
        # https://github.com/aesuli/SentiWordNet
        # The content of the file is in the following order
        # <PosSentiScore>, <NegSentiScore>, <Word>, <possible synonyms>
        # for example, 0.125,0.25,preferential,discriminatory
        # You must have already thought of creating a dictionary of words (keys) and corresponding sentiment scores (values)
        # Since there are synonyms listed for some words, think about the best possible structure of the dictionary, i.e. what would be the keys and corresponding values of the dictionary
        # Keys have to be immutable objects! -- a list is mutable -- think how can you solve it

        # file = open(os.path.join(os.getcwd(), "Support_files", SentimentMining.senti_word_file), 'r',
        #             encoding="utf8")
        # senti_content = file.read()
        # dummy assignment
        # <Find the sentiment of each words available in the useful_words>
        # <See the distribution of the score either by plotting it or just looking at the raw numbers>
        # <Try to write your logic here for the classification>
        # <A value will be assigned to the value "sentiment" and return the sentiment>


# Helper function to print a dictionary (line by line)
def print_dictionary(dict_in):
    for key in dict_in:
        print(key, ': ', dict_in[key])
#
#
# # *****Following code need not be changed*****#
#
if __name__ == "__main__":
    # Install packages as suggested
    # install seaborn
    import seaborn as sns
    # Install matplotlib
    import matplotlib.pyplot as plt
    # Install sklearn
    from sklearn.metrics import confusion_matrix

    classes = ['Positive', 'Neutral', 'Negative']
    input_folder_path = os.path.join(os.getcwd(), 'student_input_files')
    ACTUAL_LABELS = []
    PREDICTED_LABELS = []
    for file_name in os.listdir(input_folder_path):
        # print("----------Analysis of {}----------".format(file_name))
        Document = SentimentMining(file_name)
        Document.print_content()
        print('The cleaned up content:', Document.preprocess())
        print('The dictionary of letter freq:')
        print_dictionary(Document.get_letter_frequency())
        print('The dictionary of word freq:')
        print_dictionary(Document.get_word_frequency())
        print('The set of unique words:', Document.get_set_of_unique_words())
        print('The set of useful words:', Document.get_useful_words())
        print('The list of keywords:', Document.get_keywords())
        ACTUAL_LABELS.append(file_name[file_name.find('_') + 1:-4])
        PREDICTED_LABELS.append(Document.get_the_sentiment().replace(" ", ""))  # Removing spaces if any

    conf_mat = confusion_matrix(ACTUAL_LABELS, PREDICTED_LABELS, classes)
    # Draw a heatmap with the numeric values in each cell
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(conf_mat, annot=True, fmt="d", linewidths=.5, ax=ax, cmap='Pastel2')
    ax.set_xticklabels(classes)
    ax.set_yticklabels(classes)
    plt.yticks(rotation=0)
    plt.xticks(rotation=0)
    plt.show()

a = SentimentMining("605_Positive.txt")
print(a.preprocess())
