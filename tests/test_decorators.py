import time
from utils import decorators


# pytest -s tests/test_decorators.py
def test_cost_time():
    @decorators.cost_time
    def demo_function():
        time.sleep(5)
    
    demo_function()
