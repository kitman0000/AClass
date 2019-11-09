import json

class JsonHelper:

    def json_serialize(obj):
        obj_dic = JsonHelper.class2dic(obj)
        return json.dumps(obj_dic,ensure_ascii=False)

    def class2dic(obj):
        obj_dic = obj.__dict__
        for key in obj_dic.keys():
            value = obj_dic[key]
            obj_dic[key] = JsonHelper.value2py_data(value)
        return obj_dic

    def value2py_data(value):
        if str(type(value)).__contains__('.'):
            # value 为自定义类
            value = JsonHelper.class2dic(value)
        elif str(type(value)) == "<class 'list'>":
            # value 为列表
            for index in range(0, value.__len__()):
                value[index] = JsonHelper.value2py_data(value[index])
        return value