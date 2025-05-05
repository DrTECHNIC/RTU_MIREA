from collections import defaultdict


class MooreMachine:
    def __init__(self):
        self.transitions = {
            'x5/C0': {
                'tread': [{'next_state': 'x6/C0', 'cond': None}],
                'print': [{'next_state': 'x1/C1', 'cond': None}]
            },
            'x6/C0': {
                'sway': [{'next_state': 'x4/C0', 'cond': None}]
            },
            'x4/C0': {
                'order': [
                    {'next_state': 'x6/C0', 'cond': {'var': 'p', 'value': 0}},
                    {'next_state': 'x1/C1', 'cond': {'var': 'p', 'value': 1}}
                ]
            },
            'x1/C1': {
                'sway': [{'next_state': 'x4/C0', 'cond': None}],
                'tread': [{'next_state': 'x0/C1', 'cond': None}]
            },
            'x0/C1': {
                'order': [
                    {'next_state': 'x5/C0', 'cond': {'var': 'v', 'value': 0}},
                    {'next_state': 'x7/C1', 'cond': {'var': 'v', 'value': 1}}
                ]
            },
            'x7/C1': {
                'model': [
                    {'next_state': 'x6/C0', 'cond': {'var': 'q', 'value': 1}},
                    {'next_state': 'x2/C1', 'cond': {'var': 'q', 'value': 0}}
                ]
            },
            'x2/C1': {
                'model': [{'next_state': 'x3/C0', 'cond': None}]
            },
            'x3/C0': {}
        }
        self.current_state = 'x5/C0'
        self.variables = {}
        self.methods_seen = defaultdict(int)
        self.edges_seen = defaultdict(int)
        self.in_edges_count = defaultdict(int)
        self._build_in_edges()

    def _build_in_edges(self):
        for from_state, methods in self.transitions.items():
            for method, transitions in methods.items():
                for trans in transitions:
                    self.in_edges_count[trans['next_state']] += 1

    def set_p(self, value):
        self.variables['p'] = value

    def set_v(self, value):
        self.variables['v'] = value

    def set_q(self, value):
        self.variables['q'] = value

    def get_output(self):
        return self.current_state.split('/')[1]

    def has_max_in_edges(self):
        if not self.in_edges_count:
            return False
        current_in = self.in_edges_count.get(self.current_state, 0)
        return current_in == max(self.in_edges_count.values())

    def seen_method(self, method_name):
        return self.methods_seen.get(method_name, 0)

    def _handle_method(self, method):
        if not any(method in state for state in self.transitions.values()):
            return 'unknown'
        current_trans = self.transitions[self.current_state].get(method)
        if not current_trans:
            return 'unsupported'
        for trans in current_trans:
            cond = trans.get('cond')
            if (cond is None or self.variables.get(cond['var'])
                    == cond['value']):
                prev = self.current_state
                self.current_state = trans['next_state']
                self.edges_seen[(prev, self.current_state)] += 1
                self.methods_seen[method] += 1
                return
        return 'unsupported'

    def __getattr__(self, name):
        if name.startswith('run_'):
            method = name[4:]

            def wrapper():
                return self._handle_method(method)

            return wrapper
        raise AttributeError(f"'{self.__class__.__name__}'"
                             f" object has no attribute '{name}'")


def main():
    return MooreMachine()


def test_unknown_methods():
    obj = main()
    assert obj.run_hurry() == 'unknown'
    assert obj.get_output() == 'C0'
    assert obj.seen_method('test') == 0


def test_unsupported_transitions():
    obj = main()
    obj.run_tread()
    obj.run_sway()
    obj.set_p(2)
    assert obj.run_order() == 'unsupported'

    obj.current_state = 'x3/C0'
    assert obj.run_tread() == 'unsupported'
    assert obj.has_max_in_edges() is False


def test_edge_cases():
    obj = main()
    obj.in_edges_count.clear()
    assert obj.has_max_in_edges() is False

    obj = main()
    obj.in_edges_count = defaultdict(int, {'x1/C1': 2, 'x4/C0': 2})
    obj.current_state = 'x1/C1'
    assert obj.has_max_in_edges() is True


def test_variable_conditions():
    obj = main()
    obj.current_state = 'x4/C0'

    obj.variables.pop('p', None)
    assert obj.run_order() == 'unsupported'

    obj.set_p(999)
    assert obj.run_order() == 'unsupported'

    obj.variables.clear()
    assert obj.run_order() == 'unsupported'


def test_state_transitions():
    obj = main()
    states = [
        'x5/C0', 'x6/C0', 'x4/C0',
        'x1/C1', 'x0/C1', 'x7/C1',
        'x2/C1', 'x3/C0'
    ]
    for state in states:
        obj.current_state = state
        obj.run_order()


def test_main_flow():
    obj = main()
    obj.run_sway()
    obj.current_state = 'x4/C0'

    obj.set_p(0)
    obj.run_order()

    obj.current_state = 'x4/C0'
    obj.set_p(1)
    obj.run_order()

    obj.current_state = 'x0/C1'
    obj.set_v(0)
    obj.run_order()

    obj.current_state = 'x0/C1'
    obj.set_v(1)
    obj.run_order()

    obj.set_q(1)
    obj.run_model()
    obj.set_q(0)
    obj.run_model()
    obj.run_model()

    assert obj.get_output() == 'C0'
    assert obj.seen_method('order') == 4


def test_attribute_errors():
    obj = main()
    try:
        obj.invalid_method()
    except AttributeError:
        pass


def test():
    test_unknown_methods()
    test_unsupported_transitions()
    test_edge_cases()
    test_variable_conditions()
    test_state_transitions()
    test_main_flow()
    test_attribute_errors()
