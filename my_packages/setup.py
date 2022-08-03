from distutils.core import  setup

 #setup(name='压缩包的名字'，version='1.0',author='作者'，pymodules=['my_package.module1'])
setup(name='my_calibration', version='1.0', author='ZhaoQiChen', 
       py_modules=['mycalibration.ccalibration', 'mymeasure.cMonocularMeasure'])

# setup(name='my_measure', version=1.0, author='ZhaoQiChen', 
#        py_modules=['mymeasure.cMonocularMeasure'])