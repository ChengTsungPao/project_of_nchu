## 
</br>程式說明:

step1 四個py檔放於同一目錄
step2 開啟training_parameter.py,按照指示輸入參數(可分為單一訓練或大量訓練)
step3 執行training_parameter.py,等待生成pkl
step4 開啟pkl_npz_all.py,更改程式前幾行之參數
step5 開啟pkl_npz_all.py,然後輸入pkl檔之開始時間,再輸入pkl檔之結束時間,等待執行

(如果一直有bug那就只好使用training1D.py,training2D.py,training4D.py逐一檔案調參了!!!)


</br>註:
* 預設data路徑為"./train_data" (相較於 training_*.py)
* 預設npz檔儲存路徑為"./npzfile" (相較於 pkl_npz_*.py)
* .pkl 和 pkl_npz_all.py 需保持在同一路徑
* Training_parameter.txt 為之前大量訓練之所有參數
* pkl_npz_all.py"可能"需更改的參數為dimension,kind_of_data,particle_data(控制test data的檔名)