# blog
Blog posts for my Medium Blog

### Interpret the "black box"
I can't stand when people say that machine learning models are consider to be a "black box". There are actually many way to interpret a machine learning model. In this post, the three questions that I want to answer: 
- How does the `feature_importance_` method in sklearn models work. Can we replicate these results?
- How can we build an 'objective based' model that we can actually determine how this prediction was computed? Can we interpret this 'black box' model? 
- What is the best interpretation library and technique? Lets compare different model interpretation techniques

We confirm in this post that we *can* interpret these black box models and explore the very nice libraries of SHAP, LIME, and treeinterpreter. 

You can see the Medium post based on this [here](https://medium.com/@mevanoff24/interpret-the-black-box-dc69031a81fa)

### Libraries
- Sklearn
- lightgbm
- SHAP
- LIME
- treeinterpreter

Most can be installed using `pip`. 
