load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "massplanner",
  srcs = glob(["mp/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "api",
  srcs = ["api.py"],
  deps = [
    ":massplanner",
  ],
)


py_binary(
  name = "executable",
  srcs = ["executable.py"],
  deps = [
    ":massplanner",
  ],
)
