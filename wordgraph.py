
__author__ = 'Sarath Joseph'


### Tested with both Python 2.x and 3+ 

from bfs2 import Queue, bfs, getPath
import sys

class Node:

    def __init__(self, name):
        self.name = name
        self.neighbours = []

    __slots__ = ('name', 'neighbours')

    def __str__(self):
        result = self.name + ' : '
        for n in self.neighbours:
            result += n.name + ', '
        return result[:-1]


def buildWordGraph(file):
    w = {}
    f = open(file)
    words = f.read().split('\n')

    for word in words:

        for i in range(len(word)):
            wcard = word[:i] + '*' + word[i + 1:]
            if wcard in w:
                w[wcard].append(word)
            else:
                w[wcard] = [word]

    for key in w:
        wordlist = w[key]
        for w1 in wordlist:
            for w2 in wordlist:
                if w1 != w2:
                    inputGraph(w1, w2)


def inputGraph(word1, word2):

    if word1 not in Graph:
        node = Node(word1)
        node.neighbours.append(Node(word2))
        Graph[word1] = node
    else:

        neighbours = Graph[word1].neighbours

        if word2 not in [x.name for x in neighbours]:
            neighbours.append(Node(word2))

    if word2 not in Graph:
        node = Node(word2)
        node.neighbours.append(Node(word1))
        Graph[word2] = node
    else:

        neighbours = Graph[word2].neighbours

        if word1 not in [x.name for x in neighbours]:
            neighbours.append(Node(word1))


if __name__ == '__main__':

    Graph = {}

    #file="/usr/share/dict/words"
    file="words"

    buildWordGraph(file) 

    """ Enter Input here or pass as command line args """

    word1 = 'cold'
    word2 = 'warm'


    if len(sys.argv) > 1:


        word1=sys.argv[1]
        word2=sys.argv[2]

    if word1 in Graph:

        start = Graph[word1]
        
        if word2 in Graph:
            finish=Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors) 
            str = ''

            for p in path:

                str += p + ' -> '

            print (str[:-3])
	    
    	
        else:
             print("Word2 not in Graph") 

	
    else:
        print("Word1 not in Graph")

    


			

			
			
