@echo off
if "%1"=="test" goto :TEST
if "%1"=="pypi" goto :PYPI

python setup.py sdist bdist_wininst bdist_egg bdist_wheel
goto :EXIT

:TEST
python setup.py register -r test
echo *** END REGISTER ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel upload -r test
goto :EXIT

:PYPI
python setup.py register -r pypi
echo *** END REGISTER ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel upload -r pypi

:EXIT
