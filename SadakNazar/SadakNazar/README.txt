SadakNazar - Setup (VS Code, Windows)
=====================================

1) Zip ko extract karo (OneDrive ke bahar rakho, jaise C:\DL\SadakNazar)
2) VS Code me File > Open Folder > SadakNazar folder
3) Terminal kholo (Ctrl + `) aur chalao:

   python -m venv dl_env
   dl_env\Scripts\activate
   pip install -r requirements.txt
   python check_setup.py

   (Python 3.12 best hai. Install me 5-10 min lag sakte hain.)

4) Dataset (YOLO format wala pothole dataset) is tarah rakho:

   sadak_project\data\train\images   + ...\labels
   sadak_project\data\val\images     + ...\labels   (na ho to notebook khud bana lega)
   sadak_project\data\test\images    + ...\labels   (na ho to notebook khud bana lega)

5) SadakNazar_Pothole_Priority.ipynb kholo
   - upar-right "Select Kernel" > Python Environments > dl_env
   - pehli baar EPOCHS = 2 rakho (jaldi test ke liye), phir 40
   - Run All

Tips:
- TensorFlow ka pehla import 1-2 min leta hai, normal hai.
- CPU par training dheeri hai. Asli training Google Colab (GPU) par karo:
  notebook + sadak_project folder Drive me upload karo.
- "Application Control policy blocked" aaye to Windows Smart App Control off karo
  ya Colab use karo.
