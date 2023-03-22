from invoke import task


@task
def start(ctx):
    pass


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage_report(ctx):
    ctx.run("pytest --cov --cov-branch --cov-report html", pty=True)
