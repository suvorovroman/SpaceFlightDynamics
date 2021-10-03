#include "../instance.h"
#include "display.h"

int enter_instance_display(int (*_entry)(display& _d, instance& _i), instance& _i)
{
  X11::display d;
  return (*_entry)(d, _i);
}
