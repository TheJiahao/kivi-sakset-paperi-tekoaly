from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("pytest --cov --cov-branch --cov-report xml", pty=True)


@task
def coverage_report(ctx):
    ctx.run("pytest --cov --cov-branch --cov-report html", pty=True)


@task
def format(ctx):
    ctx.run("black src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def build(ctx):
    ctx.run("pyinstaller src/index.py -n ksp_peli -y")
