from cadence_pass.syncance import Syncance
from cadence_pass.rhythm import Rhythm
from cadence_pass.anchor_way import AnchorWay
from cadence_pass.cadence_pass import CadencePass

def test_cadence_pass_apply():
    s = Syncance(1.0)
    r = Rhythm("steady")
    a = AnchorWay(2.0)

    cp = CadencePass(r, a)
    result = cp.apply(s)

    # steady → len("steady") = 6
    # amplify: 1.0 * 6 = 6.0
    # stabilise: 6.0 / 2.0 = 3.0
    assert result == 3.0
