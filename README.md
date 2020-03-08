# WISH by Nana 
*What is she wearing?*

**WISH** is a machine-learning powered fashion recommendation engine which allow users to input any JPG or JPEG photo of clothing items and receive recommendations for visually similar items (and where to buy them). It works using **Object Detection** with **YOLO V3**, **Feature Extraction** with **Inception V3** in conjunction with **K-Nearest Neighbor**. 

Proposed Business Applications: 

- SHOPS: Instant Item Retrieval 
- SHOPPERS: Instant Shop-the-Look Solution

I created WISH from scratch because I wanted to offer a proof-of-concept solution to specific-item retrieval challenges faced by both Shops and Shoppers. WISH is the result of my 12 weeks in a Machine Learning Bootcamp taught at CoderSchool in Ho Chi Minh City, Vietnam. The project competed with 16 others and snatched the **First Prize** agreed upon by 5 external judges. 

![](https://i.imgur.com/6kww597.png)

Please view the entire project [here](https://www.beautiful.ai/player/-M19TNQ-3mBssQUbIK53).

<h2> How it works: </h2> 

A - SHOW Mode: 

In SHOW, users upload a picture (JPG or JPEG format) - the built-in YOLO function will apply preprocessing onto the image & feed it to the model as an input. The output will be a number of prediction (0 - the number of detected item) with bounding boxes drawn around the detected clothing item. There are 5 labels: Top, Trousers, Skirt, Shorts and Dress. The bounding box will be accompanied by the prediction label (one of five). 

![](https://i.imgur.com/fr8KJhU.jpg)
![](https://i.imgur.com/SS4I10b.jpg)


B - SHOOT Mode: 

With SHOOT, users are able to use their device's camera to perform Live Detection of any clothing item. Good lighting & frontal capture will work best. 

![](https://i.imgur.com/G6y0EYS.jpg)

<h2> The Dataset: </h2> 
https://github.com/switchablenorms/DeepFashion2

I used a portion of the abovementioned dataset (a total of about 16GB in size) and combined a few categories (e.g. Short-sleeve Top & Long-sleeve Top as Top, Sling Dress & Midi Dress as Dress etc.) to create my own dataset of 5 labels mentioned earlier. 

<h2> The Database: </h2>

To create the Database for recommendation, I scraped product information from the following websites ([Topshop](https://www.topshop.com/), [Stylenanda](https://en.stylenanda.com/), and [Farfetch](https://www.farfetch.com/vn/)). They were chosen to represent different price points and styles (e.g. Korean, Western etc.). The data is stored in .csv files for shorter & simpler information such as names, prices, hrefs etc. while feature extraction vectors was stored in .pkl files due to their length (storing a (1, 2048) vector in a .csv file will cause it to be truncated and rendering it incomplete.) 

![](https://i.imgur.com/2IBFiQY.jpg)

![](https://i.imgur.com/LeCOnuS.jpg)

<h2> Pipeline </h2> 

![](https://i.imgur.com/HVJzgdt.jpg)

<h4>Customized Object Detection:</h4> YOLOV3 was trained using the Darknet framework. Please go to https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects for AlexeyAB's tutorial which taught me how to train using my own dataset of clothes. Thank you Alexey! 

To allow users to feed whatever input images (one containing just one clothing item to those containing multiple set of clothing) into the recommendation engine, I chose to train with YOLOV3 and the Customized Object Detection route instead of going the classification with CNN > recommendation route. I found that YOLOV3 also produces incredible accuracy and very low loss. 

<h4> Feature Vector Extraction: </h4> 

Thanks to one of my colleague's work (please give him a Github star [here](https://github.com/jodythai/nozama-recommendation-system)), I learned about the simple but powerful idea of Feature Vector Extraction. To accomplish this, I used a pre-trained CNN Model, [InceptionV3](https://github.com/keras-team/keras-applications/blob/master/keras_applications/inception_v3.py), capitalized on the optimized weights then stack a GlobalAveragePooling2D layer (pictured) as the output layer to produce a vector of shape (1, 2048) containing features of the input image. I applied the same method on all images in my Database to allow comparison using KNN (next step) and produce visually similar recommendations for every input. 

<h4> K-Nearest Neighbor: </h4> 

Another easy-to-implement but extremely useful [module](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier) of the scikit-learn library, KNN is a Classifier implementing the k-nearest neighbors vote. Feature Vectors of the same categories are trained (fit) and the trained model will predict the class for new user-input image and produce the nearest neighbors = visually similar items. 

Learn more [here](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier). 

<h2> Future Works </h2> 

WISH was created in 2 weeks, so it goes without saying that there is room for (many) improvement(s). Including male fashion, expanding the categories for detection & recommendation, improving the website's functionality are a few to name. 

As a beginner, I am fully aware how my codes can be improved to increase efficiency. Any recommendation (:D), suggestion and criticism is welcomed. Please, if you have anything to contribute / comment, don't hesistate to reach out to me via email at natalientb.nguyen@gmail.com. Let's also connect on [LinkedIn](https://www.linkedin.com/in/nnatalienguyen/)! 

I started this journey only a little more than 4 months ago and this is my first end-to-end project. There is a long way ahead but I am filled with nothing but excitement and curiousity. I'd like to leave you with the following quote by one of my favourite scientists of all time, Stephen Hawking: “Remember to look up at the stars and not down at your feet. Try to make sense of what you see and wonder about what makes the universe exist. Be curious. And however difficult life may seem, there is always something you can do and succeed at. It matters that you don't just give up.” Hope it inspires anyone reading as it did for me! Thank you for reading :) 





















