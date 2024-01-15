# EST_wassup01_TEAM4<ul align="center">
  
![middle](https://capsule-render.vercel.app/api?type=cylinder&color=0147FF&height=150&section=header&text=Wassup&fontColor=FFFFFF&fontSize=70&animation=fadeIn&fontAlignY=55)
  
**WR(Water_Rocket)** <br>
김도연 :<br> 
방서빈 :<br>
이봉훈 : Git Branch management<br>
이재석 : <br>
정문선 : <br></ul>

### Directory
- `archive`: history
- `data`: origin train data
- `config`: setting files for model parameters
- `doc`: documents, images, reports
- `pipeline`: ANN models, PATCHTST models
- `results`: Random Forest models
- `requirements.txt`: required libraries and packages
- 
### How to Run
1) `pip install -r requirements.txt` to install required packages
2) Set the mode in the pipeline model's config
3) you can choose one between two options : split = train, test, predict_mode = one_step, dynamic
4) also choose select_channel_idx = 0, # elec_amount (This must be used)
                                      # 1, # temp
                                      # 2, # wind_speed
                                      # 3, # humidity
                                      # 4, # rainfall
                                      # 5, # sunshine
                                      # 6, # rolling_mean
                                      # 7, # diff
5) then, try this!

<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src = "https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
