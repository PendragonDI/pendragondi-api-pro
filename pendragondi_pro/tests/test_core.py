import time
from pendragondi_api_pro import duplicate_guard, duplicate_guard_pro, get_event_log
from pendragondi_api_pro.redact import default_redactor

def test_duplicate_within_window():
    log = get_event_log()
    log.clear()
    @duplicate_guard
    def f(x): return x
    f(1); f(1)
    events = [e for e in log.snapshot() if e.get("duplicate")]
    assert len(events) >= 1

def test_not_duplicate_after_window():
    log = get_event_log()
    log.clear()
    @duplicate_guard_pro(window_ms=200)
    def g(x): return x
    g(2); time.sleep(0.25); g(2)
    dups = [e for e in log.snapshot() if e.get("duplicate")]
    assert len(dups) >= 1

def test_redaction():
    log = get_event_log()
    log.clear()
    @duplicate_guard_pro(capture_args=True, redact=default_redactor)
    def h(token, user_id): return True
    h("super_secret_token_abc123", "u1")
    events = [e for e in log.snapshot() if e.get("call")]
    assert any("***" in str(e["call"]["kwargs"].get("token", "")) for e in events)