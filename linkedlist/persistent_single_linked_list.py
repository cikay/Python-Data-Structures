
class Commit:

    def __init__(self, message):
        self.message = message
        self.next = None

class Branch:

    def __init__(self, name, head_commit):
        self.name = name
        self.head_commit = head_commit


class Git:

    def __init__(self):
        self.branchs = []
        master_branch = Branch('master', None)
        self.branchs.append(master_branch)
        self.current_branch = master_branch

    def add_commit(self, message):
        commit = Commit(message)
        commit.next = self.current_branch.head_commit
        self.current_branch.head_commit = commit

    def log(self):
        print(f'****{self.current_branch.name}****')
        iter_ = self.current_branch.head_commit
        while iter_ is not None:
            print(iter_.message)
            iter_ = iter_.next

    def create_new_branch(self, branch_name):
        head_commit = self.current_branch.head_commit
        branch = Branch(branch_name, head_commit)
        self.current_branch = branch
        self.branchs.append(branch)
        print(f'Switched to a new branch: {branch_name}')

    def change_branch(self, branch_name):
        for branch in self.branchs:
            if branch.name == branch_name:
                self.current_branch = branch
                print(f'Switched to branch: {self.current_branch.name}')
                break

    def log_graph(self):
        pass

    def log_branchs(self):
        for branch in self.branchs:
            print(branch.name)

    def get_branchs(self):
        return self.branchs

    def log_current_branch(self):
        print(f'Current branch: {self.current_branch.name}')

git = Git()
commit_messages = ["first commit", "Implement Instagram"]
for commit_message in commit_messages:
    git.add_commit(commit_message)

git.create_new_branch('new_feature')
git.log_current_branch()
git.add_commit('Implement receive post event')
git.change_branch('master')
git.log_current_branch()
git.add_commit('Handle error')
for branch in git.get_branchs():
    git.change_branch(branch.name)
    git.log()
    print("**************")