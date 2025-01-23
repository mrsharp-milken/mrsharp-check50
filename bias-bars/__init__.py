import check50

@check50.check()
def exists():
    """biasbars files exists"""
    check50.exists("biasbars.py")
    check50.exists("rating_stats.py")
    check50.exists("biasbarsgui.py")
    check50.exists("biasbarsdata.py")
    check50.exists("ethics.txt")


