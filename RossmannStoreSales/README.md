# Store Sales Analysis

Store sales analysis and sales prediction is probably one of the most popular tasks for companies and analysts. Relying on store analytics and hard data rather than guesswork enables companies to make smarter decisions toward higher profits, better customer satisfaction, and better efficiency in their stores. 


## Motivation

The motivation for this particular project was to explore a classic time series problem and get a good handle on *Time Series Analysis* with the [statsmodels](https://www.statsmodels.org/stable/index.html) and [fbprophet](https://facebook.github.io/prophet/) libraries while being able to clearly communicate these results with visuals and machine learning. 


## Summary of Results
- We determined that store promotions have a large affect on store sales. However certain dates are much more valuable than others. 
- We took one example store and analyzed the seasonality and trend in the store sales with Time Series Analysis techniques. The particular store analyzed was in a downward trend. Rossmann should try to put more attention on this store. 
- We trained a model to predict a certain store sales for an arbitrary future date and analyzed how store managers could help influence profits by selecting correct promotional dates.



## Files
- [Data Exploration notebook](https://github.com/mevanoff24/blog/blob/master/RossmannStoreSales/Data%20Exploration.ipynb). Analyzes store sales based on features and Time Series Analysis 
- [Model](https://github.com/mevanoff24/blog/blob/master/RossmannStoreSales/Model.ipynb). LightGBM model predicting sales for a given store
- `utils.py`. Some utility functions. 




## Libraries
- pandas
- numpy
- matplotlib
- seaborn
- lightgbm
- statsmodels
- fbprophet

Most can be installed using `pip`.


## Acknowledgements

Special thanks from all the [Kagel Kernels](https://www.kaggle.com/c/rossmann-store-sales/kernels) and [fast.ai](http://www.fast.ai/)
