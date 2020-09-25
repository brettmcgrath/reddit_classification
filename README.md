## Table of Contents  
- [Project Contents](#Project_Contents)
- [Data](#Data)  
- [Data Problem](#Data_Problem)  
- [Exploratory Data Analysis and Feature Engineering](#Exploratory_Data_Analysis_and_Feature_Engineering)  
- [Preprocessing and Modeling](#Preprocessing_and_Modeling)  
- [Reflections on the modeling process](#Reflections_on_the_modeling_process)  

## Project Contents:

The attached file contains two CSV files with data consumed from the pushift.io reddit API, the api.py python file that contains the code I used for making API calls, and reddit.ipynb, a jupyter notebook that contains my exploratory data analysis and classification modeling between r/news and r/conspiracy subreddits.

## Data

Data used in this project consists of 51.96% conspiracy subreddit comments (only comments on posts, no posts themselves) and 48.04% comments from r/news. Data consists of 42,881 separate entries in total. Comments were from Tuesday, September 15, 2020 4:45:52 PM to Thursday, September 17, 2020 12:52:17 AM and Wednesday, September 16, 2020 3:41:27 AM Thursday, September 17, 2020 12:53:19 AM from the conspiracy and news subreddits respectively.

## Data_Problem

The problem I have set out to solve is to accurately classify comments (not posts, but rather the comments attached to them) from the conspiracy and news subreddits. I chose these two subreddits as a challenge to see how well machine learning algorithms could distinguish between two subreddits with similar content. 

## Exploratory_Data_Analysis_and_Feature_Engineering

Deleted comments and comments by moderators (around 15% of content) were filtered out in my function consuming the pushift.io Reddit API. A significant amount of time was spent cleaning the dataset of non-english characters, creating stop words, and removing URLs, mathematical and other special characters not useful to Natural Language Processing. In an attempt to account for things computers cannot so readily understand as humans--sentiment, tone, type of sentence, etc--I created the following categories:
1. **cl_count** - Number of capital letters appearing in each post
2. **exc_count** - Number of exclamation points appearing in each post
3. **qm_count** - Number of question marks points appearing in each post
4. **char_count** - Number of individual characters in each post
5. **word_count** - Number of words in each post
6. **url_count** - Number of urls in each post
7. **elongated_vowels** - Instances of three or more vowels together appearing in each post: ie "aaa", "iii", "uuu", etc
8. **percent_count** - Number of times % or 'percent' appears in a post
9. **q_word_count** - Number of occurences of question words "who," "what", "when", "why", "where", and "how"
10. **number_count** - Occurences of digits appearing in each post

These features were used in a Logistic Regression and a Linear SVC model but not in the final Multinomial Naive Bayes model.

## Preprocessing_and_Modeling

WordNetLemmatizer was used to further break words down once filtered as explain above. TfidfVectorizer was used to create a sparse matrix of binary encoded words. Several different classification model types were attempted, with the best results found in a Multinomial Naive Bayes model. This model achieved 99% accuracy on the Training data, and 75.94% on testing data with a cross-validation score of 75.12% accuracy as the mean of 5 cross validations. Logistic Regression, which was my first choice when establishing a baseline, came in second at around 73% accuracy. My Multinomail Naive Bayes model performed best using words as the analyzing parameter with ngram_range=(1,3), no extra stop words, max_df=0.15, and utilizing l2 (Ridge) regularization. The low DF number indicates to me that the model focused on rarer words to differentiate between the two subreddits. Best hyperparameters were found through pipeline and GridSearchCV.

## Reflections_on_the_modeling_process

Overfitting was a major concern I had from the beginning of the modeling process. My first Logistic Regression model performed with 87.54% accuracy on training data, and 73.16% on testing data. The features I engineered added little explanatory power in most cases, but did add explanatory power for the Linear SVC model. In the future I would like to explore other ways to incorporate other features to give meaning to words beyond vectorized counts. 

## Conclusions_and_Recommendations

As a first dive into Natural Language Processing, I am left with many questions I would like to explore. I would like to explore the relationship of words with more detail and ways that I can allow them to have more explanatory power beyond what I have demonstrated here. I feel that 75% accuracy is a great achievement in the creation of a model that can classify comments on two subreddits that share so many topics and users in common. Though this model itself is likely not immediately useful to any individual or organization, the modeling techniques used could be applied beyond this project for implementation in Natural Language Processing tasks elsewhere and could contribute valuable insights to marketing teams or academic study.
