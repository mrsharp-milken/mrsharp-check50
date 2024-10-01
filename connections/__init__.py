import check50
import check50.c


@check50.check()
def exists():
    """connections.c exists"""
    check50.exists("connections.c")


@check50.check(exists)
def compiles():
    """connections.c compiles"""
    check50.c.compile("connections.c", lcs50=True)
