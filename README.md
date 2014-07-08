#GOAL

Automate all the things!


First thing I want to automate is TDD process,
which is:

- well defined
- structured
- predictable


Typical double loop, outside in tdd process can be modelled as:

```
while code_not_ready:

    write functional tests
    watch it fail

    while functional test is failing on some feature:
        write some unit tests
        while unit_tests_are_failing:
            watch them fail
            write some implementation
```

What if someone run you tests after each change in the codebase?
If there were any errors, look for them in the interne?
If you use new library in a wrong way, it will pull `source graph`
for examples.

It will check your coverage and hint which parts of the code you should test more.

It'll autoformat your code to adhere to defined standards and add docs' stubs.

It'll store all your diffs after each save and show in pretty way.

And it should learn and get better the more you use it.


