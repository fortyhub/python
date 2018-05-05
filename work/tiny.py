#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tinify

tinify.key = "CA30EQeQMcnrVt8Y4Gk4YilSsnJ5OJ7G"

source = tinify.from_file("/Users/qiulibo/python/work/热带雨林1.jpg")
source.to_file("optimized.jpg")
print tinify.compression_count
