### PROJECT
- Deacon Power Usage Forecasting Contest
- Hourly data from June 1, 2020 to August 24, 2020 for 60 specific buildings from the Korea Energy Agency
- we selected no.1 buliding, one of 60

### Team
- [BONGHOON LEE](https://github.com/Bong-HoonLee)
- [SEOBIN BANG](https://github.com/vin10ah)
- [DOYEON KIM](https://github.com/electronicguy97)
- [JAESEOK LEE](https://github.com/appleman153)
- [MOONSUN JUNG](https://github.com/JUNGMOONSUN/)

### Directory
- `archive`: history
- `data`: origin train data
- `config`: setting files for model parameters
- `doc`: documents, images, reports
- `pipeline`: ANN models, PATCHTST models
- `results`: Random Forest models
- `requirements.txt`: required libraries and packages

### How to Run
1) `pip install -r requirements.txt` to install required packages
2) Set the mode in the pipeline model's config
3) you can choose one between two options : split = train, test, predict_mode = one_step, dynamic
4) also choose select_channel_idx = <br> # 0, # elec_amount (This must be used) <br>
                                      # 1, # temp<br>
                                      # 2, # wind_speed<br>
                                      # 3, # humidity<br>
                                      # 4, # rainfall<br>
                                      # 5, # sunshine<br>
                                      # 6, # rolling_mean<br>
                                      # 7, # diff<br>
5) then, try this!

### Dataset
- Source: (https://dacon.io/competitions/official/235736/data)
- Train & Test Set
	- total data : 2040
	- Train Set: 1681
 	- validation Set: 168
	- Test Set: 168
- Features
	- 7 features are selected 5 from over 9 features <br>
	(temp, wind_speed, humidity, rainfall, sunshine) <br>
	+ 2 features are created (rolling mean, diff)
  
- Target
	- elec_amout


### Results
![image](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/assets/115579916/2d32607c-7eba-42a3-9a21-7976c3b5d6c9)


![24](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/assets/115579916/96af7cda-1e05-43cf-8192-50b26849d74b)

![168](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/assets/115579916/c9897c5b-71e8-4f1e-ab84-9ee462feee3e)



### 실험보고서
|실험보고서|발표자료|
|---|---|
|[실험보고서.docx](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/files/13936854/default.docx)|[최종발표자료.pptx](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/files/13936842/default.pptx)|
|[실험보고서.pdf](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/files/13936866/default.pdf)|[최종발표자료.pdf](https://github.com/Bong-HoonLee/EST_wassup01_TEAM4/files/13936841/default.pdf)|



