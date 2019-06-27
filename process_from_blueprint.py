import json

from graphviz import Digraph

with open('blueprint_example.json') as json_file:
    data = json.load(json_file)


def find_next_node(item):

	if item['next']:
		return data['nodes'][item['next']-1]
	return None


def main():

	f = Digraph('blueprint_example', filename='blueprint_example.gv')
	f.attr(rankdir='LR', size='8,5')
	for item in data['nodes']:
		f.node(item['type'])
	for item in data['nodes']:
		next_node = find_next_node(item)
		if next_node:
			f.edge(item['type'], next_node['type'])
	f.view()


if __name__=='__main__':
	main()
