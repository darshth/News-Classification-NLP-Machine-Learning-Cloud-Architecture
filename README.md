# News-Classification-NLP-Machine-Learning-Cloud-Architecture



## AWS Application Front-End

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/images/classifier_example.png)
![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/classifier_performance2.png)


## Model Performance

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/images/classifier_performance.png)


## Auto-Cleaner Example

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/autocleaner_example.png)


## Introduction


‘Data’ has taken world by storm. Humans generate massive amounts of data everyday- knowingly and unknowingly. This is what the Scientists term as ‘The Data Glut’. Pulling out some facts and figures:

•	1.7MB of data is created every second by every person during 2020.

•	In the last two years alone, we managed to create 90% of the data that exists today.

•	2.5 quintillion bytes of data are produced by humans every day. 
•	95 million photos and videos are shared every day on Instagram.

•	Every day, 306.4 billion emails are sent, and 5 million Tweets are made.

•	It is predicted that 44 zettabytes of data will make up the entire digital universe, by 2020.

•	And a mammoth 463 exabytes of data will be generated each day by humans as of 2025.

What is happening due to this is that tremendous amount of important data and information is either being lost or being fabricated. The fabrication of information leads to mass-panic, superficial believes and biased judgements. And this information is mostly fabricated in the form of news. This is what we call fake news. 

The motivation behind developing and completing this project was to efficiently deliver a one stop solution to classify news and also to efficiently tackle fake news using the best tools and technologies in Natural Language Processing and Classification. 


## Supervised Learning Approach

Both, The News Classification as well as The Fake News Detection model use Supervised Learning Approach. 

Supervised learning is a machine learning domain that maps an input to an output based on example input-output pairs. It infers a function from labeled training data consisting of a set of training examples.


The architecture of Supervised Learning is as given below:

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/images/supervised.jpg)

Both the models use labelled data to train the machine to make accurate predictions/classifications when new instances of data are passed to the model.


## News Classification Model Tools
	
The following tools and technologies were used to create an end-to end pipeline and build a production level for the model for this use case:

•	Terminal: Terminal is used to write Linux Shell Commands in a Macintosh Computer. Ruby and Homebrew commands are essential to operate a MongoDB database.

•	MongoDB: MongoDB is a database, which has both cloud and local storage options. The objects in MongoDB are stored in a BSON (Binary JavaScript Object Notation) format.

•	PyCharm: PyCharm is an Integrated Development Environment, which here is used with Python 3.8 scripting language to pull the data, pre-process it and feed it into a CSV file.

•	AWS S3 Buckets: The AWS S3 bucket stores the CSV file, which is necessary to train using Amazon Comprehend. 

•	Amazon Comprehend: Amazon Comprehend is a Machine Learning tool that can perform various custom classification tasks like detecting dominant language, key entity recognition etc. It also provides real-time and batch-analysis options to analyze the input data and generate results with confidence intervals. The image below shows a high-level overview of Amazon Comprehend’s custom classification architecture.

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/images/comprehend_arch.png)


## Model Architecture

The pipeline architecture for model is as shown below: 

![alt text](https://github.com/darshth/News-Classification-NLP-Machine-Learning-Cloud-Architecture/blob/main/images/model_arch.png)


The Dataset for this model is derived from Kaggle, and can be found on the following link: https://www.kaggle.com/rmisra/news-category-dataset 

This dataset was downloaded in JSON format, which was then converted into a pandas data-frame. 

It has columns for category, headline, author, link, short description and date. 







 
