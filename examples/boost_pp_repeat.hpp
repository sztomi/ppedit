/*
    This is a basic example of BOOST_PP_REPEAT.
    Try the following in the scratch window:

        BOOST_PP_REPEAT(5, DECL, int x)

    Adjust the number 5 to see change in the output.
*/

#include <boost/preprocessor/repetition/repeat.hpp>

#define DECL(z, n, text) text ## n = n;

