#include <boost/preprocessor/repetition/repeat.hpp>

#define DECL(z, n, text) text ## n = n;

/*
    Try the following in the sketch window:

        BOOST_PP_REPEAT(5, DECL, int x)

    Adjust the number 5 to see change in the output.
*/
