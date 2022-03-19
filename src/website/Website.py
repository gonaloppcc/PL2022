import stats.stats as stats


def boilerplate_html(title: str, header_h1: str = "Header h1"):
    return f"""<!DOCTYPE html>
<html lang="en">
   <head>
     <meta charset="UTF-8">
     <title>{title}</title>
   </head>
   <body>
       <header><h1>{header_h1}</h1></header>
       <section>
       """ + '\n'.join([f"<p>Year: {year}, Genders: {genders}" for year, genders in stats.get_stats('../../files/emd.csv').items()]) + """
       </section>
   </body>
</html>"""


index = open("../html/index2.html", "w", encoding='utf-8')

index.write(boilerplate_html("Website"))
