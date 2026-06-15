import streamlit as st

st.set_page_config(
  page_title="문화재 훼손"
)

st.title("문화재 훼손 예측")
st.divider()

!pip install pandas folium lxml scikit-learn seaborn koreanize-matplotlib -q

# ----------------------------------------------------------
# 한글 폰트 설치
# ----------------------------------------------------------
!apt-get -qq install fonts-nanum
!fc-cache -fv > /dev/null

# ----------------------------------------------------------
# 라이브러리 불러오기
# ----------------------------------------------------------
import requests
import pandas as pd
import numpy as np
import time
import xml.etree.ElementTree as ET
import re
import math

# 시각화
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# 지도
import folium
from folium.plugins import HeatMap, MarkerCluster

# 머신러닝
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ----------------------------------------------------------
# 한글 폰트 설정
# ----------------------------------------------------------
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

# ----------------------------------------------------------
# 구글 드라이브 연결
# ----------------------------------------------------------
from google.colab import drive #자동
drive.mount('/content/drive')
