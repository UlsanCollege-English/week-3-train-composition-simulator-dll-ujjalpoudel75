from src.train import Train

def test_attach_detach_and_middle_remove():
    t = Train()
    for cid in ["E1", "E2", "C1"]:
        t.attach_back(cid)
    t.attach_front("L0")
    assert t.to_list() == ["L0", "E1", "E2", "C1"]
    assert t.detach_front() == "L0"
    assert t.detach_back() == "C1"
    assert t.to_list() == ["E1", "E2"]
    assert t.detach("E1") is True
    assert t.to_list() == ["E2"]
    assert t.detach("X") is False
