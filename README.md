Course: CS 107, Fall 2020, Haverford College
Due Date: Midnight, October 16, 2020

Alex Reichard

Problem: Basic Sentiment Analysis

Allowed packages: everything supplied to you with Python 3.7, some packages (e.g., NLTK) are already imported for specific purposes in order to complete the sentiment analysis pipeline. You should not use NLTK or any other package to accomplish the tasks that you have to program. In other words, you need to implement all methods except auto_correct only with things supplied in Python 3.7. In case, you really need to use a package, post it on Piazza with details, the instructor will consider if it's appropriate). 

Useful Readings: 

Note: These reading are to develop your understanding about the domaina and excite you about the field. You dont have to understand/follow everything given in these articles (especially the machine learning models given at the end as its out of scope of the class -- of course you are encouraged to read through them). Also, make sure you DO NOT copy the statements from these articles to accomplish the tasks that you are supposed to acomplish via code that you will developed. 

Basics of sentiment analysis: https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python
Details about NLTK: https://www.linkedin.com/pulse/text-classification-using-bag-words-approach-nltk-scikit-rajendran/
A flowchart of sentiment analysis: https://images.app.goo.gl/c2eV5FcvrJHX33Kq6

Goal: to test knowledge and skills in Python's basic data structures (e.g. list, string, dictionary, tuple). 

Grading: 33% is the minimum (baseline) accuracy you have to obtain to get the full points. Every 5% higher than the baseline, you get a 2-point bonus.

Terms and Definitions:

Stop Words: 

A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that search engines are programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query. See the stopwords.txt file for the list of words that you have to use. Read more at https://en.wikipedia.org/wiki/Stop_words 

https://krakensystems.co/blog/2018/sentiment-analysis-problems

Negations:

Since we are using a classical “Bag of words” model, we have a problem because it doesn’t work well with negations. Considering that word order isn’t important, the model doesn’t recognize the opposite meaning between sentences like “I like this chocolate” and “I do not like this chocolate”. It would probably give them the same score, marking the words “like” and “chocolate” as positive. To bypass this problem, you can stick negation to the following verb (e.g. notlike) and treat it as a new word. Before that, it is good to restore all abbreviated negations into their longer versions (like: don’t to do not).

Irony, Sarcasm, Metaphors, Jokes:

Well, computers don’t have a sense of humor and are not able to understand figurative language. Most of the times, even people aren’t really sure what was intended. Humour as a phenomenon is still undefined, we cannot generalize or formalize something that makes people laugh. Sarcasm or irony usually changes a positive literal meaning of word into something negative, but how can we be sure that a person didn’t literally mean what he or she wrote? That is why we can say that it is impossible to create uniform detector which will work well with irony, sarcasm, metaphors, and jokes without good context investigation and even then it doesn’t work great.


Sentiment computation: To find the sentiment of the given text you will first need to compute the sentiment score of the text. The process is described below:

    > Step1: preprocess
    
    > Step2: remove any special symbols and incorrect spelling
    
    > Step3: get_useful_words
    
    > Step4: get the sentiment score for each word in the list obtained in Step3. The sentiment score for each word is available in SentiWordNet3.txt (inside Support_files folder).
    
    > Step5: Think what can you do with the list of scores obtained in Step4. 

Some basic ideas and associated pros/cons are provided below. This Step is more of an open challenge where you are free to think of any method and obtained the best accuracy you can. Hint: none of the suggested methods take the statement that include Negation, Irony, Sarcasm, Metaphors, and Jokes. 

    > You can count number of possitives and number of negatives and setup classification rule as follows:
        if (num_pos_words - num_neg_words) > = threshold1: 
           return "positive" #  threshold1 is a positive real numbers
        elif (num_pos_words - num_neg_words) > = threshold2 and (num_pos_words - num_neg_words) < threshold1: # threshold2 is a negative real number
           return "neutral"
        else:
           return "negative"
    > (ii) You can find the median of the score and compare it with different threshold similar to what we have done above.
    > (iii) Some of you may be tempted to use an average of the pos and neg sentiment scores. Think more it may or may not be a good idea. 
    ** This part of the lab is a research component i.e. you have to try and test several methods and find out which works better and why. See in FAQs.

Specific tasks that you have to accomplish:

Implement the following methods:

Part I: Prepare at least one test case for each of the following methods.
> (1) preprocess(<parameter_list_of_your_choice>): remove everything but alphabets (only remove extra spaces). 
      Note: There is a chance that you may lose valid words while removing comma or extra spaces, that means you have to be diligent, and should be able to recover each and every possible word from the text.
	  
> (2) auto_correct(<parameter_list_of_your_choice>): replaces mis-spelled words with correct ones.  // look at auto_correct in UsefulCodeBase.py

> (3) get_letter_frequency(<parameter_list_of_your_choice>): returns a dictionary with keys: letters, values: frequency

> (4) get_word_frequency(<parameter_list_of_your_choice>): returns a dictionary keys: words, values: frequency

> (5) get_set_of_unique_words(<parameter_list_of_your_choice>): returns a "set" of unique words (set here is a data structure)

> (6) get_useful_words(<parameter_list_of_your_choice>): returns list of NON-stopwords (see stopwords.txt)
Note: Return all if there is a tie for sixth place. And it has to be up to six words, that means if you have an input of three unique words, you would just return all three words. 

> (7) get_keywords(<parameter_list_of_your_choice>): returns a list of 6 most frequent NON-stopwords words (see stopwords.txt) 

> (8) get_the_sentiment(<parameter_list_of_your_choice>): returns the sentiment of the text, read the sentiment computation in the description

Part II: Test each of the above with test cases developed in step Part -I 

Part-II: Make sure you comment your code and use self explanatory identifiers.


The Accuracy GOAL:

The Minimum Accuracy (better than random):
As mentioned in the class that the target you have to achieve is just better than random. The random is 33% for each of the three classes. In other words, for every row, if you divide the value in the diagonal box by the sum of that row and multiply the result by 100, you should be getting at least 33. If you run the given code, a confusion matrix (actual vs. predicted) will be get plotted. The confusion matrix visualizes the classification performance. Currently everything is being return as "positive" so you can figure our which axis is actual and which is predicted. 

Training Accuracy: The accuracy obtained by training (fine tunning the thresholds in classification rule) and testing on the same data is considered as a Training Accuracy. In other words, if you are using all the input files to decide the classification rule and adjust the thresholds, and testing the system on the same files, the results you obtain would be training accuracy. 

Testing Accuracy: The recomended way of training and testing your system is to divide the given input files into two parts, "Training" and "Testing". The accepted ratio is 2/3rd for training and 1/3rd for testing, but you can do half-half as we have more than 1100+ files. Fine-tune you threshold and classification rules that you are developing on "Training" files. Once you are convinced that it is the best you can get, no just change the folder name and test your approach on the files available in "Testing folder" 

Make sure you submit the report in report format that you have been using. (Format:https://docs.google.com/document/d/1iTjJH9jGxrbsTmScR3by0uzE_CaaAhiZgh3GPj5RbzE/edit?usp=sharing)

FAQs:

Question:
A number of words are repeated over the course of the sentiment list with different positive and negative values. Should this be the case? How should we choose between different entries for the same word? 
Answer: 
>> You could apply, min, max, or average rule. I would suggest that you take the one that gives you the strongest sentiment to keep it simple i.e. take the max of all the possible occurances. 
   
Question:   
The file contains entries for phrases, which are separated by underscores. Should we be accounting for this by checking the words around the word we are currently checking to see if they form one of these phrases? 
>> This could be very effective but I am afraid that it will make the problem much more complex. Keeping the time and scope of this lab in mind, I would suggest not to conduct this analysis. But if you have the bandwidth to do this, you are certainly encouraged to do so. 

Question: 
There are so many neutral words in the list that almost any reasonable sentence would be counted as neutral. All of the given test files are neutral according to the algorithm, even though a common-sense analysis would suggest that they span a wider range of sentiments. How should we adjust for this? Should we narrow the ranges that represent each category?
>> It depends on what method you use to develop classification rules. The options may include (1) removing all the neutral words before computing the scores, and/or (2) or anything else that you think will work better. 

Question:
How should we handle words that are not on the list? Should we discount them entirely? Should we assume that they're neutral? 
>> I would say we should discount them (not include them) in the analysis. 
    
Question:
I'm having a lot of trouble improving my accuracy in general. Currently, my algorithm sits just under 20% correctness, and about 44% fall within a +/- 1 range of being correct (for example, neutrals being classified as somewhatnegative or somewhatpositive). I'm currently calculating word sentiment based on the difference between the positive and negative scores of the first occurrence of the word in SentiWords. Then, for the sentiment of reviews, I'm averaging the nonzero scores of each word. I'm not sure what I'm doing wrong. I'm especially concerned about the large portion of positive reviews that are being classified as neutral. Can you offer some advice? 
>> Did you try squeezing in the cut off threshold for neutral? And/or increasing the range for positives in the classification rules. That might help. 

Question: 
If we use unique word set to work out the useful word list, and the unique word occurs more than one time in the article, do we include multiple times of unique word in useful word list?
>> Yes

Question:
In the get_keywords method, how should we choose which six words to include if over six words share the highest frequency?
>>> Return all if there is a tie for sixth place. Remember, it has to be up to six words, that means if you have an input of three unique words, you would just return all three words. 
 
Question:
How should our code handle capitalization? Should capitalized words be counted separately from the same word in lower case on the word frequency table? On the list of unique words? Should capitalized and lower case letters be counted separately for the letter frequency table? 
>>>> No they will be considered same words and letters. I suggest you convert everything to lowercase. 

Question:
Error when running code to create confusion matrix --- "ValueError: At least one label specified must be in y_true"
>>> The root of the error is there is no common element in the ACTUAL and PREDICTED labels. Unless you have a common element it would be impossible to find the confusion. The situation may be occurring because you do not have <>_<One of the five sentiment labels>.txt in your input file name. For example, in student_input_files you might see there is a file called dummy.txt. The dummy.txt does not follow the pattern that is previously mentioned in its name.. if you change the name of the file to dummy_Positive.txt it would work. 
