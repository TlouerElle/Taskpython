import requests
import json
import re
import xlsxwriter
from bs4 import BeautifulSoup

print("RUNNING……")

headers = {
    'accept-language': 'zh-CN,zh;q=0.9',
    'origin': 'https://www.zhihu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/69.0.3497.100 Safari/537.36 '
}
cookies = {'__snaker__id': 'XBIh8p1ZN5yXiEGK', ' SESSIONID': 'B2cDVzHGMkdNc50LNQOioxTh03vBSwcbYoVAgtgJYGt',
           ' osd': 'UVgTB0KRdZg84GhgLJYcjaOCSIo60EH5dbwRLmnWHfpwjldTZnjvKlrpbWQjWNjP8LxE_i11AphsMaxH7bIxtjM=',
           ' JOID': 'U1sVAE2Tdp4772pjKpETj6CET4U400f-er4SKG7ZH_l2iVhRZX7oJVjqa2MsWtvJ97NG_StyDZpvN6tI77E3sTw=',
           ' _zap': 'd02986b4-70fe-42fb-8085-5e16f21dee94',
           ' d_c0': '"APCclWon4xOPTt2Y_tt9-RTWVmMlF747m2o=|1634441559"', ' ISSW': '1', ' _9755xjdesxxd_': '32',
           ' YD00517437729195%3AWM_TID': 'R%2FCIRr0FPExERVAUEEd78PbM48ZAvP4R',
           ' _xsrf': '8vMQdGUA1PL1JU1frQxdyGfciWm1Z1at', ' __snaker__id': 'tupzBVKqwQj1SWWs',
           ' YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6ee9abc3eba9eb6aad07c8ca88eb6c45a969b8f85f565b289b8d1d842adb39cd6b82af0fea7c3b92aae9cfda3d872afa9f890f473bb8dbfaece6b88b08587ec219588afb9b46a89f5fb9acc599b8afb9ad834bc87bdb3d343b8a9e18ed5469b8ea085b57dbab7f8a6b373a9ada9aee27ca7a9aca3d561f5888597c23b909984a6b3688eadbdd3b269f79098afe26591ac8a94f67e888e84baf04595ab878db653edb0858ddc5096ec9cd1d037e2a3',
           ' YD00517437729195%3AWM_NI': 'nD3BUzmw8oqyySqMOaDpKfi%2BWXaX1bK%2B5yISYV5yU8xYsRPItw%2FmVNYRPd6wzi8E0yksgMcpewdBVk7XKvC1LGLE0lNss23c5PXNcoStFswvDRLYmOWuIl7Y%2FpKlYDV4T0M%3D',
           ' capsion_ticket': '"2|1:0|10:1639813958|14:capsion_ticket|44:ZGFjMWNlZWY3NmI2NGNmYzhkNjBlYjEyNjVmODc3NjU=|76f7e6c3fe775c93ae4f368e62b19f55b33b0d56c65dbf2a2f7c6a96dd4ad29c"',
           ' oauth_from': '"/settings/account"', ' tst': 'r',
           ' gdxidpyhxdE': 'x8sxCJfTZ1OCGL8PN3w76i9WViDOOhC4%2FS%5COZrGM%2BCkrJwVDsCuGnadtXzS48p2NsBnmv0fwxx1%5C'
                           '%2BpRT%2BHN7ypmMfRz%2BppPol8eGbSnY3Qw%5CVw1%2FzlnULv%2FGZA4ynn6EktcovwMn8YP%2FyDLaY7'
                           '%2F1Dr21pkv7y2OkUL7kU3fLy%2F3zGDUa%3A1639819105776',
           ' captcha_session_v2': '"2|1:0|10:1639818961|18:captcha_session_v2|88'
                                  ':czloUzdtL0JjV2Z4RFl2RHp3ajhCMEpNVUtXeDBMYmxRZUhDb3R3TDRadXlBRStXcGh1dGJnUnZIT1lXd0tKMw==|346b981bcbd158c95d92a188be54440d0884c23aacb354f7c1ccd7e5c34e98e5"',
           ' captcha_ticket_v2': '"2|1:0|10:1639818967|17:captcha_ticket_v2|704'
                                 ':eyJ2YWxpZGF0ZSI6IkNOMzFfYUxxSl9ONWhCNXc0OFdHLUlROWIxbmNmeE5OZFV0bVpRWEoud0d0YVdYdnJudGREbV94SVguWklwbEQ3cE8tSENXMEZlbG1PcGZNOVRwdWdDZzV4dWpDZVZmTmRLUmMwZnJ6djZaNV95QmFyLXplN3Fxd29ieWZ4cnZMQ1JXdDZ5V2xkdi1YMldGS2ZLaTZNU1o0eGJIRVNrNS4xQ1diLnJIMTRNZDhienZ6ckdvSkktMlF1LWVWNE5xSFl6VkM3VzhudkZFeVlYOUdvX0hpa0tMVTd3SUI2SVh2eUV2V1dyQzd2amJZeVI0ekdnTzZCUHRybmNKWXpQUWFiSG9XRDhzVnVGWVd5Z3BIV1hMdWdHelpiYTVndEZ1aHNIeVR1ajJwQzUtWFgwSlJ4ZFN1c041YUZncHVrRWZRNlRlcjFoaTRtdUNJcC1IdUowWGV2aWd5eWl5LTBjaDVvdEl6MTJCbm5PWWhHVTk3QUlJSEJwUGlScXdWWl9qREZVOXFsdXRYWDdIQU14ZktfV1pMZGxhWDJmd1A4Tmk3RlJRcjhuUjd0ZXk2NW1fNVZEeGdSUmcycU0wSkR6Y0RDMGx4N1FvZWJnYlBNeFVYT2paODZ1VUZoMHJrV2o3enJSSWtCMDlINElCZHkueUR1a2YxOHVrNHhqaWhJc1NJMyJ9|f6e1a47a0847f9a7a424f11abe6e0fd2ce3031138f9dcb6f5646be8cb24631be"',
           ' z_c0': '"2|1:0|10:1639818967|4:z_c0|92'
                    ':Mi4xdF9xRERnQUFBQUFBOEp5VmFpZmpFeVlBQUFCZ0FsVk4xX1NxWWdCQjZjWWJRYmN1czRWQXlWTFhiZWxjb1pXSTZ3'
                    '|04cb29d6d8e905066113bcf49c6c86f536fa533aef26957125947dfeca61b92b"',
           ' NOT_UNREGISTER_WAITING': '1', ' KLBRSID': 'af132c66e9ed2b57686ff5c489976b91|1639818983|1639813569 '}


def extract_answer(s):
    temp_list = re.compile('<[^>]*>').sub("", s).replace("\n", "").replace(" ", "")
    return temp_list


def getAnswers(qid):
    start_url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset=0&platform=desktop&sort_by=default".format(qid, 0)

    next_url = [start_url]
    count = 0

    # 打开xlsx文件
    workbook = xlsxwriter.Workbook("知乎回答%s.xlsx" % qid)
    worksheet = workbook.add_worksheet()

    # 爬取知乎问题号为qid的所有回答
    for url in next_url:
        html = requests.get(url, headers=headers, cookies=cookies)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text, "lxml")
        content = str(soup.p).split("<p>")[1].split("</p>")[0]
        c = json.loads(content)

        if "data" not in c:
            print("获取数据失败，本 ip 可能已被限制。")
            print(c)
            break

        answers = [extract_answer(item["content"]) for item in c["data"] if extract_answer(item["content"]) != ""]

        for answer in answers:
            count = count + 1
            worksheet.write("A%s" % count, count)
            worksheet.write("B%s" % count, answer)

        next_url.append(c["paging"]["next"])
        if c["paging"]["is_end"]:
            break

    # 关闭xlsx文件
    workbook.close()


if __name__ == '__main__':
    getAnswers(27544958)
    print("END")
    print("Please check your file QAQ")
