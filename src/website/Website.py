import stats.stats as stats


def boilerplate_html(title: str):
    return f"""<!DOCTYPE html>
<html lang="en">
   <head>
     <meta charset="UTF-8">
     <title>{title}</title>
   </head>
   <body>
       <header><h1>{title}</h1></header>
       <section>
       """ + '\n'.join(
        [f"<p>Year: {year}, Genders: {genders}" for year, genders in stats.get_stats('../../files/emd.csv').items()]) + """
       <a href='#'>Check This Year Distributions!</a>
       </section>
   </body>
</html>"""


index = open("../html/index2.html", "w", encoding='utf-8')

index.write(boilerplate_html("Registos de Exames Médicos Desportivos"))
