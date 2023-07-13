# -*- coding: utf-8 -*-
from Divinatories import *
import json
import pandas as pd

# dui = Bagua(name='兑', value=0b111)
# qian = Hexagram(name='乾', value=0b111111, div_index=1, up_div=BaguaEnum.Qian, down_div=BaguaEnum.Qian,
#                 changed_flag=0b000)
# # str_qian = qian.model_dump_json()
# dict_qian = qian.model_dump()
# # print(str_qian, type(str_qian))
# #
# # jsonData = json.loads(str_qian)
# # print(jsonData)
# # new_qian: Hexagram = dict_hexagram(jsonData)
# # print(new_qian.up_div.value.name)
#
# df = pd.DataFrame(dict_qian, index=[0])
# df.to_csv('Hex.csv')

new_df = pd.read_csv('IChing/Data/Hex.csv', encoding='gbk')
dict_data = new_df[new_df['value'] == 63].to_dict()
print(new_df[new_df['value'] == 63].to_dict())
new_qian: Hexagram = dict_hexagram(dict_data)
print(new_qian.up_div.value.name)
