from app.report.method.methodGeneration import MethodReportCreator

def method_analyse(methods):
    res = mc(methods)
    return res


mrc = MethodReportCreator()

def mc(m):
    get = 0
    post = 0
    head = 0
    put = 0
    path = 0
    delete = 0
    for i in m:
        data = i.split(' ')
        if len(data) != 3:
            continue
        val = data[0].upper()
        if val == "GET":
            # print(data[1])
            get += 1
        elif val == "POST":
            post += 1
        elif val == "HEAD":
            head += 1
        elif val == "OPTION":
            options += 1
        elif val == "PUT":
            put += 1
        elif val == "PATH":
            path += 1
        elif val == "DELETE":
            delete += 1
    list_ = {
        'get': get,
        'post': post,
        'head': head,
        'put': put,
        'path': path,
        'delete': delete,
    }
    mrc.create(list_)
    return list_
