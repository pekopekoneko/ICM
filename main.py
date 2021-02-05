import  csv
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import matplotlib.colors as mcolors

class artist():
    def __init__(self, data):
        self.data = data
        self.figure = pd.concat([data[2:7], data[8:13]])
        self.artist_names = data[0]
        self.artists_id = data[1]
        self.duration_ms = data[14]  # 磁道持续时间，单位为毫秒（时长
        self.popularity = data[15]  # 流行度，重复的音轨(例如，来自一个单曲和专辑的相同的音轨)是独立评级的。艺术家和专辑的流行度是由歌曲的流行度计算出来的
        self.count=data[16]
    def radar(self):#绘制雷达图，涉及变量为11个中排除调式剩下的10个，标准化后的极径范围为0-1
        # 导入中文
        font_dirs = ['./font']
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        plt.rcParams['font.family'] = 'SimHei'
        feature=['danceability','energy','valence','tempo','loudness','key','acousticness','instrumentalness','liveness','speechiness','danceability']
        # 启用主题
        plt.style.use('ggplot')
        #等分图
        angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
        #角度首尾封闭
        angles = np.append(angles, angles[0])
        #数据首尾封闭
        values = np.append(np.array(self.figure), self.data[2])
        fig=plt.figure()
        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180 / np.pi, feature)
        plt.title('radar')
        ax.set_ylim(0, 1.1)
        # 添加网格线
        ax.grid(True)
        plt.show()


class year():
    def __init__(self, data):
        self.data = data
        self.figure = pd.concat([data[1:6], data[7:12]])
        self.year = data[0]
        self.duration_ms = data[12]  # 磁道持续时间，单位为毫秒（时长
        self.popularity = data[13]  # 流行度，重复的音轨(例如，来自一个单曲和专辑的相同的音轨)是独立评级的。艺术家和专辑的流行度是由歌曲的流行度计算出来的
    def radar(self):#绘制雷达图，涉及变量为11个中排除调式剩下的10个，标准化后的极径范围为0-1
        # 导入中文
        font_dirs = ['./font']
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        plt.rcParams['font.family'] = 'SimHei'
        feature=['danceability','energy','valence','tempo','loudness','key','acousticness','instrumentalness','liveness','speechiness','danceability']
        # 启用主题
        plt.style.use('ggplot')
        #等分图
        angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
        #角度首尾封闭
        angles = np.append(angles, angles[0])
        #数据首尾封闭
        values = np.append(np.array(self.figure), self.data[2])
        fig=plt.figure()
        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180 / np.pi, feature)
        plt.title('radar')
        ax.set_ylim(0, 1.1)
        # 添加网格线
        ax.grid(True)
        plt.show()


class music():
    def __init__(self,data):
        self.data=data
        self.figure=pd.concat([data[2:7],data[8:13]])
        self.artist_names=data[0]
        self.artists_id=data[1]
        """
       
        #音乐特征变量
        self.danceability=data[2]#舞蹈性,0-1浮点数
        self.energy=data[3]#能量:表示强度和活动的量度。0.0是强度最小的值，1.0是强度最大的值。
        self.valence=data[4]#效价:描述音轨所传达的乐感的一种量度。0.0是最负的值，1.0是最正的值
        self.tempo=data[5]#节奏:以每分钟节拍(BPM)计算的曲目的总体估计节奏
        self.loudness=data[6]#响度:音轨的整体响度，单位为分贝(dB)
        self.mode=data[7]#调式:音轨中调式(大调或小调)的一种表示，大调1小调0，这个雷达图里不要
        self.key=data[8]#关键:估计的整体键值的轨道
        #人声类型
        self.acousticness=data[9]#声学:是否音轨是声学(没有技术增强或电子放大)的置信度测量，0-1浮点数
        self.instrumentalness=data[10]#工具性:预测音轨中是否没有人声。工具性值越接近1.0，这首歌就越有可能不包含声乐内容。高于0.5的值表示工具性轨迹，但当值接近1.0时，置信度更高
        self.liveness=data[11]#活力:检测轨道中是否有观众。如果该值高于0.8，则表明该轨道很有可能是实时的。
        self.speechiness=data[12]#言语能力：检测曲目中口语的存在。大于0.66的值描述的曲目可能完全由口语组成。介于0.33到0.66之间的值描述了可能同时包含音乐和语音的曲目，无论是分段还是分层的（包括说唱音乐）。低于0.33的值最有可能代表音乐和其他非语音类曲目。
        """
        self.explicit=data[13]#明确的：检测曲目中的显式歌词（true（1）=yes； false（0）= no或者未知，这个变量不包括在相似度计算中
        #说明
        self.duration_ms=data[14]#磁道持续时间，单位为毫秒（时长
        self.popularity=data[15]#流行度，重复的音轨(例如，来自一个单曲和专辑的相同的音轨)是独立评级的。艺术家和专辑的流行度是由歌曲的流行度计算出来的
        self.year=data[16]
        self.release_date=data[17]
        self.song_title=data[18]


    def radar(self):#绘制雷达图，涉及变量为11个中排除调式剩下的10个，标准化后的极径范围为0-1
        # 导入中文
        font_dirs = ['./font']
        font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
        font_list = font_manager.createFontList(font_files)
        font_manager.fontManager.ttflist.extend(font_list)
        plt.rcParams['font.family'] = 'SimHei'
        feature=['danceability','energy','valence','tempo','loudness','key','acousticness','instrumentalness','liveness','speechiness','danceability']
        # 启用主题
        plt.style.use('ggplot')
        #等分图
        angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
        #角度首尾封闭
        angles = np.append(angles, angles[0])
        #数据首尾封闭
        values = np.append(np.array(self.figure), self.data[2])
        fig=plt.figure()
        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180 / np.pi, feature)
        plt.title('radar')
        ax.set_ylim(0, 1.1)
        # 添加网格线
        ax.grid(True)

        plt.show()

def similar_score(object_1,object_2):#衡量相似性的参数，为了泛用选择调用类的对应属性
    #纳入计算的参数包括音乐特征变量与人声类型的变量，采用余弦相似度计算，需要提前标准化
    """
    len_1=pow(object_1.danceability,2) +pow(object_1.energy,2) + pow(object_1.valence,2) + pow(object_1.tempo,2) + pow(object_1.loudness,2) + pow(object_1.mode,2)+pow(object_1.key,2)+ \
        pow(object_1.acousticness,2)+pow(object_1.instrumentalness,2)+pow(object_1.liveness,2)+pow(object_1.speechiness,2)
    len_2 = object_2.danceability ^ 2 + object_2.energy ^ 2 + object_2.valence ^ 2 + object_2.tempo ^ 2 + object_2.loudness ^ 2 + object_2.mode ^ 2 + object_2.key ^ 2 + \
            object_2.acousticness ^ 2 + object_2.instrumentalness ^ 2 + object_2.liveness ^ 2 + object_2.speechiness ^ 2
    muti=object_1.danceability*object_2.danceability+object_1.energy*object_2.energy+object_1.valence*object_2.valence+object_1.tempo*object_2.tempo+\
         object_1.loudness*object_2.loudness+object_1.mode*object_2.mode+object_1.key*object_2.key+object_1.acousticness*object_2.acousticness+ \
         object_1.instrumentalness*object_2.instrumentalness+object_1.liveness*object_2.liveness+object_1.speechiness*object_2.speechiness
    """
    len_1=0;len_2=0;muti=0
    for i in range(9):
        len_1 +=pow(object_1.figure[i],2)
        len_2 += pow(object_2.figure[i], 2)
        muti += object_1.figure[i]*object_2.figure[i]
    cossin=muti /(math.sqrt(len_1)*math.sqrt(len_2))
    return cossin

def radar_compare(object_1,object_2):
    # 导入中文
    font_dirs = ['./font']
    font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
    font_list = font_manager.createFontList(font_files)
    font_manager.fontManager.ttflist.extend(font_list)
    plt.rcParams['font.family'] = 'SimHei'
    feature = ['danceability', 'energy', 'valence', 'tempo', 'loudness', 'key', 'acousticness', 'instrumentalness',
               'liveness', 'speechiness', 'danceability']
    # 启用主题
    plt.style.use('ggplot')
    # 等分图
    angles = np.linspace(0, 2 * np.pi, 10, endpoint=False)
    # 角度首尾封闭
    angles = np.append(angles, angles[0])
    fig = plt.figure()
    for x in [object_1,object_2]:
        # 数据首尾封闭
        values = np.append(np.array(x.figure), x.data[2])

        # 设置为极坐标格式
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        # 填充颜色
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles * 180 / np.pi, feature)

        ax.set_ylim(0, 1.1)
    # 添加网格线
    ax.grid(True)
    plt.title('对比雷达图')
    plt.show()

if __name__ == '__main__':
    file=pd.read_csv("G:\\大学生活\\活动\\美赛2\\full_music_data.csv",engine='python')
    #reader=csv.reader(file)
    music_list=[]
    for index,row in file.iterrows():
        music_list.append(music(row))
    music_list[0].radar()
    radar_compare(music_list[0],music_list[1])
    print(similar_score(music_list[0],music_list[1]))




