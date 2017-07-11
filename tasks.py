from invoke import task


@task
def build(ctx):
    ctx.run('python setup.py sdist', echo=True)
    ctx.run('python setup.py bdist_wheel', echo=True)


@task
def publish(ctx):
    clean(ctx)
    build(ctx)
    ctx.run('twine upload dist/*', echo=True)


@task
def clean(ctx):
    ctx.run("rm -rf build")
    ctx.run("rm -rf dist")
    ctx.run("rm -rf *.egg-info")
    print("Cleaned up.")
