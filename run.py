#!/usr/bin/env python
# coding=UTF-8
"""
@Author: STAURL.COM
@Contact: admin@staurl.com
@Project: future_loan_interface_test
@File: run.py
@Time: 2019/7/17 0:09
@Desc: S
"""
import os

from libs import HTMLTestRunnerNew
from scripts.handle_path import REPORTS_DIR
from scripts.handle_test_suite import suite

with open(os.path.join(REPORTS_DIR, 'test_resule.html'), 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='四则运算测试用例报告',
                                              description='测试两数的四则运算',
                                              tester='刀刀')
    result.run(suite)