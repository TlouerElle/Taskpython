# -*- coding: utf-8 -*-
# @Time : 2021/6/26 13:39
# @Author : Toutoutoutouer
# @Email : wes0018@aliyun.com
def verification(code):
    symbol = '!@#$%^&*()-+\/,.;[]<>?:"{}'
    nums = '1234567890'
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    result1 = 0
    result2 = 0
    result3 = 0
    result4 = 0
    for i in code:
        if i in symbol + nums + letters + '_':
            if i in symbol:
                result1 = 1
                continue
            if i in nums:
                result2 = 2
                continue
            if i in letters:
                result3 = 3
                continue
            if i == '_':
                result4 = 4
                continue
        else:
            raise Exception('密码错误原因:密码一定包含特殊符号、数字、字母、下划线')

    if result1 == 1 and result2 == 2 and result3 == 3 and result4 == 4:
        print('密码格式正确')
        exit()
    if result1 == 0 and result2 == 0 and result3 == 0 and result4 == 4:
        raise Exception('密码错误原因:缺少特殊符号、数字、字母')
    if result1 == 0 and result2 == 0 and result3 == 3 and result4 == 0:
        raise Exception('密码错误原因:缺少特殊符号、数字、下划线')
    if result1 == 0 and result2 == 2 and result3 == 0 and result4 == 0:
        raise Exception('密码错误原因:缺少特殊符号、字母、下划线')
    if result1 == 1 and result2 == 0 and result3 == 0 and result4 == 0:
        raise Exception('密码错误原因:缺少数字、字母、下划线')
    if result1 == 1 and result2 == 2 and result3 == 3 and result4 == 0:
        raise Exception('密码错误原因:缺少下划线')
    if result1 == 1 and result2 == 2 and result3 == 0 and result4 == 4:
        raise Exception('密码错误原因:缺少字母')
    if result1 == 1 and result2 == 0 and result3 == 3 and result4 == 4:
        raise Exception('密码错误原因:缺少数字')
    if result1 == 0 and result2 == 2 and result3 == 3 and result4 == 4:
        raise Exception('密码错误原因:缺少特殊符号')
    if result1 == 1 and result2 == 2 and result3 == 0 and result4 == 0:
        raise Exception('密码错误原因:缺少字母、下划线')
    if result1 == 1 and result2 == 0 and result3 == 3 and result4 == 0:
        raise Exception('密码错误原因:缺少数字、下划线')
    if result1 == 1 and result2 == 0 and result3 == 0 and result4 == 4:
        raise Exception('密码错误原因:缺少数字、字母')


try:
    code = input('请输入密码:')
    verification(code)
except Exception as err:
    print(err)
