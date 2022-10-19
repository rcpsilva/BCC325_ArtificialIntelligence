def explain(observations, kb, explanation = set()):
    if observations:
        a = observations[0]

        if a in kb['assumables']:
            return explain(observations[1:],kb,explanation|{a})
        else:
            bodies = kb['rules'][a]
            explanations = []

            for body in bodies:
                explanations += explain(body + observations[1:],kb,explanation)

            return explanations
    return [explanation]