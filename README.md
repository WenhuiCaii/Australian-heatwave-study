# Australian heatwave study
This repository is for paper "Nexus of heat-vulnerable chronic diseases and heatwave mediated through tri-environmental interactions: a nationwide fine-grained study in Australia"

The heatwave index applied in this paper was generated using [heatwave_original.ipynb](https://github.com/WenhuiCaii/Australian-heatwave-study/blob/main/heatwave_original.ipynb)

The EHF index was calculated refering to *Nairn, John R., and Robert JB Fawcett. "The excess heat factor: a metric for heatwave intensity and its use in classifying heatwave severity." International journal of environmental research and public health 12.1 (2015): 227-253.*

The annual EFH index map of Australia is:
![image](https://user-images.githubusercontent.com/112457418/188405704-49efdb47-f967-4327-9d37-e0c287a72e79.png)

The Random Forest Model (RFM) was introduced to explain the potential association between heatwave and heat-vulnerable chronic diseases. To unbox the machine learning model with local explanations to enhance the interpretability of RFR models, ALE analysis was applied to RFM results by using [ RF and ALE.ipynb](https://github.com/WenhuiCaii/Australian-heatwave-study/blob/main/RF%20and%20ALE.ipynb). It will plot like:

![image](https://user-images.githubusercontent.com/112457418/188411507-ff64db27-32c3-438b-bbc3-b72b9546b23c.png)

We also tried SHAP analysis to further unbox the RFM results by using [RF and SHAP.ipynb](https://github.com/WenhuiCaii/Australian-heatwave-study/blob/main/RF%20and%20SHAP.ipynb)

