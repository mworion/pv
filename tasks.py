############################################################
# -*- coding: utf-8 -*-
#
#       #   #  #   #   #    #
#      ##  ##  #  ##  #    #
#     # # # #  # # # #    #  #
#    #  ##  #  ##  ##    ######
#   #   #   #  #   #       #
#
# written in python3, (c) 2019-2023 by mworion
#
# Licence APL2.0
#
###########################################################
from invoke import task
import glob


def runMW(c, param):
    c.run(param)


def printMW(param):
    print(param)


@task(pre=[])
def make_pdf(c):
    drawio = '/Applications/draw.io.app/Contents/MacOS/draw.io'
    printMW('Generate PDF')
    for fullFilePath in glob.glob('./doc/**/**.drawio', recursive=True):
        output = fullFilePath[:-6] + 'png'
        command = f'{drawio} -x -f png -o {output} {fullFilePath}'
        runMW(c, command)
    with c.cd('doc'):
        runMW(c, 'make latexpdf')
        runMW(c, 'open ./build/latex/photovoltaik.pdf')
    printMW('Generation finished\n')


@task(pre=[])
def make_html(c):
    drawio = '/Applications/draw.io.app/Contents/MacOS/draw.io'
    printMW('Generate HTML')
    for fullFilePath in glob.glob('./doc/**/**.drawio', recursive=True):
        output = fullFilePath[:-6] + 'png'
        command = f'{drawio} -x -f png -o {output} {fullFilePath}'
        runMW(c, command)
    with c.cd('doc'):
        runMW(c, 'make html')
    with c.cd('docs'):
        runMW(c, 'rm -rf *')
        runMW(c, 'rm -rf .nojekyll')
        runMW(c, 'rm -rf .buildinfo')
    with c.cd('doc/build'):
        runMW(c, 'mv html/* ../../docs')
        runMW(c, 'mv html/.nojekyll ../../docs')
        runMW(c, 'mv html/.buildinfo ../../docs')
    with c.cd('docs'):
        runMW(c, 'open ./index.html')
    printMW('Generation finished\n')
