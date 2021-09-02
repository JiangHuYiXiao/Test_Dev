# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/19 9:02
# @Software       : Python_study
# @Python_verison : 3.7


# pytest_rerunfailures重复执行
import pytest
class Test_Rerun_Failures():
    def test_case1(self):
        print('test_case1')
        assert(1==2)


    def test_case2(self):
        print('test_case2')
        assert('i' in 'hi')

if __name__ =='__main__':
    pytest.main(["-s","-v","test_rerun.py"])                        # 可以将参数放在main()中或者直接执行main()
    # pytest.main()

# 在命令窗口执行命令：
# pytest -s -v --reruns 3 （测试的文件）                           用例执行失败后立刻重复执行3次
# pytest -s -v --reruns 3 --reruns-delay 2 （测试的文件）          用例执行失败后，隔2秒重复执行一次，总共重复执行三次

