# Adicionar funcionalidade para ir para mais de um estado

import json

from graphviz import Digraph


class GraphVisualizer(object):

	def __init__(self, json_blueprint):
		self.data = json.load(json_blueprint)

	def print_graphs(self):

		f = Digraph('blueprint_example', filename='blueprint_example.gv')
		f.attr(rankdir='LR', size='8,0')
		self.set_nodes(f)
		self.set_edges(f)
		f.view()

	def set_nodes(self, f):

		for node in self.data['nodes']:
			style, shape, color = self.find_shape(node)
			f.node(str(node['id']), style=style, shape=shape, color=color)

	def set_edges(self, f):

		for node in self.data['nodes']:
			next_node = self.find_next_node(node)
			if next_node:
				f.edge(str(node['id']), str(next_node['id']))

	@staticmethod
	def find_shape(node):

		if node['type']=="Start":
			return None, "circle", None

		elif node['type']=="Finish":
			return "filled", "doublecircle", None
		
		return "rounded, filled", "box", "lightsalmon"

	def find_next_node(self, node):

		if node['next']:
			return self.data['nodes'][node['next']-1]
		return None


if __name__=='__main__':
	with open('blueprint_example.json') as json_file:
		graph_viz = GraphVisualizer(json_file)
	graph_viz.print_graphs()
