{\rtf1\ansi\ansicpg1251\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red242\green239\blue236;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c96078\c94902\c94118;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
# \uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1083 \u1103 \u1077 \u1084  \u1079 \u1072 \u1074 \u1080 \u1089 \u1080 \u1084 \u1086 \u1089 \u1090 \u1080 \
from selenium import webdriver\
from selenium.webdriver.chrome.service import Service\
# \uc0\u1059 \u1082 \u1072 \u1079 \u1099 \u1074 \u1072 \u1077 \u1084  \u1075 \u1076 \u1077  \u1085 \u1072 \u1093 \u1086 \u1076 \u1080 \u1090 \u1089 \u1103  ChromeDriver (\u1085 \u1072 \u1096  Dockerfile \u1091 \u1078 \u1077  \u1089 \u1082 \u1072 \u1095 \
chromedriver_path = "/usr/bin/chromedriver"\
# \uc0\u1054 \u1087 \u1094 \u1080 \u1080  \u1076 \u1083 \u1103  Chrome\
options = webdriver.ChromeOptions()\
options.add_argument('--ignore-certificate-errors')  # Ignores\
options.add_argument('--headless')  # Runs Chrome in headless m\
options.add_argument('--disable-gpu')  # Disables GPU hardware\
options.add_argument('--no-sandbox')  # Bypass OS security mode\
options.add_argument('--window-size=1920x1080')  # Sets the ini\
options.add_argument('--ignore-certificate-errors')\
# \uc0\u1048 \u1085 \u1080 \u1094 \u1080 \u1072 \u1083 \u1080 \u1079 \u1072 \u1094 \u1080 \u1103  Driver\
s = Service(chromedriver_path)\
driver = webdriver.Chrome(service=s, options=options)\
# \uc0\u1054 \u1090 \u1082 \u1088 \u1099 \u1090 \u1100  \u1089 \u1090 \u1088 \u1072 \u1085 \u1080 \u1094 \u1091 \
driver.get("http://qa-stand-login.inzhenerka.tech/login")\
# \uc0\u1053 \u1072 \u1087 \u1077 \u1095 \u1072 \u1090 \u1072 \u1090 \u1100  \u1085 \u1072 \u1079 \u1074 \u1072 \u1085 \u1080 \u1077  \u1089 \u1090 \u1088 \u1072 \u1085 \u1080 \u1094 \u1099 \
print(driver.title)
\fs24 \cb1 \

\fs32 \cb3 # \uc0\u1044 \u1077 \u1088 \u1078 \u1072 \u1090 \u1100  \u1073 \u1088 \u1072 \u1091 \u1079 \u1077 \u1088  \u1086 \u1090 \u1082 \u1088 \u1099 \u1090 \u1099 \u1084  \u1087 \u1086 \u1089 \u1083 \u1077  \u1079 \u1072 \u1074 \u1077 \u1088 \u1096 \u1077 \u1085 \u1080 \u1103  \u1090 \u1077 \u1089 \u1090 \u1072  (\u1085 \u1072 \u1087 \u1088 \u1080 \u1084 \u1077 \u1088 , 10\
import time\
time.sleep(10)\
# \uc0\u1047 \u1072 \u1082 \u1088 \u1099 \u1090 \u1100  \u1086 \u1082 \u1085 \u1086  \u1073 \u1088 \u1072 \u1091 \u1079 \u1077 \u1088 \u1072 \
driver.quit()\
}