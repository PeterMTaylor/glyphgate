from cadence_pass.syncance import Syncance
from cadence_pass.rhythm import Rhythm
from cadence_pass.anchor_way import AnchorWay
from cadence_pass.cadence_pass import CadencePass
from cadence_pass.cadence_chain import CadenceChain

def test_cadence_chain_run():
    s = Syncance(1.0)

    # Pass 1: steady → len=6, anchor=2 → (1*6)/2 = 3
    p1 = CadencePass(Rhythm("steady"), AnchorWay(2.0))

    # Pass 2: drift → len=5, anchor=1 → (3*5)/1 = 15
    p2 = CadencePass(Rhythm("drift"), AnchorWay(1.0))

    chain = CadenceChain([p1, p2])
    result = chain.run(s)

    assert result == 15.0
