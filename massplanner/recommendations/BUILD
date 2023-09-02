load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "massplanner_recommendations",
  srcs = glob(["src/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "external_api",
  srcs = ["external_api.py"],
  deps = [
    ":massplanner_recommendations",
  ],
)
