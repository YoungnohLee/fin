from __future__ import annotations

# customized config from finrl.config.py
class config_rolling(self, sma=30, lma=60):
    
    DATA_SAVE_DIR = 'datasets'
    TRAINED_MODEL_DIR = 'trained_models'
    TENSORBOARD_LOG_DIR = 'tensorboard_log'
    RESULTS_DIR = 'results'
    
    # date format = '%Y-%m-%d'
    TRAIN_START_DATE = '2010-01-01'
    TRAIN_END_DATE = '2021-10-01'
    
    TEST_START_DATE = "2021-10-02"
    TEST_END_DATE = "2022-11-01"
    
    TRADE_START_DATE = '2021-11-02'
    TRADE_END_DATE = '2023-05-28'
    
    # stockstats technical indicator columns names
    # # check https://pypi.org/project/stockstats/ for different names
    def INDICATORS(sma=30, lma=60):
        INDICATORS = [
           'macd',
           'boll_ub',
           'boll_lb',
           'rsi_30',
           'cci_30',
           'dx_30',
           f'close_{sma}_sma'
           f'close_{lma}_sma' 
        ]
        return INDICATORS

    # Model Parameters
    A2C_PARAMS = {"n_steps": 5, "ent_coef": 0.01, "learning_rate": 0.0007}
    PPO_PARAMS = {
        "n_steps": 2048,
        "ent_coef": 0.01,
        "learning_rate": 0.00025,
        "batch_size": 64,
    }
    DDPG_PARAMS = {"batch_size": 128, "buffer_size": 50000, "learning_rate": 0.001}
    TD3_PARAMS = {"batch_size": 100, "buffer_size": 1000000, "learning_rate": 0.001}
    SAC_PARAMS = {
        "batch_size": 64,
        "buffer_size": 100000,
        "learning_rate": 0.0001,
        "learning_starts": 100,
        "ent_coef": "auto_0.1",
    }
    ERL_PARAMS = {
        "learning_rate": 3e-5,
        "batch_size": 2048,
        "gamma": 0.985,
        "seed": 312,
        "net_dimension": 512,
        "target_step": 5000,
        "eval_gap": 30,
        "eval_times": 64,  # bug fix:KeyError: 'eval_times' line 68, in get_model model.eval_times = model_kwargs["eval_times"]
    }
    RLlib_PARAMS = {"lr": 5e-5, "train_batch_size": 500, "gamma": 0.99}