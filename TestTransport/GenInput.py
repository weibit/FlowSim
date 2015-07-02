__author__ = 'li'

from StepByStepSimulator import *
import json

sim = StepByStepSimulator(
    CONCURRENCY=5,
    SIMTIME=0.01,
    RTT=0.000001*100)
flows = sim.geninput()

flowdict = dict()
for f in flows:
    flowdict[f.flowId] = {
        'flowSize': f.flowSize,
        'deadline': f.deadline,
        'startTime': f.startTime,
        'finishTime': f.finishTime,
    }

with open('Out/flowdump.json', 'wb') as f:
    flowdump = json.dump(flowdict, f)

print json.dumps(flowdict, sort_keys=True, indent=4, separators=(',', ': '))