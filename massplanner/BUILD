load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "massplanner",
  srcs = glob(["lib/**/*.py", "recommendations/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "external_gateway_api",
  srcs = ["external_gateway_api.py"],
  deps = [
    ":massplanner",
  ],
)

py_binary(
  name = "external_data_builder",
  srcs = ["external_data_builder.py"],
  deps = [
    ":massplanner",
  ],
)
