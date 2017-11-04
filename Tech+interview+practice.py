
# coding: utf-8

# # Tech Interview Practice
# ## Jeremy Dai

# # Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
# 
# ## Solution
# To check if some anagram of t is a substring of s, we can check whether s has all the characters within s. 
# 
# We can first compile a dictionary of counts for t and check with every possible consecutive substring sets in s. If any set is anagram of t, then we return True, else False. 
# 
# Comparing counts of all characters will can be done in constant time since there are only limited amount of characters to check. Looping through all possible consecutive substrings will take worst case O(len(s)). Therefore, the time complexity of this algorithm is O(len(s)). The space complexity is O(1) although we are creating a dictionary because we can have atmost 26 characters and thus it is bounded.
# 
# 
# 

# In[51]:

from collections import defaultdict
def question1(t,s):
    t_list = helper1(t)
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            substring = s[i:j+1]
            s_list = helper1(substring)
            if t_list==s_list:
                return True

    return False
    
def helper1(chars):
    clist = defaultdict(int)
    for c in chars:
        clist[c]+=1
    return clist
        

'''
#previous answer
It is easy test if a string is a substring of another. 
The question here is how to create all the anagrams for a string. 
Imagine we have a list of all the anagrams for a certain string t. 
Every time, we want to create a list of all the anagrams for t plus one addiontal character. 
The way doing this is add that character to any location of every anagram of t.

So in the begining t only contains one character. 
We will add characters until it contains all the characters we need. 
A for loop plus an recursive function will be used here.

def question1(t,s):
    chars=sorted(t)
    #Use helper1 fuction to get a list of all the anagrams
    t_list=helper1(chars)
    print 'The anagram list is:',t_list
    print 'The target string is:',s
    print 'One of the anagram is a substring of target string?'
    for t in t_list:
        if t in s:
            return True
    return False
    
def helper1(chars):
    #create a list of all the anagrams
    if len(chars)<=1:
        return chars
    else:
        anagrams=[]
        for anagram in helper1(chars[1:]): # get all the possible anagrams with last i-1 character(s)
            for i in range(len(chars)): # there are i combination(s) for each anagram
                new_anagram=anagram[0:i]+chars[0]+anagram[i:]
                anagrams.append(new_anagram)
        return anagrams
        
# For a string of n characters, inserting another character in any location requires n+1 times calculation.
So the runtime is O(n!)
'''
print question1('ol','love') 
print question1('','love')
print question1('love','')
print question1('ss','sometimes')


# ### Complexity
# The worst case if tryiing all the substring of s, which takes len(s)^2 times of calculation. Looping through t takes len(t) times of calculation.
# - Time: O(len(s)^2+len(t))
# - Space: O(len(s)+len(t))
# 
# 
# # Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
# 
# ## Solution
# First, everay single character is a palindrom of length 1. 
# 
# The simple solution is to list all the palindroms in the list and return the longest ones.
# 
# 1. Two situations: palindrome of even length or odd length 
# 2. Start with one character or two identical characters within the word
# 3. Check the left and right characters in the word besides the character
# 4. If they are the same, add them into the current palindrom
# 5. Repeat 3 and 4 until they are different or we run out of characters in the word
# 6. Append the index of the start character of the current palindrom in the list

# In[52]:

from collections import defaultdict

def question2(a):
    if not a:
        print 'Please give a value'
        return None
    else:
        maxlength=1
        palindrome=defaultdict(list)
        palindrome[1]=[0,len(a)-1] #st
        # Find the longest odd length palindrome with center 
        for i in range(1,len(a)-1):
            maxj=min(len(a)-1-i,i) # stop when we reach the leftmost or rightmost character
            for j in range(1,maxj+1):
                if a[i-j]!=a[i+j]:
                    break
            if a[i-j]!=a[i+j]:
                length=2*j-1
                index=i-j+1
            else:
                length=2*j+1
                index=i-j
            palindrome[length].append(index) #append the index based on its length
            if length > maxlength:
                maxlength=length # update the maxlength is the current one is longer

        # Find the longest even length palindrome with center 
        for i in range(0,len(a)-1):
            if a[i]==a[i+1]: # find two adjacent identical characters in the word
                # if the characters are the leftmost or rightmost ones
                if i==0 or i==len(a)-2:
                    if maxlength<2:
                        maxlength=2 # update the maxlength is the current one is longer
                    palindrome[2].append(i)
                else:
                    maxj=min(len(a)-2-i,i) # stop when we reach the leftmost or rightmost character
                    for j in range(1,maxj+1):
                        if a[i-j]!=a[i+1+j]:
                            break
                    if a[i-j]!=a[i+1+j]:
                        length=2*j
                        index=i-j+1
                    else:
                        length=2*j+2
                        index=i-j                  
                    palindrome[length].append(index) #append the index based on its length
                    if length > maxlength:
                        maxlength=length # update the maxlength is the current one is longer

        print 'The length of longest palindromic substring of ', a, 'is',maxlength
        print 'They are/It is:'
        for i in palindrome[maxlength]:
            print a[i:i+maxlength]
            
question2('cbcdaaa')
question2('abcbaaa')
question2('abc')
question2('')


# ### Complexity
# For a string of length n, serach every character takes n times of calculation. For each character, we need an average of n/2 times of calculation. In total, the runtime is O(n^2)
# - Time: O(n^2)
# - Space: O(n)
# 
# # Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
# 
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)
# 
# ## Solution
# We will use prim's algorithm here. Based on [wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm):
# > Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

# In[53]:

from collections import defaultdict


# In[54]:

G={'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

def question3(G):
    mst=defaultdict(list) # to store all the edges in the minimum spanning tree
    edgeweight=defaultdict(dict) # a nested dictionary to store edge weights
    queue=[] # a queue to store all the nodes not in the mst
    key={} # we will choose the node with lowest key for every iteration
    parent={} # store the previous node to create edge
    first = None # the first node we start with
    
    ### initialize
    # create parant
    for k in G:
        if not first: # if there is no first node, assign a node to it
            first = k
        key[k] = 9999
        parent[k] = None
        queue.append(k)
        for node in G[k]:    
            edgeweight[k][node[0]]=node[1]

    key[first]=0
    print 'The start node is:',first
    
    # iterate until there is no node in the queue
    
    while queue:
        u = min(queue, key=lambda q: key[q])
        queue.remove(u)
        v = parent[u]
        i = 0
        if v:
            # push the edge into the mst
            weight= edgeweight[v][u]
            mst[v].append((u,weight))
            mst[u].append((v,weight))             
        for adj in G[u]:
            v = adj[0]
            weight = adj[1]
            if v in queue and weight < key[v]:
                parent[v]=u
                key[v]=weight       
    return mst

G={'A': [('B', 2),('C', 1)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5),('A', 1)]}


print question3(G)

G={}


print question3(G)

G={'A': [('B', 2)],
   'B':[('A', 1)]}


print question3(G)


# ### Complexity
# When we use Prim's algorithm, we search every node and its adjacent node. If we have V vertex:
# - Time:O(V^2)
# - Space:O(V)
# 
# # Question 4
# Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. 
# 
# ## Solution
# First we create lists to store all the ancestors for each of the the node. Then we find the first matching node from the list.

# In[55]:

def question4(T, r, n1, n2):
    length=len(T[0])
    if length == 1:
        return 0
    else:
        ancestor1=[]
        ancestor2=[]
        # find the ancestor lists of the two leaves
        ancestor1=helper4(T,r,n1,length,ancestor1)
        #print ancestor1
        ancestor2=helper4(T,r,n2,length,ancestor2)
        #print ancestor2
        # find the least common ancestor
        for i in ancestor1:
            if i in ancestor2:
                return i
        return ancestor1[-1]

def helper4(T,r,n,length,ancestor):
    # this function is used to store the all the ancestors of a certain leaf
    for i in range(length):
        if T[i][n]==1:
            ancestor.append(i)
            if i == r:
                return ancestor
            helper4(T,r,i,length,ancestor)
    return ancestor


A=[[0, 0, 0, 0, 0],
   [1, 0, 1, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 1, 0, 0, 1],
   [0, 0, 0, 0, 0]]
print question4(A,3,0,2)
print question4(A,3,1,2)

B=[[0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [1, 0, 0, 0, 1],
   [0, 0, 0, 0, 0]]
print question4(B,3,0,4)

C=[[0]]
print question4(C, 0, 0, 0)


# ### Complexity
# First we go through the height of the tree for two leaves. The worst case takes n times of calculation (unbalanced) and the average case takes log(n) times. Then we compare the ancestor lists.
# - Time: worst case is O(n^2) and average case is O(log(n)^2)
# - Spce: worst case is O(n) and average case is O(log(n))
# 
# # Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
# 
# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None
# NEXT
# 
# ## Solution
# Firt we go though the Linkedinlist and append every item in a list. And then we serach through the list and find the item based on the index.

# In[56]:

# define the node class
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# define the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def append(self, new_node): 
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

def question5(l,m):
    length, node_list = helper5(l)
    print node_list
    print length
    print node_list[length-m] # start from the right end of the list
    
def helper5(l): 
    counter = 0 #get number of nodes
    node_list=[] #get all the nodes in the LinkedList
    current = l.head
    while current:
        node_list.append(current.data)
        current = current.next
        counter += 1
    return counter, node_list

# Test cases
# Set up some Elements
e1 = Node('I')
e2 = Node('Love')
e3 = Node('Taylor Swift\'s')
e4 = Node('Goregeous')
e5 = Node('I\'m alone')

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
one = LinkedList(e5)

# Test Question5
question5(ll,1)
question5(ll,3)
question5(one,1)


# ### Complexity
# All it needs is seraching through the list. With n nodes: 
# - Time: O(n) 
# - Space: O(n)
