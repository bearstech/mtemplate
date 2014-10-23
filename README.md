µ template

Tiny template tool for devops.

## Build it

    virtualenv .
    source bin/activate
    pip install pex jinja2 wheel
    python setup.py sdist
    python setup.py bdist_wheel
    pex -r jinja2  -e mtemplate:main --repo=dist -r mtemplate -o mtemplate.pex

## Test it

    echo 'hello {{ENV.USER}}' | ./mtemplate.pex

# Licence

3 Terms BSD licence, © 2014 Mathieu Lecarme.
