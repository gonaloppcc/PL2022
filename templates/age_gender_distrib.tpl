<!DOCTYPE html>
<html>
    <head>
        <title>Gender distribuition by age</title>
    </head>

    <body>
        <h1>< 35</h1>
        <h2>M</h2>
            {{stats.age_gender_distrib['< 35']['M']}}
        <h2>F</h2>
            {{stats.age_gender_distrib['< 35']['F']}}
        <h1>>= 35</h1>
        <h2>M</h2>
            {{stats.age_gender_distrib['>= 35']['M']}}
        <h2>F</h2>
            {{stats.age_gender_distrib['>= 35']['F']}}
    </body>
</html>