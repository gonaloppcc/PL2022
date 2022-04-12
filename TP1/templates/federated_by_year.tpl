<!DOCTYPE html>
<html>
    <head>
        <title>{{name(federated_by_year)}}</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    </head>

    <body>
        <h1>{{name(federated_by_year)}}</h1>
        <h2>Athletes</h2>
        {{data(federated_by_year)}}
    </body>
</html>