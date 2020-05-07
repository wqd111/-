import string
import json
import re
import execjs
from random import randint
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
from flask import request
from flask_cors import CORS
from py2neo import Graph, Node, Relationship, NodeMatcher
from bson import json_util
# from goto import with_goto

app = Flask(__name__,
            static_folder="D:\hypertension\dist\static",
            template_folder="D:\hypertension\dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['DEBUG'] = True  # 开启 debug

mongo = PyMongo(app, uri="mongodb://localhost:27017/disease")  # 开启数据库实例
hyp_mongo = PyMongo(app, uri="mongodb://localhost:27017/Hypertension")  # 开启数据库实例

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='990119')


# graph.delete_all()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/mongo/query')
def QueryUser():
    # users = mongo.db.disease.find_one({'章节或编码': 'L2-1A0'})
    # print(type(users))
    # print(users)
    # if users:
    # return render_template('index.html')
    # else:
    # return 'No user found!'
    data = request.args
    data = data.to_dict()
    print(data)
    if (data['table'] == "icd"):
        # 查询语句
        if (data['msg']):
            condition = {}
            filter = {}
            condition['$regex'] = data['msg']
            filter["name"] = condition


            res = mongo.db.icd.find(filter)
            len_res = res.count()
            if (len_res):
                dict2 = []
                id = 1
                for i in res:
                    dict1 = {}
                    dict1["name"] = i['name']
                    dict1["chapter_or_code"] = i['ICD-11']
                    dict1["valid"] = i['valid']
                    dict2.append(dict1)
                    id = id + 1
                print(dict2)
                result = {
                    'msg': "查询成功!",
                    'code': 200,
                    'data': dict2
                }
                print("查询成功!")
                result_json = jsonify(result)
            else:
                result = {
                    'msg': "查询为空!",
                    'code': 400,
                    'data': ""
                }
                print("查询为空!")
                result_json = jsonify(result)
        else:
            res = mongo.db.icd.find().limit(10)
            print(res)
            print(type(res))
            if (res):
                dict2 = []
                id = 1
                for i in res:
                    dict1 = {}
                    dict1["name"] = i['name']
                    dict1["chapter_or_code"] = i['ICD-11']
                    dict1["valid"] = i['valid']
                    dict2.append(dict1)
                    id = id + 1
                print(dict2)
                print("查询成功!")
                result = {
                    'msg': "查询成功!",
                    'code': 200,
                    'data': dict2
                }
                result_json = jsonify(result)
            else:
                result = {
                    'msg': "查询为空!",
                    'code': 400,
                    'data': ""
                }
                print("查询为空!")
                result_json = jsonify(result)
    elif (data['table'] == "drug"):
        if (data['msg']):
            condition = {}
            filter = {}
            condition['$regex'] = data['msg']
            filter["name"] = condition
            # filter["classification"]= condition

            res = hyp_mongo.db.drug.find(filter)
            len_res = res.count()
            if (len_res):
                dict2 = []
                id = 1
                for i in res:
                    dict1 = {}
                    dict1["name"] = i['name']
                    dict1["element"] = i['element']
                    dict1["atc"] = i['atc']
                    dict1["usage"] = i['usage']
                    dict1["unto"] = i['unto']
                    dict1["classification"] = i['classification']
                    dict2.append(dict1)
                    id = id + 1
                print(dict2)
                result = {
                    'msg': "查询成功!",
                    'code': 200,
                    'data': dict2
                }
                print("查询成功!")
                result_json = jsonify(result)
            else:
                result = {
                    'msg': "查询为空!",
                    'code': 400,
                    'data': ""
                }
                print("查询为空!")
                result_json = jsonify(result)
        else:
            res = hyp_mongo.db.drug.find().limit(10)
            print(res)
            print(type(res))
            if (res):
                dict2 = []
                id = 1
                for i in res:
                    dict1 = {}
                    dict1["name"] = i['name']
                    dict1["element"] = i['element']
                    dict1["atc"] = i['atc']
                    dict1["usage"] = i['usage']
                    dict1["unto"] = i['unto']
                    dict1["classification"] = i['classification']
                    dict2.append(dict1)
                    id = id + 1
                print(dict2)
                print("查询成功!")
                result = {
                    'msg': "查询成功!",
                    'code': 200,
                    'data': dict2
                }
                result_json = jsonify(result)
            else:
                result = {
                    'msg': "查询为空!",
                    'code': 400,
                    'data': ""
                }
                print("查询为空!")
                result_json = jsonify(result)
    else:
        print("ERROR!")
        result = {
            'msg': "ERROR!",
            'code': 400,
            'data': ""
        }
        result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json


def test(datas):
    dict2 = {}
    id = 1
    for data in datas:
        dict1 = {}
        # print(data)
        # print(type(data))
        print(data['r'])
        relation = str(data['r'])
        a = relation.split('->')
        a[1] = a[1].replace('(', '')
        a[1] = a[1].replace(')', '')
        end_node = a[1]
        b = a[0].split('-')
        b[0] = b[0].replace('(', '')
        b[0] = b[0].replace(')', '')
        start_node = b[0]
        b[1] = b[1].replace('[:', '')
        b[1] = b[1].replace(']', '')
        relation = b[1]
        print(start_node)
        print()
        print(relation)
        # dict1["id"] = id
        dict1["start_node"] = start_node
        dict1["end_node"] = end_node
        dict1["relation"] = relation
        dict2[id] = dict1
        id = id + 1

    print(dict2)
    return dict2

    # dict['r'] =
    # print(type(data['r']))


def print_object(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


@app.route('/test')
def test1():
    data = request.args
    data = data.to_dict()
    print("1")
    print(data)
    return render_template('index.html')


@app.route('/graph/create')
def neo4j_graph_create():
    # 创建结点
    test_node_1 = Node('ru_yi_zhuan', name='皇帝')  # 修改的部分
    test_node_2 = Node('ru_yi_zhuan', name='皇后')  # 修改的部分
    test_node_3 = Node('ru_yi_zhuan', name='公主')  # 修改的部分
    graph.create(test_node_1)
    graph.create(test_node_2)
    graph.create(test_node_3)

    ##创建关系
    # 分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"丈夫、妻子"，两条关系都有属性count，且值为1。
    node_1_zhangfu_node_1 = Relationship(test_node_1, '丈夫', test_node_2)
    node_1_zhangfu_node_1['count'] = 1
    node_2_qizi_node_1 = Relationship(test_node_2, '妻子', test_node_1)
    node_2_munv_node_1 = Relationship(test_node_2, '母女', test_node_3)

    node_2_qizi_node_1['count'] = 1

    graph.create(node_1_zhangfu_node_1)
    graph.create(node_2_qizi_node_1)
    graph.create(node_2_munv_node_1)

    print(graph)
    print(test_node_1)
    print(test_node_2)
    print(node_1_zhangfu_node_1)
    print(node_2_qizi_node_1)
    print(node_2_munv_node_1)

    # matcher = NodeMatcher(graph)
    # nodes = matcher.match("ru_yi_zhuan")
    # new_nodes = list(nodes)
    # print(new_nodes)

    results = graph.run("MATCH ()-[r]->() RETURN r").data()
    # print(results)
    # results = list(results)
    # print(type(results))

    res = test(results)

    # for rel in graph.match(r_type="丈夫"):
    # print(rel.start_node["name"])
    # print(rel.end_node["name"])

    # new_links = get_links(results)
    # print(new_links)

    # result_json = json.dumps(results, ensure_ascii=False)
    result_json = jsonify(res)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    print(result_json)
    # print(type(result_json))

    data = request.args
    data = data.to_dict()
    print(data)

    return result_json


@app.route('/graph/query')
def neo4j_graph_query():
    matcher = NodeMatcher(graph)
    nodes = matcher.match("ru_yi_zhuan")
    new_nodes = list(nodes)
    print(new_nodes)
    return render_template('index.html')


@app.route('/user/login')
def Login():
    data = request.args
    data = data.to_dict()
    flag = 0  # 判断用户名、手机号是否为空
    print(data)
    if (data["name"]):
        res = hyp_mongo.db.User.find_one({'name': data['name'], 'password': data['password']})
        flag = 1  # 用户名不为空
    elif (data["phone"]):
        res = hyp_mongo.db.User.find_one({'phone': data['phone'], 'password': data['password']})
        flag = 1  # 手机号不为空
    else:
        pass

    # 查询到结果，登录成功
    if (res and flag):
        dict1 = {}
        dict1["id"] = str(res['_id'])
        dict1["name"] = res['name']
        dict1["password"] = res['password']
        dict1["phone"] = res['phone']
        dict1["authority"] = res['authority']
        print(dict1)
        res = {
            "msg": "登陆成功",
            "code": 200,
            "data": dict1
        }
    # res为none，密码错误，导致查找失败
    elif (flag):
        res = {
            "msg": "密码错误",
            "code": 400,
            "data": ""
        }
    else:
        res = {
            "msg": "用户名或手机号为空",
            "code": 400,
            "data": ""
        }

    result_json = jsonify(res)
    result_json.headers.add('Access-Control-Allow-Origin', '*')

    return result_json


@app.route('/user/register')
def Register():
    data = request.args
    data = data.to_dict()
    print(data)
    # 判断是否有该用户
    if (hyp_mongo.db.User.find_one({'name': data['name']})):
        result = {
            "msg": "用户名已存在",
            "code": 400,
            "data": ""
        }
        print("用户名已存在")
    elif (hyp_mongo.db.User.find_one({'phone': data['phone']})):
        result = {
            "msg": "手机号已存在",
            "code": 400,
            "data": ""
        }
        print("手机号已存在")
    else:
        # 插入数据
        data["authority"] = "user"
        res = hyp_mongo.db.User.insert_one(data)
        # print(res)
        # print(res.inserted_id)
        id = json_util.dumps(res.inserted_id)
        print(type(id))
        id = json.loads(id)
        response = {
            "id": id["$oid"]
        }
        result = {
            "msg": "成功",
            "code": 200,
            "data": response
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')

    return result_json


def IsNode(label, name):
    match_str = "MATCH(p:" + label + "{name:\"" + name + "\"}) RETURN p"
    is_in = graph.run(match_str).data()
    return is_in


def IsRelation(match_str):
    is_in = graph.run(match_str).data()
    print(is_in)
    return is_in


def NodeCreate(data):
    is_success = ''
    new_node = ''
    if (data['attr']):
        attr = eval(data['attr'])
        print("data attr exist")
        print(type(attr))
        tran = graph.begin()
        if (data['type'] == "疾病"):
            new_node = Node("疾病", name=data['name'], icd11=attr['icd11'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "药品类型"):
            new_node = Node("药品类型", name=data['name'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "药品"):
            new_node = Node("药品", name=data['name'], atc=attr['atc'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "人群"):
            new_node = Node("人群", name=data['name'])
            tran.create(new_node)
            tran.commit()
        else:
            pass
    else:
        print("data attr not exist")
        tran = graph.begin()
        if (data['type'] == "疾病"):
            new_node = Node("疾病", name=data['name'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "药品类型"):
            new_node = Node("药品类型", name=data['name'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "药品"):
            new_node = Node("药品", name=data['name'])
            tran.create(new_node)
            tran.commit()
        elif (data['type'] == "人群"):
            new_node = Node("人群", name=data['name'])
            tran.create(new_node)
            tran.commit()
        else:
            pass
    # res = {
    # "is_success": is_success
    # "node": new_node
    # }
    if (new_node):
        is_success = graph.exists(new_node)
    else:
        print("newnode不存在")
    print("is_success")
    print(is_success)
    return is_success


# 创建neo4j节点
@app.route('/graph/create/node')
def GraphCreateNode():
    # 读取前端数据：type、name、attr
    data = request.args
    data = data.to_dict()
    print(data)
    attr = data['attr']

    # 创建是否成功
    is_success = ''

    # 查询是否存在该节点
    is_in = IsNode(data['type'], data['name'])

    # 节点存在
    if (is_in):
        res = {
            "msg": "该节点已存在",
            "code": 400,
            "data": ""
        }
    # 节点不存在，创建
    else:
        is_success = NodeCreate(data)
        # 创建成功
        if (is_success):
            res = {
                "msg": "插入成功",
                "code": 200,
                "data": ""
            }
        # label不存在，创建失败
        else:
            res = {
                "msg": "该节点label不存在",
                "code": 400,
                "data": ""
            }

    result_json = jsonify(res)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    print(result_json)

    return result_json


# 创建neo4j关系
@app.route('/graph/create/relation')
# @with_goto
def GraphCreateRelation():
    # 读取前端数据，start_node，end_node，relation，都是json
    data = request.args
    data = data.to_dict()
    print(data)
    start_node = data['start_node']
    start_node = eval(start_node)
    end_node = data['end_node']
    end_node = eval(end_node)
    relation = data['relation']
    relation = eval(relation)

    # 创建是否成功
    is_success = ''

    # 判断start、end节点是否存在
    is_start = IsNode(start_node['type'], start_node['name'])
    is_end = IsNode(end_node['type'], end_node['name'])

    # 不存在start节点
    if (not is_start):
        is_success_start = NodeCreate(start_node)
        if (not is_success_start):
            res = {
                "msg": "创建start节点失败",
                "code": 400,
                "data": ""
            }
        # goto.end
    else:
        pass

    # 不存在end节点
    if (not is_end):
        is_success_end = NodeCreate(end_node)
        if (not is_success_end):
            res = {
                "msg": "创建end节点失败",
                "code": 400,
                "data": ""
            }
        # goto.end
    else:
        pass

    # 节点都存在，先判断该关系是不是存在
    pattern = "\'(\w+)\':"
    repl = "\\1:"
    str_attr = re.sub(pattern, repl, str(relation['attr']))
    print("str_attr")
    print(str_attr)
    match_str = "MATCH (p:" + start_node['type'] + "{name:\"" + start_node['name'] + "\"})-[r:" + relation[
        'name'] + str_attr + "]->(q:" + end_node['type'] + "{name:\"" + end_node['name'] + "\"}) RETURN r"
    print("match_str: " + match_str)
    is_in = IsRelation(match_str)
    if (is_in):
        print("该关系已存在")
        res = {
            "msg": "该关系已存在",
            "code": 400,
            "data": ""
        }
    # 不存在，创建neo4j关系
    else:
        create_str = "MATCH (p:" + start_node['type'] + "{name:\"" + start_node['name'] + "\"}),(q:" + end_node[
            'type'] + "{name:\"" + end_node['name'] + "\"}) CREATE (p)-[r:" + relation[
                         'name'] + str_attr + "]->(q) RETURN r"
        print(create_str)
        is_success = graph.run(create_str).data()
        if (is_success):
            res = {
                "msg": "创建关系成功",
                "code": 200,
                "data": ""
            }
        else:
            res = {
                "msg": "创建关系失败",
                "code": 400,
                "data": ""
            }

    # label.end

    result_json = jsonify(res)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    print(result_json)

    return result_json

@app.route('/graph/query/indication')
def IndicationGraph():

    data = request.args
    data = data.to_dict()
    print(data)
    if(data['table']=='indication' and data['msg'] == 'true'):
        cypher_1 = "Match (n)-[r:适应证]->(b) return n.name as name,id(n) as id,labels(n) as labels"
        cypher_2 = "Match (n)-[r:适应证]->(b) return b.name as name,id(b) as id,labels(b) as labels"
        cypher_3 = "Match (n)-[r:适应证]->(b) return r.type as value,id(n) as source,id(b) as target"

        nodes_data1 = graph.run(cypher_1).data()
        nodes_data2 = graph.run(cypher_2).data()
        links_data = graph.run(cypher_3).data()
        # print(nodes_data1)

        node_data = nodes_data2 + nodes_data1
        nodes_data = []
        for i in node_data:
            if i not in nodes_data:
                nodes_data.append(i)
        # print(nodes_data)

        # print(node_data)

        len_res = 1
        if (len_res):
            dict2 = []
            id = 1
            for i in nodes_data:
                dict1 = {}
                dict1["name"] = i['name']
                dict1["id"] = i['id']
                dict1["druggable"] = True
                if (i['labels'] ==  ["人群"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 0
                elif (i['labels'] ==  ["疾病"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 2
                else:
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                dict2.append(dict1)
                id = id + 1
            print(dict2)


        # print(dict2)

        len_res2 = 1
        if(len_res2):
            dict4 = []
            id2 = 1
            for i in links_data:
                dict3 = {}
                dict3["value"] = i['value']
                dict3["source"] = str(i['source'])
                dict3["target"] = str(i['target'])
                dict4.append(dict3)

                id2 = id2 + 1
            print(dict4)



        result = {
            'nodes_data': dict2,
            'links_data': dict4,
            'msg': '成功'
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json

@app.route('/graph/query/contra')
def ContraGraph():

    data = request.args
    data = data.to_dict()
    print(data)
    if(data['table']=='contra' and data['msg'] == 'true'):
        cypher_1 = "Match (n)-[r:禁忌证]->(b) return n.name as name,id(n) as id,labels(n) as labels"
        cypher_2 = "Match (n)-[r:禁忌证]->(b) return b.name as name,id(b) as id,labels(b) as labels"
        cypher_3 = "Match (n)-[r:禁忌证]->(b) return r.type as value,id(n) as source,id(b) as target"

        nodes_data1 = graph.run(cypher_1).data()
        nodes_data2 = graph.run(cypher_2).data()
        links_data = graph.run(cypher_3).data()
        # print(nodes_data1)

        node_data = nodes_data2 + nodes_data1
        nodes_data = []
        for i in node_data:
            if i not in nodes_data:
                nodes_data.append(i)
        # print(nodes_data)

        # print(node_data)

        len_res = 1
        if (len_res):
            dict2 = []
            id = 1
            for i in nodes_data:
                dict1 = {}
                dict1["name"] = i['name']
                dict1["id"] = i['id']
                dict1["druggable"] = True
                if (i['labels'] ==  ["人群"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 0
                elif (i['labels'] ==  ["疾病"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 2
                else:
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                dict2.append(dict1)
                id = id + 1
            print(dict2)


        # print(dict2)

        len_res2 = 1
        if(len_res2):
            dict4 = []
            id2 = 1
            for i in links_data:
                dict3 = {}
                dict3["value"] = i['value']
                dict3["source"] = str(i['source'])
                dict3["target"] = str(i['target'])
                dict4.append(dict3)

                id2 = id2 + 1
            print(dict4)



        result = {
            'nodes_data': dict2,
            'links_data': dict4,
            'msg': '成功'
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json


@app.route('/graph/query/all')
def AllGraph():

    data = request.args
    data = data.to_dict()
    print(data)
    if(data['table']=='all' and data['msg'] == 'true'):
        cypher_1 = "Match (n)-[r]->(b) return n.name as name,id(n) as id,labels(n) as labels limit 200"
        cypher_2 = "Match (n)-[r]->(b) return b.name as name,id(b) as id,labels(b) as labels limit 200"
        cypher_3 = "Match (n)-[r]->(b) return r.type as value,id(n) as source,id(b) as target limit 400"
        cypher_4 = "Match (n)-[r]->(b) return r.level as value,id(n) as source,id(b) as target limit 400"

        nodes_data1 = graph.run(cypher_1).data()
        nodes_data2 = graph.run(cypher_2).data()
        links_data1 = graph.run(cypher_3).data()
        links_data2 = graph.run(cypher_4).data()
        # print(nodes_data1)

        node_data = nodes_data2 + nodes_data1
        nodes_data = []
        for i in node_data:
            if i not in nodes_data:
                nodes_data.append(i)

        link_data = links_data1 + links_data2
        links_data = []
        for i in link_data:
            if i not in links_data:
                links_data.append(i)
        # print(nodes_data)

        # print(node_data)

        len_res = 1
        if (len_res):
            dict2 = []
            id = 1
            for i in nodes_data:
                dict1 = {}
                dict1["name"] = i['name']
                dict1["id"] = i['id']
                dict1["druggable"] = True
                if (i['labels'] ==  ["人群"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 0
                elif (i['labels'] ==  ["疾病"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 2
                elif (i['labels'] ==  ["药品类型"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                else :
                    dict1["symbolSize"] = 50
                    dict1["category"] = 3
                dict2.append(dict1)
                id = id + 1
            print(dict2)


        # print(dict2)

        len_res2 = 1
        if(len_res2):
            dict4 = []
            id2 = 1
            for i in links_data:
                dict3 = {}
                dict3["value"] = i['value']
                dict3["source"] = str(i['source'])
                dict3["target"] = str(i['target'])
                dict4.append(dict3)

                id2 = id2 + 1
            print(dict4)



        result = {
            'nodes_data': dict2,
            'links_data': dict4,
            'msg': '成功'
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json


@app.route('/graph/query/drug')
def DrugGraph():

    data = request.args
    data = data.to_dict()
    print(data)
    if(data['table']=='drug' and data['msg'] == 'true'):
        cypher_1 = "Match (n)-[r:分类]->(b) return n.name as name,id(n) as id,labels(n) as labels"
        cypher_2 = "Match (n)-[r:分类]->(b) return b.name as name,id(b) as id,labels(b) as labels"
        cypher_3 = "Match (n)-[r:分类]->(b) return r.level as value,id(n) as source,id(b) as target"

        nodes_data1 = graph.run(cypher_1).data()
        nodes_data2 = graph.run(cypher_2).data()
        links_data = graph.run(cypher_3).data()
        # print(nodes_data1)

        node_data = nodes_data2 + nodes_data1
        nodes_data = []
        for i in node_data:
            if i not in nodes_data:
                nodes_data.append(i)
        # print(nodes_data)

        # print(node_data)

        len_res = 1
        if (len_res):
            dict2 = []
            id = 1
            for i in nodes_data:
                dict1 = {}
                dict1["name"] = i['name']
                dict1["id"] = i['id']
                dict1["druggable"] = True
                if (i['labels'] ==  ["药品类型"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                elif (i['labels'] ==  ["药品"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 3
                else:
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                dict2.append(dict1)
                id = id + 1
            print(dict2)


        # print(dict2)

        len_res2 = 1
        if(len_res2):
            dict4 = []
            id2 = 1
            for i in links_data:
                dict3 = {}
                dict3["value"] = i['value']
                dict3["source"] = str(i['source'])
                dict3["target"] = str(i['target'])
                dict4.append(dict3)

                id2 = id2 + 1
            print(dict4)



        result = {
            'nodes_data': dict2,
            'links_data': dict4,
            'msg': '成功'
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json

@app.route('/graph/query/combine')
def CombGraph():

    data = request.args
    data = data.to_dict()
    print(data)
    if(data['table']=='combine' and data['msg'] == 'true'):
        cypher_1 = "Match (n)-[r:药物相互作用]->(b) return n.name as name,id(n) as id,labels(n) as labels"
        cypher_2 = "Match (n)-[r:药物相互作用]->(b) return b.name as name,id(b) as id,labels(b) as labels"
        cypher_3 = "Match (n)-[r:药物相互作用]->(b) return r.type as value,id(n) as source,id(b) as target"

        nodes_data1 = graph.run(cypher_1).data()
        nodes_data2 = graph.run(cypher_2).data()
        links_data = graph.run(cypher_3).data()
        # print(nodes_data1)

        node_data = nodes_data2 + nodes_data1
        nodes_data = []
        for i in node_data:
            if i not in nodes_data:
                nodes_data.append(i)
        # print(nodes_data)

        # print(node_data)

        len_res = 1
        if (len_res):
            dict2 = []
            id = 1
            for i in nodes_data:
                dict1 = {}
                dict1["name"] = i['name']
                dict1["id"] = i['id']
                dict1["druggable"] = True
                if (i['labels'] ==  ["人群"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 0
                elif (i['labels'] ==  ["疾病"]):
                    dict1["symbolSize"] = 50
                    dict1["category"] = 2
                else:
                    dict1["symbolSize"] = 50
                    dict1["category"] = 1
                dict2.append(dict1)
                id = id + 1
            print(dict2)


        # print(dict2)

        len_res2 = 1
        if(len_res2):
            dict4 = []
            id2 = 1
            for i in links_data:
                dict3 = {}
                dict3["value"] = i['value']
                dict3["source"] = str(i['source'])
                dict3["target"] = str(i['target'])
                dict4.append(dict3)

                id2 = id2 + 1
            print(dict4)



        result = {
            'nodes_data': dict2,
            'links_data': dict4,
            'msg': '成功'
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json

@app.route('/graph/query/indication/search')
def IndicationTable():

    data = request.args
    data = data.to_dict()
    tablevalue = 0
    print(data)

    if(data['table']=='indication' and data['msg']):
        mes = data["msg"]

        cypher_1 = "Match (n)-[r:适应证]->(b) return n.name as name1"
        cypher_2 = "Match (n)-[r:适应证]->(b) return b.name as name2"

        start_data = graph.run(cypher_1).data()
        end_data = graph.run(cypher_2).data()



        dict2 = []
        if ({'name1':mes} in start_data):
            tablevalue = 1
            cypher_3 = "Match (n)-[r:适应证]->(b) return n.name as name1,r.type as type,b.name as name2"
            data1 = graph.run(cypher_3).data()
            print(data1)

            id = 1

            for i in data1:
                dict1 = {}
                if (i['name1'] == mes and data['msg2'] == '0'):
                    dict1["disease"] = i['name1']
                    dict1["type"] = i['type']
                    dict1["drugtype"] = i['name2']
                    dict2.append(dict1)
                    id = id + 1
                elif (i['name1'] == mes and data['msg2'] == '1'):
                    if (i['type'] == '+'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                elif (i['name1'] == mes and data['msg2'] == '2'):
                    if (i['type'] == '-'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                elif (i['name1'] == mes and data['msg2'] == '3'):
                    if (i['type'] == '±'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                print(dict2)

        elif ({'name2':mes} in end_data):
            tablevalue = 1
            cypher_3 = "Match (n)-[r:适应证]->(b) return n.name as name1,r.type as type,b.name as name2"
            data1 = graph.run(cypher_3).data()
            print(data1)

            id = 1

            for i in data1:
                dict1 = {}
                if (i['name2'] == mes and data['msg2'] == '0'):
                    dict1["disease"] = i['name1']
                    dict1["type"] = i['type']
                    dict1["drugtype"] = i['name2']
                    dict2.append(dict1)
                    id = id + 1
                elif (i['name2'] == mes and data['msg2'] == '1'):
                    if (i['type'] == '+'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                elif (i['name2'] == mes and data['msg2'] == '2'):
                    if (i['type'] == '-'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                elif (i['name2'] == mes and data['msg2'] == '3'):
                    if (i['type'] == '±'):
                        dict1["disease"] = i['name1']
                        dict1["type"] = i['type']
                        dict1["drugtype"] = i['name2']
                        dict2.append(dict1)
                        id = id + 1
                print(dict2)






        result = {
            'data': dict2,
            'value': tablevalue,
            'msg': '成功',
            'code': 200
        }

    else:
        result = {
            'msg':'false'
        }

    result_json = jsonify(result)
    result_json.headers.add('Access-Control-Allow-Origin', '*')
    return result_json

# 查找
# n=nodes.match("明星",name='郭德纲')
# for i in n:
# print(i)

# rps = graph.relationships
# for r in rps:
# print(r)


# 增加
# from py2neo import Graph, Node, Relationship
# g = Graph("bolt://127.0.0.1:7687", username="neo4j", password="******")
# tx = g.begin()
# a = Node("明星", name="张鹤伦")
# tx.create(a)
# b = Node("明星", name="杨九郎")
# ab = Relationship(a, "师兄弟", b)
# tx.create(ab)
# tx.commit()
# g.exists(ab)

