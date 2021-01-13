import pytest
from behave import *
from classes.zad1 import Hamming


@given("create class Hamming and run distance method")
def step_impl(context):
    context.hamming = Hamming()


@when("running with two empty strands")
def step_impl(context):
    context.result = context.hamming.distance("", "")


@when("running with strands with identical single letter")
def step_impl(context):
    context.result = context.hamming.distance("A", "A")


@when("running with two long identical strands where distance is 0")
def step_impl(context):
    context.result = context.hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG")


@then("return 0 distance value")
def step_impl(context):
    assert context.result == 0


@when("running with strands with different single letter")
def step_impl(context):
    context.result = context.hamming.distance("G", "T")


@then("return 1 distance value")
def step_impl(context):
    assert context.result == 1


@when("running with two long different strands where distance is 9")
def step_impl(context):
    context.result = context.hamming.distance("GGACGGATTCTG", "AGGACGGATTCT")


@then("return 9 distance value")
def step_impl(context):
    assert context.result == 9


@when("running with first strand longer than the second")
def step_impl(context):
    context.result = context.hamming.distance("AATG", "AAA")


@when("running with second strand longer than the first")
def step_impl(context):
    context.result = context.hamming.distance("ATA", "AGTG")


@when("running with empty first strand")
def step_impl(context):
    context.result = context.hamming.distance("", "G")


@when("running with empty second strand")
def step_impl(context):
    context.result = context.hamming.distance("G", "")


@then("get error")
def step_impl(context):
    assert context.result == "ERROR!"
