from GraphVisualizer import GraphVisualizer as gv

if __name__=='__main__':
	with open('blueprint_example.json') as json_file:
		gv().print_from_json(json_file)
