<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Registos de Exames Médicos Desportivos</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
              integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
              crossorigin="anonymous">
    </head>
    <body>
        <h1>Registos de Exames Médicos Desportivos</h1>

        <h2>Indicadores estatísticos</h2>

        <ul>
            <li>
                {{link(Age Gender distribution, age_gender_distrib.tpl)}}
                {{stats(age_gender_distrib)}}
            </li>

            <li>
                {{link(Federated by year , federated_by_year.tpl)}}
                {{stats(federated_by_year)}}
            </li>

            <li>
                {{link(Gender by year,gender_by_year.tpl)}}
                {{stats(gender_by_year)}}
            </li>
            <li>
                {{link(Location Distribution,location_distrib.tpl)}}
                {{stats(location_distrib)}}
            </li>

            <li>
                {{link(Results by year, result_by_year.tpl)}}
                {{stats(result_by_year)}}
            </li>

            <li>
                {{link(Sport by year, sport_by_year.tpl)}}
                {{stats(sport_by_year)}}
            </li>

            <li>
                {{link(Extreme dates, extreme_dates.tpl)}}
                {{stats(extreme_dates)}}
            </li>
        </ul>
    </body>
</html>