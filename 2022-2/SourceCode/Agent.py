
class Agent():
    def __init__(self, env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]

    def act(self):
        while self.F:
            path = self.F.pop(-1)

            action = {'position':path[-1]}
            self.percepts = self.env.change_state(action)

            if path[-1] == self.percepts['goal']:
                return path
            else:
                for n in self.percepts['neighbors']:
                    if n not in path:
                        self.F.append(path + [n])

        print('Impossible!')
        return []








