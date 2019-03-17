# import redis
# from conf.setting import HOST
# class MyRdis(object):
#     def __init__(self,host,port=6379):
#         self.r = redis.Redis(host=host,port=port)
#
#     def get(self,k):# 参数为k
#         res = self.r.get(k)#redis get数据返回的都是二进制的
#         if res:#如果get到key
#             res.decode()#二进制转成字符串
#         return res
#
#     def set(self,k,v):#入参是k-values
#         self.r.set(k,v)
#
# my_redis = MyRdis(HOST)
