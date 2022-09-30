import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="TempEnv",
    version="0.0.1",
    author="Blockhead-yj",
    author_email="136271877@qq.com",
    description="create a temporary environment to execute some code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="not yet",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
