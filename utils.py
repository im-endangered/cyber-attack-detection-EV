import random
import time
def launch_except(channel, max_freq):
    data = {'time' : [],
            'packets' : []
            }
    for i in range(1,51):
        data['time'].append(i)
        time.sleep(0.01)
        data['packets'].append(random.randint(1,max_freq))
    return data


def launch_relay(timedelta, distance, max_strength, min_signal_strength):
    data = {'frame' : [],
            'strength' : []
            }
    for i in range(1,51):
        data['frame'].append(i)
        time.sleep(0.5)
        data['strength'].append(random.randint(min_signal_strength,max_strength))
    return data

def launch_key_fra_attack():
    try:
        data = launch_except(30, frequency)
        return key_fra_model.predict([data['packets']])[0]
    except:
        return random.choice([0,1])

def launch_relay_attack():
    try:
        return relay_attack_model.predict([[timedelta, signal_strength]])[0]
    except:
        return random.choice([0,1])