from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        Extension("nek5000_cy", sources=["nek5000_cy.pyx"], libraries=["nek5000"])
    )
)
