"""
   作业:定义结构数据,存储一下信息
   --多个城市多个景区和美食
   "北京"
        "景区":"天安门","天坛","故宫"
        "美食":"驴打滚","豆汁"
   "四川"
        "景区":"九寨沟","宽窄巷子"
        "美食":"火锅","串串香"
   ----打印北京所有美食(一行一个)
   ----打印所有城市(一行一个)
   ----(扩展)打印所有城市的所有景区(一行一个)
"""
#方法一:
dict01={"北京":{"景区":["天安门","天坛","故宫"]},
      "四川":{"景区":["九寨沟", "宽窄巷子"]}}
dict02={"北京":{"美食":["驴打滚","豆汁"]},
      "四川":{"美食":["火锅","串串香"]}}
# ----打印北京所有美食(一行一个)
for item in dict02["北京"]["美食"]:
    print(item)
# ----打印所有城市(一行一个)
for city in dict01:
    print(city)
# ----(扩展)打印所有城市的所有景区(一行一个)
for spot in dict01.values():
    for value in spot.values():
        for spott in value:
            print(spott)