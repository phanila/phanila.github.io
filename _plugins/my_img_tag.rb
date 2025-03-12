# from https://stackoverflow.com/questions/61257609/how-to-remove-the-end-slash-from-the-img-tag/61264446#61264446
module Kramdown

    module Converter
  
      class Html < Base
  
        # Overriding method
        def convert_img(el, _indent)
          "<img#{html_attributes(el.attr)}>"
        end
  
      end
  
    end
  
  end