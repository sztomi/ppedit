/*
   This metaprogram can be used to generate smart/reflective enums.

   Try this in the scratch window:

       SMARTENUM(Color, (Red)(Green)(Blue)(Purple))

   Add/remove items to the enum to see the change in the output.
*/

#include <boost/preprocessor.hpp>

#define STR_TO_ENUM(r, data, elem)                                             \
  if (!strcmp(s, BOOST_PP_STRINGIZE(elem)))                                    \
    return data::elem;

#define ENUM_TO_STR(r, data, elem)                                             \
  case data::elem:                                                             \
    return BOOST_PP_STRINGIZE(data::elem);

#define SMARTENUM(name, enumerators)                                           \
  enum class name { BOOST_PP_SEQ_ENUM(enumerators) };                          \
  const name FromString(const char *s) {                                       \
    BOOST_PP_SEQ_FOR_EACH(STR_TO_ENUM, name, enumerators)                      \
    throw std::runtime_error("Invalid enumerator name");                       \
  }                                                                            \
  const char *ToString(name value) {                                           \
    switch (value) {                                                           \
      BOOST_PP_SEQ_FOR_EACH(ENUM_TO_STR, name, enumerators)                    \
    default:                                                                   \
      throw std::runtime_error("Invalid enum value");                          \
    }                                                                          \
  }
