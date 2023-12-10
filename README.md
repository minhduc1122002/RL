# Multi-Agent Reinforcement Learning
The Robot course final project about multi-agent reinforcement learning by Bui Thuy Duong, Nguyen Minh Duc, Nguyen Huynh Tra My

## Requirements
Install StarCraft2 and SMAC.

Set up StarCraft2
```
bash install_sc2.sh
```

Install all libraries and packages for this codes. Try the follow
```
pip install -r requirements.txt
```


## Training Example 

### 3M Map

* Example of training Q-MIX on dense reward:
```
python main.py --config=qmix --env-config=sc2 with learner=q_learner t_max=2000000 use_cuda=True save_model=True env_args.map_name=3m env_args.reward_sparse=False device_num=0 seed=125
```

* Example of training MASER on sparse reward:
```
python main.py --config=qmix --env-config=sc2 with learner=maser_q_learner t_max=2000000 use_cuda=True save_model=True env_args.map_name=3m env_args.reward_sparse=True device_num=0 lam=0.03 alpha=0.5 ind=1 mix=1 expl=1 dis=1 goal=maser seed=125
```

* Example of training SMMAE on sparse reward:
```
python main.py --config=smmae_qmix --env-config=sc2 with t_max=2000000 use_cuda=True save_model=True env_args.map_name=3m env_args.reward_sparse=True device_num=0 seed=125
```

## Results

### Dense Reward

| Method             |      3m      |   3s_vs_3z   |  2c_vs_64zg  |
|--------------------|--------------|--------------|--------------|
| Q-MIX              |      100     |     100      |    83.33     |
| MASER              |      100     |     100      |    87.50     |
| SMMAE              |      100     |     100      |    97.50     |

### Sparse Reward

| Method             |      3m      |   3s_vs_3z   |  2c_vs_64zg  |
|--------------------|--------------|--------------|--------------|
| Q-MIX              |      94.17   |       0      |      0       |
| MASER              |      100     |       0      |      0       |
| SMMAE              |      100     |      100     |    94.17     |
