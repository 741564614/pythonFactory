import requests

# 获取指定页数据
# import mysqlDao

import contentHandle

import esConnect


def get_page(offset):
    '''处理腾讯新闻'''
    total=0
    success=0
    # 数据源-腾讯新闻
    url = "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?" \
          "sub_srv_id=24hours&srv_id=pc&offset=%s&limit=20&strategy=1&"
    url = url % offset + "ext={%22pool%22:[%22top%22],%22is_filter%22:7,%22check_type%22:true}"
    # print(url)
    response = requests.get(url)
    # if response.status_code == 200:
    # print(response.text)
    # mydb = mysqlDao.get_connection()
    # mycursor = mydb.cursor()
    # sqlForMat = "INSERT INTO article(cms_id, article_title, article_content, article_source, article_authors,article_time, article_keyword, create_time) VALUES ('%s','%s','%s','%s','%s','%s','%s',%s)"
    # myresult = mycursor.fetchall()
    data=response.json().get('data')
    if data is not None:
        url_list=response.json().get('data').get('list')
        if url_list is not []:
                for item in url_list:
                    total+=1
                    content_url = item.get('url')
                    if str(content_url).find("omn") >= 0 or str(content_url).find(
                            "rain") >= 0:
                        res = contentHandle.resolving(content_url)
                        # print(res[0])
                        # print(res[1])
                        print("插入文章：" + res[0]+",url="+content_url)
                        body = {"title": res[0], "content": res[1] ,"source":content_url}
                        put_res=esConnect.put_elasticsearch("tencent", "article", item.get('cms_id'), body)
                        if put_res.get('_shards').get('successful') == 1:
                            success+=1
    return [total,success]
    



if __name__ == '__main__':
    i = 0
    total=0
    success=0
    while i <= 200:
        res=get_page(i)
        total+=res[0]
        success+=res[1]
        i += 20
    print("总共："+str(total)+"篇文章，成功："+str(success)+"篇")
