from prefect import task
from prefect.tasks.control_flow import switch


@task
def handle_zero():
    return float("nan")


with Flow("math") as f:
    x, y = Parameter("x"), Parameter("y")
    a = x + y
    switch(a, cases={0: handle_zero(), 1: 6 / a})

# if running in an Jupyter notebook,
# visualize will render in-line, otherwise
# a new window will open
f.visualize()
