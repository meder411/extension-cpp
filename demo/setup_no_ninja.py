from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='lltm_cuda',
    ext_modules=[
        CppExtension(
            'lltm_cuda',
            [
                'lltm_cuda.cpp',
            ],
            include_dirs=['includes'],
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension.with_options(use_ninja=False)
    })
