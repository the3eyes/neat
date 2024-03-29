"""
Description: Genomes classes
author: syedmohsinbukhari@googlemail.com
"""
from .genes import Node, Connection


class Genome:
    """This class models genomes"""

    def __init__(self, nodes, connections):
        """Generate a Genome object.

        :param nodes: An array of nodes to initialize the genome with.
        :param connections: An array of connections to initialize the genome with.
        """
        assert type(nodes) is list
        assert type(connections) is list
        assert all(isinstance(node, Node) for node in nodes)
        assert all(isinstance(conn, Connection) for conn in connections)

        self.nodes = nodes
        self.connections = connections

    def get_node_count(self):
        """Gets number of nodes in the genome

        :return: Number of nodes in the genome
        """
        return len(self.nodes)

    def get_connection_count(self):
        """Gets number of connections in the genome

        :return: Number of connections in the genome
        """
        return len(self.connections)

    def compute(self, inp):
        """Computes output of the Neural Network encoded by this genome.

        :param inp: a list of input numbers.
        :return: the output of the underlying neural network.
        """
        assert type(inp) is list

        # TODO: Correct implementation of compute
        return self.get_connection_count() + self.get_node_count()
