def carapp(phone, time, mileage, startstep = 8):
    if mileage >= 2:
        money = startstep + (mileage - 2) * 5 + time * 0.5
    else:
        money = startstep
    print('-'*10 + '账单'+ '-'*10)
    print(' 电话：{}\n'.format(phone),'时间：{}分钟\n'.format(time), '里程数：{}公里\n'.format(mileage), '总金额：{}元'.format(money))
    print('-' * 24)
carapp(eval(input('请输入电话号码：')), eval(input('请输入时间：')), eval(input('请输入里程数：')))