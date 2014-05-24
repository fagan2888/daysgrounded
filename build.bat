@echo off

rd /s /q build
rd /s /q dist
rd /s /q daysgrounded.egg-info
rd /s /q daysgrounded-0.0.15
del daysgrounded\*.pyc

if "%1"=="test" goto :TEST
if "%1"=="pypi" goto :PYPI
if "%1"=="cxf" goto :CXF
if "%1"=="py2exe" goto :PY2EXE

python setup.py sdist bdist_egg bdist_wininst bdist_wheel
goto :EXIT

:TEST
python setup.py register -r test
echo *** END REGISTER ***
python setup.py sdist bdist_egg bdist_wininst bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r test
goto :EXIT

:PYPI
python setup.py register -r pypi
echo *** END REGISTER ***
python setup.py sdist bdist_egg bdist_wininst bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r pypi
goto :EXIT

:CXF
python cxfreeze_setup.py build_exe
rem cxfreeze setup.py build_exe
goto :EXIT

:PY2EXE
python setup.py py2exe

:EXIT
