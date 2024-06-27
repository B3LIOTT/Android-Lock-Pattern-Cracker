from matplotlib import pyplot as plt
import networkx as nx
from utils import NODES


def plot_graph(pattern: str):
    """
    Plot the schema graph and the schema graph with the solution order
    :param pattern: Pattern to plot
    """
    
    graph1 = nx.Graph()
    graph2 = nx.Graph()
    
    # Add nodes
    i = 1
    for pos in NODES.values():
        # Schema graph
        graph1.add_node(i, pos=(pos[1], -pos[0]))

        # Schema graph with the solution order
        if pattern.__contains__(str(i)):
            graph2.add_node(pattern.index(str(i))+1, pos=(pos[1], -pos[0]))
        else:
            graph2.add_node(-1, pos=(pos[1], -pos[0]))
        i += 1
    
    # Add edges
    colors = ['orange']*len(NODES)
    for i in range(len(pattern) - 1):
        colors[int(pattern[i])-1] = 'green'
        colors[int(pattern[i + 1])-1] = 'green'
        graph1.add_edge(int(pattern[i]), int(pattern[i + 1]))
        graph2.add_edge(pattern.index(pattern[i])+1, pattern.index(pattern[i + 1])+1)



    plt.figure()
    nx.draw(graph1, nx.get_node_attributes(graph1, 'pos'), node_size=1000, node_color=colors, with_labels=True)
    plt.title("Pattern: " + pattern)
    plt.show()

    plt.figure()
    nx.draw(graph2, nx.get_node_attributes(graph2, 'pos'), node_size=1000, node_color=colors, with_labels=True)
    plt.title("Pattern: " + pattern)
    plt.show()
