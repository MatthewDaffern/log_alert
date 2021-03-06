import pathlib
from subprocess import run
import os
from os.path import isfile, join
from shutil import copy2 as cp
import time


def config_initializer():
    # path where the outlook files are saved.
    path_var = 'C:\\'
    config_file = open(path_var, 'r')
    config = config_file.readlines()
    config_file.close()
    return config


def path_initializer(config_path_input):
    path_input = config_path_input.split('\\')
    return pathlib.PurePath(path_input)


def delete_file(file_path):
    run(['del', file_path])
    result = 'deleted ' + file_path
    print(result)
    return result


def file_reader(file_path):
    file = open(file_path, 'r')
    file_lines = file.readlines()
    return file_lines


def alert_wrapper(str_input, alert_list_input, alert_function_input):
    alerts = alert_list_input
    for i in str_input.split(' '):
        if i in alerts:
            alert_function_input(i)


def list_of_files(path_input):
    raw_list = os.path(path_input)
    list_of_files_final = list()
    for i in raw_list:
        if isfile(i):
            list_of_files_final.append(i)
    return list_of_files_final


def alert_list():
    alerts = ()
    return alerts
# Needs alerts to go in the tuple


def file_copier(old_path, new_path):
    cp(old_path, new_path)
    return 'copied the files!'


def the_loop():
    while True:
        the_whole_daemon_func()
        time.sleep(7200)


def alert_function(str_input):
    actual_time = time.localtime(time.time())
    alert = str_input + str(actual_time)
    smtp_func(alert)
    return alert


def the_whole_daemon_func():
    the_path = path_initializer(config_initializer())
    file_list = list_of_files(the_path)
    finished_files = list_of_files()  # the final path
    for i in file_list:
        if i not in finished_files:
            file_lines = file_reader(i)
            file_copier(i, finished_files)
            for item in file_lines:
                alert_wrapper(i, alert_list(), alert_function)
    done_message = 'finished processing @ ' + time.localtime(time.time())
    log_file = open('file.log', 'r+')
    log_file.write(done_message)
    print(done_message)
    log_file.close()


# smtp_func()
# Was going to make this, but PHI requirements and my NDA prevents any
# customer data leaving the LAN without approval
