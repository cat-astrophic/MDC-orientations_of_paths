## Description

This script takes a user chosen orientation of a path and outputs a minimum dominator coloring of that oriented path via the algorithm presented in *A Linear Algorithm for Minimum Dominator Colorings of Orientations of Paths*.

Built in options for path orientations include a directed path, a path with no vertices of out-degree one (depending on the parity of the path length, it is possible that the final vertex has out-degree one), a random orientation, and a custom orientation.

Along with a vertex colored digraph, the algorithm also outputs the colors assigned to each vertex as a list.

The default path length is set to 8 vertices.

## Future Improvements

Eventually I intend to make the interface prettier.

## Citation

The paper is currently under review at *Transactions on Combinatorics*. You can cite the preprint version of this paper as follows:

@article{cary2019linear,\
&nbsp;&nbsp;&nbsp;&nbsp;title = {A Linear Algorithm for Minimum Dominator Colorings of Orientations of Paths},\
&nbsp;&nbsp;&nbsp;&nbsp;author = {Cary, Michael},\
&nbsp;&nbsp;&nbsp;&nbsp;journal = {arXiv preprint arXiv:1906.04523},\
&nbsp;&nbsp;&nbsp;&nbsp;year = {2019}\
}
