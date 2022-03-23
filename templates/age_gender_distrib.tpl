<!DOCTYPE html>
<html>
    <head>
        <title>Gender distribuition by age</title>
        <link rel="stylesheet" href="style.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>

    <body>
        <h1>< 35</h1>
        <h2>M</h2>
            {{stats.age_gender_distrib['distrib']['< 35']['M']}}
        <h2>F</h2>
            {{stats.age_gender_distrib['distrib']['< 35']['F']}}
        <h1>>= 35</h1>
        <h2>M</h2>
            {{stats.age_gender_distrib['distrib']['>= 35']['M']}}
        <h2>F</h2>
            {{stats.age_gender_distrib['distrib']['>= 35']['F']}}
    </body>
</html>