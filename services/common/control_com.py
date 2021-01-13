from flask import request


def login():
    # 获取form表单参数
    user_name = request.form.get('userName')
    password = request.form.get('password')
    print("user_name",user_name)
    print("password",password)
    return {"token":'qw4521sad5'}