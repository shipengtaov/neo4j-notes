#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""读取 csv 文件（需要带 header），生成 cypher 语句
"""

from __future__ import unicode_literals

import sys
from os import path
from argparse import ArgumentParser
from decimal import Decimal

import pandas
import pyperclip

from compat import int_type, force_text

float_type = (float, Decimal)


def _generate_cypher(node, headers, row, alias='line'):
    cypher = "CREATE (:{} {{".format(node)
    for i, header in enumerate(headers):
        val = row[i]
        # if isinstance(val, bool):
        #     tmp = '{prop}: toBoolean({alias}.{prop}), '
        # elif isinstance(val, int_type):
        #     tmp = '{prop}: toInteger({alias}.{prop}), '
        # elif isinstance(val, float_type):
        #     tmp = '{prop}: toFloat({alias}.{prop}), '
        # else:
        #     tmp = '{prop}: {alias}.{prop}, '
        tmp = '{prop}: {alias}.{prop}, '
        cypher += tmp.format(prop=header, alias=alias)
    cypher = cypher.rstrip(', ')
    cypher += '})'
    return cypher


def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='csv file')
    parser.add_argument('-c', '--clipboard', action="store_true", help='auto copy result to clipboard')
    args = parser.parse_args()

    curdir = path.dirname(path.abspath(__file__))
    file = args.file
    # relative filepath
    if not file.startswith('/'):
        file = path.join(curdir, file)
    if not path.exists(file):
        print('{} does not exist'.format(file))
        return

    pd = pandas.read_csv(file, encoding='utf-8')
    headers = list(pd.columns)
    row = list(pd.iloc[0])
    node = path.basename(file).rsplit('.', 1)[0]

    alias = 'line'
    cypher = _generate_cypher(node, headers, row, alias)
    cypher = 'LOAD CSV WITH HEADERS FROM "{file}" as {alias} '.format(file=file, alias=alias) + cypher
    print("\n" + "="*30 + " Result " + "="*30 + "\n")
    print(cypher)
    print("\n")

    if args.clipboard:
        pyperclip.copy(cypher)
        print('result copied to your clipboard')


if __name__ == '__main__':
    main()
