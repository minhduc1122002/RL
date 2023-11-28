from .q_learner import QLearner
from .maser_q_learner import maserQLearner
from .smmae_q_learner import SMMAEQLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY['maser_q_learner'] = maserQLearner
REGISTRY["smmae_q_learner"] = SMMAEQLearner
