from distutils.core import setup
import py2exe
import zmq
import os
import matplotlib

os.environ["PATH"] = \
    os.environ["PATH"] + \
    os.path.pathsep + os.path.split(zmq.__file__)[0]

setup(
    name='KAT',
    version='',
    packages=['preproc'],
    url='',
    license='LGPL',
    author='Shirin',
    description='Knowledge Acquisition Toolkit',
    console=['src/MainGUI.py'],
    data_files=matplotlib.get_py2exe_datafiles(),
    zipfile = None,
    options={
        "py2exe": {
            #"ascii":True,  # Exclude encodings
            #"excludes":['_ssl','pyreadline', 'difflib', 'doctest', 'locale','optparse', 'pickle', 'calendar'],  # Exclude standard library
            #"dll_excludes":['libzmq.pyd','msvcr71.dll'],  # Exclude msvcr71
            "compressed":True,  # Compress library.zip
            "includes":["zmq.utils", "zmq.utils.jsonapi",
                 "zmq.utils.strtypes",
                 #"zmq.backend.cython",
                 "matplotlib.backends.backend_tkagg","pysparse",
                 'matplotlib.backends.backend_qt4agg',
                 'scipy.integrate', 'scipy.special.*','scipy.linalg.*','scipy.sparse.csgraph._validation',
                 'matplotlib.backends.backend_qt4agg','sklearn.utils.*','sklearn.neighbors.*','sklearn.utils.sparsetools._graph_validation']}}
)
#"scipy.special._ufuncs_cxx","scipy.linalg.cython_blas"]}}
#'scipy',

