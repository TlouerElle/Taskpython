import robot_12306


if __name__ == '__main__':
    runner = robot_12306.robot_12306()
    runner.prepare()
    runner.login()
    runner.check_time()
    runner.book()