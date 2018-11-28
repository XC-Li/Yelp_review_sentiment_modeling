# Yelp review sentiment analysis (Draft Version)
**Final project for Natural Language Processing(DATS 6450, Fall 2018)**

**Author: Li Du, Xiaochi Li**

## Abstract

## Data Source and Preprocessing
The data source we use is the Yelp dataset(Link: https://www.yelp.com/dataset) that provided by Yelp, which contains 5996996 comments and stars from users for 188593 businesses. The dataset is large enough for us to try various NLP techniques on.

The Yelp dataset (Documentation: https://www.yelp.com/dataset/documentation/main) contains 6 json files, and we will only use 4 fields, the unique business id,the customer review, stars and the category of the restaurant from business.json and review.json. 
Since this dataset contains business that are not restaurants, the preprocessing part used category as a filter to filter out the business id for restaurants and also label several subcategories for the restaurant.

After that, we used the business id to select the review and stars from the review.json.

## Natural Language Processing

### Objective and Outline
The objective is to find the best way to predict stars(target variable) from customer reviews.

Firstly, we will do a Exploratory Data Analysis into the customer reviews. We will do some necessary data manipulation and cleaning.

Then, we will try different combinations of NLP preprocessing methods (like stemming and removing stop words) and NLP models (like bags of words, normalized model, bigram model and word to vector) to find the best prediction model. The evaluation metrics is Mean Squared Error (MSE) of target and prediction. 

Another interesting topic is whether the sentiment model on one subcategory(eg. American Food) can works well on anoter subcategory(eg. Chinese Food). This leads to the question whether we should train models on subcategories indepentently.
We will train and test specialized NLP model cross subcategories to find out.

### Exploratory Data Analysis

### NLP modeling on the whole review data

### NLP modeling cross different subcategories

## Finding and Conclusion 
We will summarize the findings and try to explain the findings and get the final conclusion.
