AVAILABLE_SCORES = ['arithmetic-mean', 'weighted-mean', 'f-score']


def compute_score(sentence, score, core_fes_weight):
    """ computes the confidency score for a sentence based on FE scores """

    assert score in AVAILABLE_SCORES, 'unknown scoring measure'
    scored_fes = [fe for fe in sentence['FEs'] if fe.get('score') is not None]
    if not scored_fes:
        return None

    if score == 'arithmetic-mean':
        score = (sum(fe['score'] for fe in scored_fes) / len(scored_fes))
    elif score == 'weighted-mean':
        score = sum(
                fe['score'] * core_fes_weight if fe['type'] == 'core' else 1
                for fe in scored_fes) / len(scored_fes)
    elif score == 'f-score':
        score_weight = [(fe['score'], core_fes_weight if fe['type'] == 'core' else 1)
                        for fe in scored_fes]
        score = (sum(w for s, w in score_weight) /
                             sum(w / s for s, w in score_weight))

    return score
