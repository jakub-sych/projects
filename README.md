# projects

go to gym\envs

at the end of __init__.py add lines:
register(
    id='Othello8x8-v0',
    entry_point='gym.envs.othello:OthelloEnv',
    kwargs={
        'player_color': 'black',
        'opponent': 'random',
        'observation_type': 'numpy3c',
        'illegal_place_mode': 'lose',
        'board_size': 8,
    }
)
