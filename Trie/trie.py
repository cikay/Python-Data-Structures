

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


    def words_with_prefix(self, prefix):
        current_trie = self
        words = []

        for i, char in enumerate(prefix):
            if char not in current_trie.nodes:
                return words

            if current_trie.is_leaf:
                words.append(prefix[:i])

            current_trie = current_trie.nodes[char]


        for char, c_trie in current_trie.nodes.items():
            self.add_child_trie_word(c_trie, prefix+char, words)

        return words


    def add_child_trie_word(self, trie, prefix, words):
        if trie.is_leaf:
            words.append(prefix)

        for char, c_trie in trie.nodes.items():
            self.add_child_trie_word(c_trie, prefix+char, words)


trie = Trie()
trie.insert('Muzaffer')
trie.insert('Muz')
trie.insert('Muzaff')
is_muzaffer_found = trie.search('Muzaffer')
is_muz_found = trie.search('Muz')
is_imam_found = trie.search('İmam')
print(f'is_muzaffer_found: {is_muzaffer_found}')
print(f'is_muzaffer_found: {is_muzaffer_found}')
print(f'is_imam_found: {is_imam_found}')
print('After imam inserted')
trie.insert('İmam')
is_imam_found = trie.search('İmam')
print(f'is_imam_found: {is_imam_found}')
Muzaf = trie.words_with_prefix('Muzaf')
Suleyman = trie.words_with_prefix('Süleyman')
Im = trie.words_with_prefix('İm')
print(Muzaf)
print(Suleyman)
print(Im)


