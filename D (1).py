
import pandas as pd

import networkx as nx
import matplotlib.pyplot as plt
csv_file = "c:/Users/10746/Documents/python/influence_data.csv"

data = pd.read_csv(csv_file)
print(data["influencer_id"])
def create_Graph(data):#图的基本介绍：由字典组成，influencers组成键，
    #连接到的元组（followers,followers的年代,followers的派别）组成的list是对应的值，且list的第一项是键的年份
    influencers = []
    graph = {}
    for i in range(len(data["influencer_id"])):
        id = data.at[i,"influencer_id"]#对每一个id遍历
        if id not in influencers:#如果是全新的influencer，就加入新的字典值
            influencers.append(id)
            graph[id]=[data.at[i,"influencer_active_start"],data.at[i,"influencer_main_genre"]]#前两项是对应的年份与派别
        graph[id].append((data.at[i,"follower_id"],data.at[i,"follower_active_start"],data.at[i,"follower_main_genre"]))#把这一行对应的follower加入字典中
    return graph


def Graph_out(graph,id):#返回id对应的followers
    return graph[id]

def Graph_in(graph,id):#返回id对应的influencers
    influencer = []
    year = graph[id][0]
    genre = graph[id][1]
    for ids in graph:
        if (id,year,genre) in graph[ids][2:]:
            year_i = graph[ids][0]
            genre_i = graph[ids][1]
            influencer.append((ids,year_i,genre_i))
    return influencer


def create_sub(graph,id):#建立子网（主要是用来画图的）
    sub_graph = {}
    influencer = Graph_in(graph,id)#得到入度点
    followers = Graph_out(graph,id)#得到出度点
    year = graph[id][0]
    genre = graph[id][1]
    for influencer_i in influencer:
        id1 = influencer_i[0]
        year_1 = influencer_i[1]
        genre1 = influencer_i[2]
        followers_1 = [year_1,genre1,(id,year,genre)]#入度点一定会到达目前的点，提前初始化
        for follower_i in followers[2:]:#寻找followers与influencer的联系
            if follower_i in graph[id1]:
                followers_1.append(follower_i)#如果出度点同时也是入度点的follower，则加进去
        sub_graph[id1] = followers_1

    for follower_i in followers[2:]:
        id2 = follower_i[0]
        year_2 = follower_i[1]
        genre2 = follower_i[2]
        followers_2 = [year_2,genre2]
        for influencer_i in influencer:#寻找followers与influencer的联系
            if influencer_i in graph[id2]:
                followers_2.append(influencer_i)#如果入度点同时也是出度点的follower，则加进去
        sub_graph[id2] = followers_2
    sub_graph[id] = followers
    return sub_graph

def influence_count(graph,id):#计算影响力
    power = 0
    for follower_i in graph[id][2:]:
        k_1 = 1
        k_2 = 1
        if graph[id][1]!=follower_i[2]:#如果跨领域：影响力*1.2
            k_1 = 1.2
        if follower_i[1]<graph[id][0]:#如果有老一辈粉丝：影响力*1.2
            k_2 = 1.2
        power = power + k_1*k_2*abs(follower_i[1]-graph[id][0])#基础影响力使用时间差
    return power

def draw_graph(graph):#画图
    
    g = nx.DiGraph()#无多重边有向图
    
    g.add_nodes_from(graph.keys())
    for id in graph.keys():
        for follower in graph[id][2:]:
            g.add_edge(id,follower[0]) # 添加一条边起点为x,终点为y
    pos = nx.shell_layout(g)
    nx.draw(g, with_labels=True,pos = pos,node_size = 100,alpha = 0.7,edge_color = "grey")
    plt.show()

graph = create_Graph(data)
years_power = {1930:[],1940:[],1950:[],1960:[],1970:[],1980:[],1990:[],2000:[],2010:[]}#根据年份分类
power = []
for id in graph.keys():
    if len(graph[id])>10:#只考虑有大于10个粉丝的
        power.append((id,influence_count(graph,id)))
        years_power[graph[id][0]].append((id,influence_count(graph,id)))

sub_graph = create_sub(graph,285272)
draw_graph(sub_graph)

print(years_power)

