include(TestingMacros)

add_regression_test(opt13 "psi;longtests;opt")
set_tests_properties(opt13 PROPERTIES COST 200)
