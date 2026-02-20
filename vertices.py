import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter the number of vertices: "))

if n > 3:
        G = nx.complete_graph(n)

        plt.figure(figsize=(6, 6))
        nx.draw(
            G,
            node_color="pink",
            node_size=1500, 
            with_labels=True
        )
        plt.title(f"Complete Graph with {n} vertices")
        plt.show()
else:
        print("Minimum number of vertices should be greater than 3.")
