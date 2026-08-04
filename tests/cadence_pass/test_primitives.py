from cadence_pass.syncance import Syncance
from cadence_pass.rhythm import Rhythm
from cadence_pass.anchor_way import AnchorWay

def test_syncance_amplify():
    s = Syncance(2.0)
    assert s.amplify(2.0) == 4.0

def test_rhythm_shift():
    r = Rhythm("steady")
    assert r.shift("chaotic") == "chaotic"

def test_anchor_way_stabilise():
    a = AnchorWay(2.0)
    assert a.stabilise(4.0) == 2.0
