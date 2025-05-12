import multiprocessing

bind = "0.0.0.0:7170"
workers = multiprocessing.cpu_count() * 2 + 1