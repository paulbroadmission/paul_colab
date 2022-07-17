from setuptools import setup, find_packages
setup(
    name="paul_colab",
    version="0.1",
    packages=['colab'],
    install_requires=['ffmpeg-python', 'scipy', 'pillow', 'numpy'],

    # metadata to display on PyPI
    author="Paul Chao",
    author_email="chao@consultant.com",
    description="Useful Python tools for Google Colab",
    keywords="colab Colab colaboratory google Numpy PIL OpenCV",
    url="https://github.com/paulbroadmission/paul_colab",
    classifiers=[
        'Programming Language :: Python :: 3 :: Only' # https://pypi.org/classifiers/
    ]
)

# https://setuptools.readthedocs.io/en/latest/setuptools.html
