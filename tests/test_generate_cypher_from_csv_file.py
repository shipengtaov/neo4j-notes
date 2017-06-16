# -*- coding: utf-8 -*-

import generate_cypher_from_csv_file as module


def test_generate_cypher():
    func = module._generate_cypher

    node = 'a_node'
    header = ['col1', 'col2', 'col3', 'col4']
    row = ['col1 value', 222, 6.16, True]
    assert func(node, header, row) == """CREATE (:{node} {{col1: line.col1, col2: line.col2, col3: line.col3, col4: line.col4}})
    """.format(node=node).strip()
