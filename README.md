# Project-II-How the viral recipes on social media impacts food consumtion
![image](https://user-images.githubusercontent.com/128729754/235527573-19343aac-69df-4805-84fe-cb8ba9f58fc7.png)

## 0. Introduction

In today's digital age, social media has changed the way we interact with the world around us, including the way we consume food. In particular, viral recipes on social media platforms such as TikTok have had a significant impact on food consumption patterns worldwide.

In this document, we will focus on the impact of viral TikTok recipes on food consumption in Spain. We will explore how the popularity of these recipes influences food choices and consumption habits among the Spanish population.



## 1. Project description

To understand the impact of viral TikTok recipes on food consumption in Spain, we utilized a multi-step methodology. Firstly, we conducted web scraping of two websites that feature popular recipe videos on TikTok. These websites were chosen based on their popularity and the volume of recipe videos they host. We extracted data from these websites to identify the most popular recipe videos that have gone viral on TikTok world wide.

In addition, we collected a dataset of food consumption in Spain over the past year. This dataset helped us to identify any notable changes in food consumption habits that may have been influenced by viral TikTok recipes.

To further verify our findings, we used Google Trends to investigate the search volume of the top viral recipe identified in the web scraping phase. 

Overall, this methodology allowed us to gain a comprehensive understanding of how viral TikTok recipes are affecting food consumption patterns in Spain.
The hypothesis of this study is that viral TikTok recipes have a significant impact on food consumption in Spain. 

Specifically, we aim to answer two questions:

** HYPOTESYS**
1. What are the most 5 popular recipes videos and ingredients featured in viral TikTok recipes in Spain? We hypothesize that the most trendy recipes and ingredients will be those that are visually appealing and easy to prepare, and that they will be heavily influenced by current food trends. (Only deep dive in the first one to understand the hypotesys)

2. Is the most viral recipe on TikTok generating a real impact in food consumption in Spain? We hypothesize that the most viral recipe videos on TikTok will have a measurable impact on food consumption habits in Spain, as reflected in search trends and changes in consumer behavior.

Overall, by investigating these two questions, we aim to gain a deeper understanding of the relationship between viral TikTok recipes and food consumption patterns in Spain. in the results.

## 2. Methodology

To perform the investigation, we proceed as follows:
1.-
  - Web scrapping of : https://www.directoalpaladar.com/actualidad-1/estas-han-sido-diez
  - We want to find the labels <h2>. 
  - We do web scrapping to get the ingredients throught a loop iterating the ingredients.  We will use words "Ingredients" and "Elaborations" to search our desired values. We will added to a new_dict.
  - We .drop to just keep the 5 top recipes to our study
  - Homogenize data throught .upper, .join and .split methods
  - Verify all the ingredients are present.
  - Web scrapping new website to comple all the recipes ingredients : url = 'https://www.spendwithpennies.com/how-to-make-a-charcuterie-board/'
  - Google tanslator method in order to keep dta in the same language as the website was in EN and all the data is in ES


- 2. Data set : cleaning and transformation:
     - The dataset from a offical source from the spanish goverment: https://www.mapa.gob.es/en/alimentacion/temas/consumo-tendencias/panel-de-consumo-alimentario/series-anuales/default.aspx
    - Columns renaming, subsets, data type change
    - Creat a list to correlate each ingredient of the recipes with the aliment group in the data set. If the ingredint has correlation, we will add de Aliment Group in the column
    - replace nan values and concatenate data
    
    
- 3.Visualizations:
    - Frequency that the category ingredients appears in the top 5 recipes
    - Annual consumtion of category ingredients (Thousands of kg)
    - Correlation graph between Volum and Price (Value)
    - Monthly consumption vs food category
    - Monthly market penetratin
![image](https://user-images.githubusercontent.com/128729754/235527060-1f9bedd1-7394-4b01-b996-fa749bdd528e.png)
![image](https://user-images.githubusercontent.com/128729754/235527184-7a2cb794-4a8e-4285-a7c8-aec1bbd8c196.png)
![image](https://user-images.githubusercontent.com/128729754/235527248-4a2c3ff2-6e01-4a4f-9283-41a9052da55c.png)
![image](https://user-images.githubusercontent.com/128729754/235527299-606efd06-faa1-4ac6-bc54-58505707906c.png)
![image](https://user-images.githubusercontent.com/128729754/235527360-f9bbd896-86c8-491a-944b-b4b0577a4f8a.png)
![image](https://user-images.githubusercontent.com/128729754/235527398-3fd0a71a-a5a7-4862-a7aa-fda084fc965e.png)


## 3. CONCLUSIONS
    
- Trendy ingredients in viral TikTok recipes were found to be simple and basic, and commonly used in households.
- There was no direct correlation between worldwide trendy recipes and their impact on food consumption in Spain.
- The study was able to determine that there was no significant impact on food consumption due to price increases during 2022.
- Seasonality was found to have a noticeable impact on the increase of certain ingredients, which may lead to changes in consumption habits in Spain.

  Overall, these conclusions does not provide valuable insights into the relationship between viral TikTok recipes and food consumption patterns in Spain.



## Libraries used
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


## Link and Resources
-  https://www.directoalpaladar.com/actualidad-1/estas-han-sido-diez
-  https://www.mapa.gob.es/en/alimentacion/temas/consumo-tendencias/panel-de-consumo-alimentario/series-anuales/default.aspx
-  https://www.spendwithpennies.com/how-to-make-a-charcuterie-board/
