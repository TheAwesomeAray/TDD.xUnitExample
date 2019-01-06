from test_case_test import *

test = TestCaseTest("test_running")
test.set_up()
test.test_set_up()
test.run(TestResult())
test.test_template_method()
test.test_result()
test.test_failed_result_formatting()
test.test_failed_result()
test.test_failed_set_up()
test.test_suite()

