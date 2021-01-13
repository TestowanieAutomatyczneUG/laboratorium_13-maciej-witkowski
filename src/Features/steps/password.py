from behave import *
from classes.zad2 import Password


@given("create class Password and run valid_password method")
def step_impl(context):
    context.password = Password()


@when("running with empty string")
def step_impl(context):
    context.result = context.password.valid_password("")


@when("running with string with invalid length")
def step_impl(context):
    context.result = context.password.valid_password("ABc12#")


@when("running with string without capital letter")
def step_impl(context):
    context.result = context.password.valid_password("aabbcc123#")


@when("running with string without digit")
def step_impl(context):
    context.result = context.password.valid_password("AaBbCc#&$#")


@when("running with string without special char")
def step_impl(context):
    context.result = context.password.valid_password("AaBbCc123")


@then("return False")
def step_impl(context):
    assert context.result is False


@when("running with strings with all the requirements")
def step_impl(context):
    context.result = context.password.valid_password("AaBbCc123#")


@then("return True")
def step_impl(context):
    assert context.result is True


@when("running with input of type int")
def step_impl(context):
    context.result = context.password.valid_password(2115)


@when("running with input of type object")
def step_impl(context):
    context.result = context.password.valid_password({})


@then("get err")
def step_impl(context):
    assert context.result == "ERROR!"
