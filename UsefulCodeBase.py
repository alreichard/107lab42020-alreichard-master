# print the frequency of vowels in a text file
alpha_dict = dict()
vlist = 'aeiou'
filepath = 'Example.txt'
file = open(filepath, 'r', encoding="utf8")
file_content = file.read()
file_content = file_content.lower()
for c in file_content:
 if c in vlist:
     if c not in alpha_dict:
         alpha_dict[c] = 1
     else:
         alpha_dict[c] = alpha_dict[c] + 1

print(alpha_dict)

###################################################################
# The following code creates multiple files from one text file.
# The content of the input file looks like:
# 5,"I initially had trouble deciding between the paperwhite and the voyage because reviews more or less said the same thing: the paperwhite is great, but if you have spending money, go for the voyage.Fortunately, I had friends who owned each, so I ended up buying the paperwhite on this basis: both models now have 300 ppi, so the 80 dollar jump turns out pricey the voyage's page press isn't always sensitive, and if you are fine with a specific setting, you don't need auto light adjustment).It's been a week and I am loving my paperwhite, no regrets! The touch screen is receptive and easy to use, and I keep the light at a specific setting regardless of the time of day. (In any case, it's not hard to change the setting either, as you'll only be changing the light level at a certain time of day, not every now and then while reading).Also glad that I went for the international shipping option with Amazon. Extra expense, but delivery was on time, with tracking, and I didnt need to worry about customs, which I may have if I used a third party shipping service.","Paperwhite voyage, no regrets!"
# 5,"Allow me to preface this with a little history. I am (was) a casual reader who owned a Nook Simple Touch from 2011. I've read the Harry Potter series, Girl with the Dragon Tattoo series, 1984, Brave New World, and a few other key titles. Fair to say my Nook did not get as much use as many others may have gotten from theirs.Fast forward to today. I have had a full week with my new Kindle Paperwhite and I have to admit, I'm in love. Not just with the Kindle, but with reading all over again! Now let me relate this review, love, and reading all back to the Kindle. The investment of 139.00 is in the experience you will receive when you buy a Kindle. You are not simply paying for a screen there is an entire experience included in buying from Amazon.I have been reading The Hunger Games trilogy and shall be moving onto the Divergent series soon after. Here is the thing with the Nook that hindered me for the past 4 years: I was never inspired to pick it up, get it into my hands, and just dive in. There was never that feeling of oh man, reading on this thing is so awesome. However, with my Paperwhite, I now have that feeling! That desire is back and I simply adore my Kindle. If you are considering purchasing one, stop thinking about it simply go for it. After a full week, 3 downloaded books, and a ton of reading, I still have half of my battery left as well.Make yourself happy. Inspire the reader inside of you.",One Simply Could Not Ask For More
# 4,I am enjoying it so far. Great for reading. Had the original Fire since 2012. The Fire used to make my eyes hurt if I read too long. Haven't experienced that with the Paperwhite yet.,Great for those that just want an e-reader
# 5,"I bought one of the first Paperwhites and have been very pleased with it its been a constant companion and I suppose Ive read, on average, a book every three days for the past however many years on it. I wouldnt give it up youd have to pry it from my cold dead fingers.For sundry logistical reasons, Ive also made good use of Amazons Kindle app on my iPhone. No Paperwhite screen, naturally, and all the cool usability that delivers, but it works well and has its own attractions as a companion to the Kindle.Of course, there are aspects of the Paperwhite which I would like to critique. Ah you knew that was coming somewhere, didnt you.As a member of BookBub, I get a daily list of alerts and book deals in my chosen genres. I take on many of them, however, Ive found that, even with the best will in the world, I cant keep up. Some days it seems that for every book I read, Ive bought two. Theres just so much good stuff out there! The accumulative effect of this is that the number of books actually on my Paperwhite has been creeping ever upward for some time. Its now at about 400.With this in mind, Ive noticed that while page-turning has remained exactly the same, just about every other action on the Kindle has become positively glacial. Not just very slow, but so slow you think its malfunctioning. The general consensus appears to be that its to be expected once one has that many books downloaded onto a Kindle, it will begin to behave in a flakey manner. This drives me mad. Amazon states it can hold thousands of books. I believe them. But I figure I would need a second Paperwhite to read while Im waiting for actions to complete on the first one.Read more",Love / Hate relationship
# 5,"I have to say upfront - I don't like coroporate, hermetically closed stuff like anything by Apple or in this case, Amazon. I like having devices on which I can put anything I want and use it. But...I was a fairly happy user of a Nook Touch for several years, but couldn't use all its functionalities since I live in Serbia. Then I lost the Nook and since no other devices can actually be fully used in Serbia (buying books with them, using their online capabilities) except the Kindle, and since no one except Amazon ships to Serbia, and since I've actually been a happy Amazon customer since 2005 over friends' accounts and since 2007 through my own, and since the Kindle definitely has the best technology - why not buy itSo I did. What I read in many reviews about the screen/light of the Paperwhite and similar devices was no problem with mine. The light disperses just fine, except a few black blotches (maybe you can see it in the picture) at the bottom of the screen, which are actually shadows of the black plastic casing and thus can't really be avoided. As you can see in the picture without the light - there are no blotches with light out.The Paperwhite's screen is just marvelous at 300 ppi, the touchscreen works just fine, the store works here in Serbia, and in these two days I've been using it, I'm a happy guy.I had to get the hang on how to make sideloaded books behave at least almost like Amazon books, but that's fine. That's the one thing I'd like to see Amazon do in some future upgrades: make the Kindle treat sideloaded books just like the ones bought from them directly, with sharing funcion (quotes and Goodreads) enabled and so on.The size is perfect, it sits very well in the hand, the light doesn't hurt the eyes in the dark (like the light on a tab does)... the packaging was fine, no problems there and what remains to be seen now is the battery life.So far, I can only recommend it.",I LOVE IT
# 4,"Had older model, that you could text to speech, this one hasn't. Liked the smaller size, but having to buy a different cover! Still getting used to shelf quite different from my 4 year old model.Paper white is nice reading.",Liked the smaller size

# The code assumes the first number to be the rating and creates a file name based on the rating
# Then the code writes the corresponding line into the file. 
# Make sure you create a blank folder named Input_files in the current directory
# n files shall be created inside Input_files, where n is the number of lines in the input file. 
import os
file_path = 'AmazonReviewRatings.txt'
# https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products/version/1#
sentiment_mapping = {3: 'Positive', 2: 'Neutral', 1: 'Negative'}
with open(file_path) as fp:
   for line_counter, line in enumerate(fp):
       sentiment_id = int(line[0])
       newfile_name = str(line_counter)+'_'+sentiment_mapping[sentiment_id]
       folder_location = os.path.join(os.getcwd(),"Input_files",newfile_name+'.txt')
       f = open(folder_location, "w+")
       f.write(line[2:])
 
###################################################################
# auto_correct demo and more about NLTK package.
# Source: http://theautomatic.net/2019/12/10/3-packages-to-build-a-spell-checker-in-python/

# Here is one way to use the spelling check/correction method, there are other methods that you can use too. Feel free to explore!
# Note that you can only use spelling check/correction methods in foreign packages (e.g. NLTK), no other foreign package is allowed! You need to implement all methods except auto_correct only with things supplied in Python.
# basic setup and import packages per need
from spellchecker import SpellChecker
spell = SpellChecker()
x # address
spell.correction("becuase") # because
