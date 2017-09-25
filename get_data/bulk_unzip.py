#!/usr/bin/env python
"""
script to unzip raw data into sub folders

author: yan z.
created: 2017.9.24

"""
from __future__ import print_function
import subprocess
import os
from os import path

import time
import copy

# unzip
# todo: change these two lines
dataParentDir = '../data/'
zipFileDir = '../data/raw/'

def make_output_dir(types):
    """
    :param types: of dir
    :return:
    """
    dirList = copy.deepcopy(types)
    dirList.append('temp')
    print('creating subdirectory......')
    for t in dirList:
        c = dataParentDir + t
        if not os.path.exists(c):
         os.mkdir(c)


def unzip_to_subdir(types, s1=0, s2=0):
    """
    make files into corresponding folders
    :param types: of dir
    :return:
    """
    types = types[s1:]

    for t in types:
        c1 = 'ls ' + zipFileDir + '*_' + t + '.log.tar.gz'
        # c1 = 'ls ../data/*_' + t +'.log.tar.gz'
        try:
            filestring = subprocess.check_output(c1, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as exc:
            print("Status : FAIL", exc.returncode, exc.output)
            continue

        # return bytes not string
        fileList = filestring.splitlines()

        print("unzipping to "+ dataParentDir + t +'/, total .gz files: ', len(fileList), '......')
        fileList = fileList[s2:]

        count = 1
        for b in fileList:
            f = b.decode("utf-8")
            targetName = f.split('/')[-1].split('.')[0]
            # unzip to temp folder

            c2 = 'tar -xvf '+ f + ' -C '+dataParentDir+'temp'
            try:
                logFiles = subprocess.check_output(c2, stderr=subprocess.STDOUT,shell=True)
            except subprocess.CalledProcessError as exc:
                print("Status : FAIL", exc.returncode, exc.output)
                continue

            for u in logFiles.splitlines():
                while path.isfile(dataParentDir +t+'/'+targetName+'.log'):
                    targetName = targetName+'_1'
                # move to correct subdir
                targetLoc = ' '+ dataParentDir + t +'/'+ targetName+'.log'
                print(count, '. adding ' + targetLoc + '......')
                count += 1
                c3 = 'mv '+dataParentDir+ 'temp/'+ u.decode('utf-8')+ targetLoc
                os.system(c3)

# def run_analytics():
#     """
#
#     :return:
#     """

if __name__ == '__main__':
    # unzip the single file
    # c0 = 'gunzip ../data/3_1.uids.gz'
    # os.system(c0)

    types = ['play', 'down', 'search']
    make_output_dir(types)
    start = time.time()
    unzip_to_subdir(types,0,0)
    end = time.time()

    print ('unzip finished, total time take: ', end-start, 's.')
    # run_analytics()

