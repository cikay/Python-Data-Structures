

class Trie:

    def __init__(self) -> None:
        self.nodes = {}
        self.is_leaf = False
    

    def insert(self, word):
        current_trie = self
        for char in word:
            current_trie.nodes.setdefault(char, Trie())
            current_trie = current_trie.nodes[char]

        current_trie.is_leaf = True


    def search(self, word):
        current_trie = self
        for char in word:
            if char not in current_trie.nodes:
                return False
            
            current_trie = current_trie.nodes[char]

        return current_trie.is_leaf


trie = Trie()
trie.insert('Muzaffer')
is_muzaffer_found = trie.search('Muzaffer')
is_imam_found = trie.search('İmam')
print(f'is_muzaffer_found: {is_muzaffer_found}')
print(f'is_imam_found: {is_imam_found}')
print('After imam inserted')
trie.insert('İmam')
is_imam_found = trie.search('İmam')
print(f'is_imam_found: {is_imam_found}')

            

