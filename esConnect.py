from elasticsearch6 import Elasticsearch
# es = Elasticsearch()    # 默认连接本地elasticsearch
# es = Elasticsearch(['xxx.xx.xx.xx:9200'])  # 连接指定9200端口
# es = Elasticsearch(
#     [{"host": "localhost", "port": "9200","scheme":"test"}], # 连接集群，以列表的形式存放各节点的IP地址
#     sniff_on_start=True,    # 连接前测试
#     sniff_on_connection_fail=True,  # 节点无响应时刷新节点
#     sniff_timeout=60    # 设置超时时间
# #除开链接指定的IP地址外,其他的都可以不设置,使用默认值
# )
es = Elasticsearch()

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index",doc_type="doc", id=1, body=doc)
# print(res['result'])

# res = es.get(index="user",doc_type="_doc", id=1)
# print(res['_source'])


def put_elasticsearch(index, doc_type, doc_id, body):
    '''插入数据到es里'''
    return es.index(index=index, doc_type=doc_type, id=doc_id, body=body)
