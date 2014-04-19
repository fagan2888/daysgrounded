@echo off
if "%1"=="pubtest" goto :PUBTEST
if "%1"=="pubfinal" goto :PUBFINAL

python setup.py sdist bdist_wininst bdist_egg bdist_wheel
goto :EXIT

:PUBTEST
python setup.py register -r test
echo *** END REGISTER ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel upload -r test
goto :EXIT

:PUBFINAL
python setup.py register -r pypi
echo *** END REGISTER ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel
echo *** END BUILD ***
python setup.py sdist bdist_wininst bdist_egg bdist_wheel upload -r pypi

:EXIT
