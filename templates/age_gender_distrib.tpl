<!DOCTYPE html>
<html>
    <head>
        <title>{{name(age_gender_distrib)}}</title>
        <link rel="stylesheet" href="style.css">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>

    <body>
        <h1>{{name(age_gender_distrib)}}</h1>
        <h2>Athletes</h2>
        {{data(age_gender_distrib)}}
    </body>
</html>