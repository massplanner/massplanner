load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "massplanner_recommendations",
  srcs = glob(["src/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "proxy_server",
  srcs = ["proxy_server.py"],
  deps = [
    ":massplanner_recommendations",
  ],
)
