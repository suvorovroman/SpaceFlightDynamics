#include <X11/Xlib.h>
#include <string>
#include "../failure.h"
#include "../display.h"

namespace X11
{

  class display:public ::display
  {
  public:

    display(const char* _name = NULL);

    ~display();

    class failed_to_open:public failure
    {
    public:

      failed_to_open(const std::string& _name);
      
    };
    
  private:

    Display* D;
    
  };

}
