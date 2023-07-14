# -*- coding: utf-8 -*-
# from IChing.Divinatories import *
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

# new_df = pd.read_csv('IChing/Data/Hex.csv', encoding='gbk')
# dict_data = new_df[new_df['value'] == 63].to_dict()
# print(new_df[new_df['value'] == 63].to_dict())
# new_qian: Hexagram = dict_hexagram(dict_data)
# print(new_qian.up_div.value.name)

class CsvIO:

    def __init__(self):
        self.df_all = pd.read_csv('IChing/Data/Hex.csv', encoding='gbk')

    def get_hexagram_dict(self, binary_hexagram) -> dict | None:
        self.df_all = pd.read_csv('IChing/Data/Hex.csv', encoding='gbk')
        hexagram_df = self.df_all[self.df_all['value'] == binary_hexagram]
        if not hexagram_df.empty:
            dict_data = hexagram_df.to_dict()
            return dict_data
        else:
            return None

    def get_content(self, binary_hexagram):
        hexagram_df = self.df_all[self.df_all['value'] == binary_hexagram]
        str_content = hexagram_df['gua_ci'].values[0]
        return str_content

    def get_yao_content(self, binary_hexagram, binary_yao):
        hexagram_df = self.df_all[self.df_all['value'] == binary_hexagram]
        print(hexagram_df)
        str_content = hexagram_df['{}'.format(int(binary_yao))].values[0]
        return str_content
