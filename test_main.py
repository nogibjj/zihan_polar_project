from main import get_statistics, build_barplot

def test_statistics():
    result1 = get_statistics()
    assert result1 is None

def test_plot():
    result2 = build_barplot()
    assert result2 is None

if __name__=="__main__":
    test_statistics()
    test_plot()