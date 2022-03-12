def boilerplate_html(title: str, header_h1: str = "Header h1"):
    return f"""<!DOCTYPE html>
<html lang="en">
   <head>
     <meta charset="UTF-8">
     <title>{title}</title>
   </head>
   
   <body>
       <header><h1>{header_h1}</h1></header>
   </body>
</html>
    """


index = open("index.html", "w", encoding='utf-8')

index.write(boilerplate_html("Website"))
